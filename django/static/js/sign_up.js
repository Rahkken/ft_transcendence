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
        } 
        else if (response.status === 400) {
            const formFields = form.querySelectorAll('.form-group');
            formFields.forEach((field) => {
                const errorDiv = field.querySelector('.error-message');
                if (errorDiv) {
                    errorDiv.remove();
                }
            });

            Object.entries(result.errors).forEach(([fieldName, errors]) => {
                const inputField = form.querySelector(`[name="${fieldName}"]`);
                if (inputField) {
                    const formGroup = inputField.closest('.form-group');
                    if (formGroup) {
                        const errorDiv = document.createElement('div');
                        errorDiv.className = 'error-message text-danger';
                        errorDiv.textContent = errors.join(', ');
                        formGroup.appendChild(errorDiv);
                    }
                }
            });
        }
    } catch (error) {
        console.error('Error submitting form:', error);
        alert('An error occurred. Please try again later.');
    }
}