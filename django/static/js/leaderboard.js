async function fetchLeaderboard() {
    try {
        const response = await fetch('/api/leaderboard/');
        const data = await response.json();

        if (response.ok) {
            const leaderboardContainer = document.getElementById('leaderboard-container');
            const leaderboardTable = document.createElement('table');
            leaderboardTable.classList.add('table', 'table-striped');
            leaderboardTable.innerHTML = `
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Username</th>
                        <th>Wins</th>
                        <th>Losses</th>
                    </tr>
                </thead>
                <tbody>
            `;

            data.leaderboard.forEach((profile, index) => {
                leaderboardTable.innerHTML += `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${profile.username}</td>
                        <td>${profile.wins}</td>
                        <td>${profile.losses}</td>
                    </tr>
                `;
            });

            leaderboardTable.innerHTML += '</tbody>';
            leaderboardContainer.innerHTML = '';
            leaderboardContainer.appendChild(leaderboardTable);
        } else {
            console.error('Failed to fetch leaderboard:', data);
        }
    } catch (error) {
        console.error('Error fetching leaderboard:', error);
    }
}

fetchLeaderboard();