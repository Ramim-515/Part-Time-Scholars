// post_job.js
document.addEventListener('DOMContentLoaded', function() {
    // Initialize date picker for deadline field
    const deadlineField = document.getElementById('id_deadline');
    if (deadlineField) {
        deadlineField.min = new Date().toISOString().split('T')[0];
    }

    // Character counter for textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        const counter = document.createElement('div');
        counter.className = 'text-end text-muted small mt-1';
        textarea.parentNode.appendChild(counter);
        
        textarea.addEventListener('input', function() {
            counter.textContent = `${this.value.length}/2000 characters`;
        });
    });
});