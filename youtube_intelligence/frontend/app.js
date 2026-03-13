const API = window.location.origin;

let chart;

async function loadData() {
  const response = await fetch(`${API}/metrics`);
  const data = await response.json();

  renderChart(data);
}

function renderChart(data) {
  if (chart) {
    chart.destroy();
  }

  const channels = [...new Set(data.map((d) => d.channel_name))];

  const datasets = channels.map((channel) => {
    const filtered = data
      .filter((d) => d.channel_name === channel)
      .sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));

    return {
      label: channel,
      data: filtered.map((d) => d.subscribers),
      borderWidth: 2,
      fill: false,
    };
  });

  const labels = data
    .filter((d) => d.channel_name === channels[0])
    .map((d) => d.timestamp);

  chart = new Chart(document.getElementById("subsChart"), {
    type: "line",
    data: {
      labels: labels,
      datasets: datasets,
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: "Channel Subscribers Over Time",
        },
      },
    },
  });
}

loadData();
