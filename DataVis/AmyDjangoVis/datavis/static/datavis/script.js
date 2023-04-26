// script.js
document.addEventListener('DOMContentLoaded', function() {
  fetch('/get_plot_json')
    .then(response => response.json())
    .then(data => {
      Plotly.newPlot('plot_json', data);
    });
});
