// job_details.js
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for any anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Highlight important dates
    const deadlineElement = document.querySelector('li:first-child');
    if (deadlineElement) {
        const deadlineText = deadlineElement.textContent;
        const deadlineDate = new Date(deadlineText.split(': ')[1]);
        const today = new Date();
        
        if (deadlineDate < today) {
            deadlineElement.style.color = '#dc3545';
            deadlineElement.innerHTML += ' <span class="badge bg-danger">Expired</span>';
        } else if ((deadlineDate - today) / (1000 * 60 * 60 * 24) < 7) {
            deadlineElement.style.color = '#fd7e14';
            deadlineElement.innerHTML += ' <span class="badge bg-warning text-dark">Closing Soon</span>';
        }
    }
});