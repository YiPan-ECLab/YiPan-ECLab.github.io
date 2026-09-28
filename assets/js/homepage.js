(() => {
  const search = document.getElementById('paper-search');
  const papers = [...document.querySelectorAll('.paper')];
  if (search) {
    document.querySelector('.publication-tools').hidden = false;
    const filter = () => {
      const query = search.value.toLowerCase().trim();
      let count = 0;
      papers.forEach(paper => {
        paper.hidden = !(paper.dataset.search + ' ' + paper.textContent).toLowerCase().includes(query);
        if (!paper.hidden) count++;
      });
      document.getElementById('result-count').textContent = `${count} of ${papers.length} papers`;
      document.getElementById('no-results').hidden = count !== 0;
    };
    search.addEventListener('input', filter);
    filter();
  }
  if (navigator.clipboard) document.querySelectorAll('.copy-bib').forEach(button => {
    button.hidden = false;
    button.addEventListener('click', async () => {
      const status = button.parentElement.querySelector('.copy-status');
      try {
        await navigator.clipboard.writeText(button.parentElement.querySelector('code').textContent);
        status.textContent = 'Copied';
      } catch (_) { status.textContent = 'Select the citation text to copy.'; }
    });
  });
})();
