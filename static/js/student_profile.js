// student_profile.js
document.addEventListener('DOMContentLoaded', function() {
    // Download resume button animation
    const downloadBtn = document.querySelector('.btn-outline-primary');
    if (downloadBtn) {
        downloadBtn.addEventListener('mouseenter', function() {
            this.innerHTML = '⬇️ Download Resume';
        });
        downloadBtn.addEventListener('mouseleave', function() {
            this.innerHTML = '📄 Download Resume';
        });
    }

    // Edit profile button animation
    const editBtn = document.querySelector('.btn-primary');
    if (editBtn) {
        editBtn.addEventListener('mouseenter', function() {
            this.innerHTML = '✏️ Edit Profile &nbsp;&rarr;';
        });
        editBtn.addEventListener('mouseleave', function() {
            this.innerHTML = '✏️ Edit Profile';
        });
    }
});