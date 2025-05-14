// edit_profile.js
document.addEventListener('DOMContentLoaded', function() {
    // Preview image before upload
    const fileInput = document.querySelector('input[type="file"]');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    const preview = document.createElement('img');
                    preview.src = event.target.result;
                    preview.style.maxWidth = '150px';
                    preview.style.marginTop = '10px';
                    preview.style.borderRadius = '8px';
                    
                    const existingPreview = fileInput.nextElementSibling;
                    if (existingPreview && existingPreview.tagName === 'IMG') {
                        existingPreview.remove();
                    }
                    
                    fileInput.parentNode.appendChild(preview);
                };
                reader.readAsDataURL(file);
            }
        });
    }
});