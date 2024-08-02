// Optional JavaScript for additional interactivity
document.addEventListener('DOMContentLoaded', function() {
    console.log("Webpage Loaded!");
});

function handleCredentialResponse(response) {
    console.log("Encoded JWT ID token: " + response.credential);
    // Send the ID token to your backend for verification and further processing
}

// Initialize the Google Sign-In API
window.onload = function () {
    google.accounts.id.initialize({
        client_id: "YOUR_CLIENT_ID",
        callback: handleCredentialResponse
    });
    google.accounts.id.renderButton(
        document.querySelector(".g_id_signin"),
        { theme: "outline", size: "large" }  // customization options
    );
    google.accounts.id.prompt(); // display the One Tap dialog
};
