async function submitSignupForm(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    try {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const response = await fetch('/api/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(jsonData),
        });

        const result = await response.json();

        if (response.status === 201) {
            alert(result.message);
            window.location.href = result.redirect_url;
        } else if (response.status === 400) {
            const errorContainer = document.getElementById('error-messages');
            errorContainer.innerHTML = '';

            Object.entries(result.errors).forEach(([field, errors]) => {
                const error = document.createElement('p');
                error.textContent = `${field}: ${errors.join(', ')}`;
                errorContainer.appendChild(error);
            });
        }
    } catch (error) {
        console.error('Error submitting form:', error);
        alert('An error occurred. Please try again later.');
    }
}