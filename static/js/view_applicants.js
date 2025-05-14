// view_applicants.js
document.addEventListener('DOMContentLoaded', function() {
    // Add expand/collapse functionality for long text
    const applicants = document.querySelectorAll('.list-group-item');
    applicants.forEach(applicant => {
        const coverLetter = applicant.querySelector('p:nth-of-type(1)');
        const experience = applicant.querySelector('p:nth-of-type(2)');
        
        if (coverLetter && coverLetter.textContent.length > 150) {
            coverLetter.dataset.fullText = coverLetter.innerHTML;
            coverLetter.innerHTML = coverLetter.textContent.slice(0, 150) + '...';
            
            const toggleBtn = document.createElement('button');
            toggleBtn.className = 'btn btn-sm btn-link p-0 ms-2';
            toggleBtn.textContent = 'Read more';
            toggleBtn.addEventListener('click', function() {
                if (coverLetter.textContent.length > 150) {
                    coverLetter.innerHTML = coverLetter.dataset.fullText;
                    toggleBtn.textContent = 'Show less';
                } else {
                    coverLetter.innerHTML = coverLetter.dataset.fullText.slice(0, 150) + '...';
                    toggleBtn.textContent = 'Read more';
                }
            });
            
            coverLetter.parentNode.insertBefore(toggleBtn, coverLetter.nextSibling);
        }
        
        if (experience && experience.textContent.length > 150) {
            experience.dataset.fullText = experience.innerHTML;
            experience.innerHTML = experience.textContent.slice(0, 150) + '...';
            
            const toggleBtn = document.createElement('button');
            toggleBtn.className = 'btn btn-sm btn-link p-0 ms-2';
            toggleBtn.textContent = 'Read more';
            toggleBtn.addEventListener('click', function() {
                if (experience.textContent.length > 150) {
                    experience.innerHTML = experience.dataset.fullText;
                    toggleBtn.textContent = 'Show less';
                } else {
                    experience.innerHTML = experience.dataset.fullText.slice(0, 150) + '...';
                    toggleBtn.textContent = 'Read more';
                }
            });
            
            experience.parentNode.insertBefore(toggleBtn, experience.nextSibling);
        }
    });
});