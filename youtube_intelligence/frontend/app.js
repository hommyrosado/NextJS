const API = window.location.origin;

let chart;

async function loadData() {
  const response = await fetch(`${API}/metrics`);
  const data = await response.json();

  const channels = [...new Set(data.map((d) => d.channel_name))];

  const list = document.getElementById("channel-list");

  channels.forEach((name) => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.textContent = name;

    li.onclick = () => renderChart(name, data);

    list.appendChild(li);
  });
}

function renderChart(channel, data) {
  if (chart) {
    chart.destroy();
  }

  const filtered = data.filter((d) => d.channel_name === channel);

  const labels = filtered.map((d) => d.timestamp);
  const subs = filtered.map((d) => d.subscribers);

  chart = new Chart(document.getElementById("subsChart"), {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: channel + " Subscribers",
          data: subs,
        },
      ],
    },
  });
}

loadData();
