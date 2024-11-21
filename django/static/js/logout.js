async function logoutUser() {
    try {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const response = await fetch('/api/logout/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json',
            }
        });

        const result = await response.json();

        if (response.status === 200) {
            alert(result.message);
            window.location.href = result.redirect_url;
        } else if (response.status === 400) {
            alert(result.error);
        }
    } catch (error) {
        console.error('Logout failed:', error);
        alert('An error occurred. Please try again.');
    }
}