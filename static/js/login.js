// login.js
document.addEventListener('DOMContentLoaded', function() {
    // Focus on first input field
    const firstInput = document.querySelector('input[type="text"], input[type="email"]');
    if (firstInput) {
        firstInput.focus();
    }
    
    // Add password toggle
    const passwordInput = document.querySelector('input[type="password"]');
    if (passwordInput) {
        const toggle = document.createElement('span');
        toggle.innerHTML = '👁️';
        toggle.style.position = 'absolute';
        toggle.style.right = '10px';
        toggle.style.top = '50%';
        toggle.style.transform = 'translateY(-50%)';
        toggle.style.cursor = 'pointer';
        
        const parent = passwordInput.parentNode;
        parent.style.position = 'relative';
        parent.appendChild(toggle);
        
        toggle.addEventListener('click', function() {
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                toggle.innerHTML = '👁️‍🗨️';
            } else {
                passwordInput.type = 'password';
                toggle.innerHTML = '👁️';
            }
        });
    }
});