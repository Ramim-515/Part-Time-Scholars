// employer_dashboard.js
document.addEventListener('DOMContentLoaded', function() {
    // Confirm before deleting job
    const deleteForms = document.querySelectorAll('form[onsubmit]');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!confirm('Are you sure you want to delete this job?')) {
                e.preventDefault();
            }
        });
    });
    
    // Make table rows hoverable
    const tableRows = document.querySelectorAll('tbody tr');
    tableRows.forEach(row => {
        row.style.transition = 'background-color 0.2s ease';
        row.addEventListener('mouseenter', () => {
            row.style.backgroundColor = '#f8f9fa';
        });
        row.addEventListener('mouseleave', () => {
            row.style.backgroundColor = '';
        });
    });
});