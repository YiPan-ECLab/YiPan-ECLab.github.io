"""Check publication integrity and the generated site's local links."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
papers = json.loads((ROOT / '_data/publications.json').read_text())
assert papers, 'Publication list is empty'
assert len({p['id'] for p in papers}) == len(papers), 'Duplicate publication IDs'
for paper in papers:
    assert 'Yi Pan' in paper['authors'], f"Author mismatch: {paper['title']}"
    assert paper['date'][:4] == str(paper['year'])
    for link in paper['links']:
        assert urlparse(link['url']).scheme == 'https'

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key): self.links.append(a[key])

for file in SITE.rglob('*.html'):
    content = file.read_text()
    assert not re.search(r'\{%|\{\{', content), f'Unrendered Liquid: {file}'
    parser = Links(); parser.feed(content)
    for href in parser.links:
        u = urlparse(href)
        if u.scheme or u.netloc: continue
        path = unquote(u.path)
        if not path:
            if u.fragment: assert u.fragment in parser.ids, f'Missing anchor {href}'
            continue
        target = SITE / path.lstrip('/') if path.startswith('/') else file.parent / path
        if path.endswith('/'): target /= 'index.html'
        assert target.exists(), f'Broken local link: {href} in {file}'
        if u.fragment and target.suffix == '.html':
            target_parser = Links(); target_parser.feed(target.read_text())
            assert u.fragment in target_parser.ids, f'Missing anchor {href}'
# Draft-only papers must not leak through generated pages or data downloads.
draft_path = ROOT / 'work/all-publications.json'
if draft_path.exists():
    public_ids = {p['id'] for p in papers}
    draft_ids = {p['id'] for p in json.loads(draft_path.read_text())} - public_ids
    for file in SITE.rglob('*'):
        if file.is_file() and file.suffix in {'.html','.json','.xml','.js','.md','.yml','.txt'}:
            text = file.read_text()
            assert not any(i in text for i in draft_ids), f'Draft content in published output: {file}'
assert not (SITE / 'work').exists(), 'Local drafts must be excluded'
assert not (SITE / 'SOURCES.md').exists(), 'Internal source notes should not be rendered'
print(f'PASS: {len(papers)} public papers; author/date/URL checks, local links, anchors, and draft isolation.')
