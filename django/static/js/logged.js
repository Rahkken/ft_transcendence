async function checkUserStatus() {
    try {
        const response = await fetch('/api/userstatus/');
        const data = await response.json();

        if (data.is_logged_in) {
            document.getElementById('profile-link').style.display = 'inline-block';
            document.getElementById('leaderboard-link').style.display = 'inline-block';
            document.getElementById('game-link').style.display = 'inline-block';
            document.getElementById('tournaments-link').style.display = 'inline-block';
            document.getElementById('chat-link').style.display = 'inline-block';
            document.getElementById('logout-link').style.display = 'inline-block';
            document.getElementById('login-link').style.display = 'none';
            document.getElementById('signup-link').style.display = 'none';

            const userMessage = `Welcome, ${data.username}`;
            document.getElementById('main-content').innerHTML = `<h1 class="text-center mb-4">${userMessage}</h1>`;
        } else {
            document.getElementById('login-link').style.display = 'inline-block';
            document.getElementById('signup-link').style.display = 'inline-block';
            document.getElementById('profile-link').style.display = 'none';
            document.getElementById('leaderboard-link').style.display = 'none';
            document.getElementById('game-link').style.display = 'none';
            document.getElementById('tournaments-link').style.display = 'none';
            document.getElementById('chat-link').style.display = 'none';
            document.getElementById('logout-link').style.display = 'none';
        }
    } catch (error) {
        console.error('Error fetching user status:', error);
    }
}

window.onload = checkUserStatus;