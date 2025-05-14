// apply_job.js
document.addEventListener('DOMContentLoaded', function() {
    // Character counter for textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        const counter = document.createElement('div');
        counter.className = 'text-end text-muted small mt-1';
        textarea.parentNode.appendChild(counter);
        
        textarea.addEventListener('input', function() {
            counter.textContent = `${this.value.length}/1000 characters`;
        });
    });
});