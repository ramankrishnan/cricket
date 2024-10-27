function fetchMatchStats() {
    fetch("http://backend-service:5000/api/match_stats")
        .then(response => response.json())
        .then(data => {
            document.getElementById("match-stats").innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error("Error fetching match stats:", error));
}
window.onload = fetchMatchStats;
