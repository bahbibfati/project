document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get username and password input values
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Check if username and password are correct (you can replace this with your own authentication logic)
    if (username === "admin" && password === "password") {
      // Display a success message
      document.getElementById("message").textContent = "Login successful!";
      
      // Redirect to the dashboard page
      window.location.href = "dashboard.html";
    } else {
      // Display an error message
      document.getElementById("message").textContent = "Invalid username or password";
    }
  });