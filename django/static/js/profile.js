fetchUserProfile();

async function fetchUserProfile() {
    try {
        const profileDiv = document.getElementById('profile-container');
        const username = profileDiv.getAttribute('username');
        const response = await fetch(`/api/profile/${username}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (response.status === 200) {
            const data = await response.json();
            renderUserProfile(data);
        } else if (response.status === 404) {
            alert("User not found");
        } else {
            alert("An error occurred while fetching the profile");
        }
    } catch (error) {
        console.error("Error fetching profile:", error);
    }
}

function renderUserProfile(data) {
    const profileContainer = document.getElementById('profile-container');

    profileContainer.innerHTML = `
        <h1>${data.username}'s Profile</h1>
        <p>Email: ${data.email}</p>
        <p>Wins: ${data.wins}</p>
        <p>Losses: ${data.losses}</p>
        <h3>Friends</h3>
        <ul>
            ${data.friends.map(friend => `<li>${friend}</li>`).join('')}
        </ul>
        <h3>Blocklist</h3>
        <ul>
            ${data.blocklist.map(user => `<li>${user}</li>`).join('')}
        </ul>
        <h3>Latest Matches</h3>
        <ul>
            ${data.latest_matches.map(match => `
                <li>Opponent: ${match.opponent}, Score: ${match.score}, Date: ${match.timestamp}</li>
            `).join('')}
        </ul>
    `;
}