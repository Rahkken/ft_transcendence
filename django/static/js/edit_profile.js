    // const profileInfo = document.getElementById('profile-info');
    // const editFormContainer = document.getElementById('edit-profile-form-container');
    // const editForm = document.getElementById('edit-profile-form');
    // const message = document.getElementById('message');
    // const editBtn = document.getElementById('edit-profile-btn');

    // // Fetch profile info on load
    // fetch('/api/profile/', {
    //     method: 'GET',
    //     headers: {
    //         'Content-Type': 'application/json',
    //     },
    // })
    //     .then(response => response.json())
    //     .then(data => {
    //         profileInfo.innerHTML = `
    //             <p><strong>Username:</strong> ${data.username}</p>
    //             <p><strong>Email:</strong> ${data.email}</p>
    //         `;
    //     })
    //     .catch(error => {
    //         console.error('Error fetching profile:', error);
    //         profileInfo.innerHTML = '<p>Error loading profile data.</p>';
    //     });

    // // Show the edit form
    // editBtn.addEventListener('click', () => {
    //     editFormContainer.style.display = 'block';

    //     // Populate form fields with current profile data
    //     fetch('/api/profile/', {
    //         method: 'GET',
    //         headers: {
    //             'Content-Type': 'application/json',
    //         },
    //     })
    //         .then(response => response.json())
    //         .then(data => {
    //             editForm.username.value = data.username;
    //             editForm.email.value = data.email;
    //         })
    //         .catch(error => {
    //             console.error('Error fetching profile for edit:', error);
    //         });
    // });

    // // Handle profile updates
    // editForm.addEventListener('submit', (event) => {
    //     event.preventDefault();

    //     const formData = new FormData(editForm);

    //     fetch('/api/profile/update/', {
    //         method: 'POST',
    //         body: formData,
    //     })
    //         .then(response => response.json())
    //         .then(data => {
    //             if (data.message) {
    //                 message.textContent = data.message;
    //                 message.style.color = 'green';
    //                 editFormContainer.style.display = 'none';
    //                 location.reload(); // Reload profile data
    //             } else if (data.errors) {
    //                 message.textContent = `Error: ${JSON.stringify(data.errors)}`;
    //                 message.style.color = 'red';
    //             }
    //         })
    //         .catch(error => {
    //             console.error('Error updating profile:', error);
    //             message.textContent = 'Error updating profile.';
    //             message.style.color = 'red';
    //         });
    // });

    fetchUserProfileForEdit();

    async function fetchUserProfileForEdit() {
        try {
            const profileDiv = document.getElementById('edit-profile-container');
            const username = profileDiv.getAttribute('username');
    
            if (!username) {
                console.error("Username attribute not found on the profile container.");
                profileDiv.innerHTML = '<p>Error: Unable to fetch user profile for editing. Username missing.</p>';
                return;
            }
    
            const response = await fetch(`/api/profile/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
    
            if (response.status === 200) {
                const data = await response.json();
                renderEditProfileForm(data);
            } else if (response.status === 404) {
                alert("User not found");
            } else {
                alert("An error occurred while fetching the profile for editing.");
            }
        } catch (error) {
            console.error("Error fetching profile for editing:", error);
        }
    }
    
    function renderEditProfileForm(data) {
        const profileContainer = document.getElementById('edit-profile-container');
    
        profileContainer.innerHTML = `
            <h1>Edit Profile</h1>
            <form id="edit-profile-form">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" value="${data.username}" required />
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" value="${data.email}" required />
                
                <button type="submit">Save Changes</button>
            </form>
        `;
    
        // Attach event listener to the form
        const form = document.getElementById('edit-profile-form');
        form.addEventListener('submit', handleProfileEdit);
    }
    
    async function handleProfileEdit(event) {
        event.preventDefault();
    
        const form = event.target;
        const username = form.username.value;
        const email = form.email.value;
    
        try {
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            const response = await fetch(`/api/profile/update/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    username: username,
                    email: email,
                }),
            });
    
            if (response.status === 200) {
                const data = await response.json();
                alert('Profile updated successfully!');
                renderEditProfileForm(data); // Refresh the form with the latest data
            } else if (response.status === 400) {
                alert("Invalid data. Please check your input.");
            } else {
                alert("An error occurred while updating the profile.");
            }
        } catch (error) {
            console.error("Error updating profile:", error);
        }
    }
    