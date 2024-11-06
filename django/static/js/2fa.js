function toggle2FA() {

    fetch("/toggle-2fa/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
        }
    })
    .then(response => response.json())
    .then(data => {
        const message = document.getElementById("toggleMessage");
        if (data.status === true) {
            message.innerText = "2FA has been enabled.";
            document.getElementById("toggle2faButton").innerText = "Disable 2FA";
        } else if (data.status === false) {
            message.innerText = "2FA has been disabled.";
            document.getElementById("toggle2faButton").innerText = "Enable 2FA";
        } else {
            message.innerText = data.error;
        }
    })
    .catch(error => console.error("Error:", error));
}