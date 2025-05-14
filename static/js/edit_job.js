// edit_job.js
document.addEventListener('DOMContentLoaded', function() {
    // Add date picker for date fields
    const dateFields = document.querySelectorAll('input[type="date"]');
    dateFields.forEach(field => {
        field.classList.add('form-control');
    });
});