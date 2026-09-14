document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const imagePreview = document.getElementById('imagePreview');
    const form = document.getElementById('uploadForm');
    const submitBtn = document.getElementById('submitBtn');

    // Show image preview locally before upload
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
                // Hide the default text and icon when image is shown
                document.querySelector('.upload-icon').style.display = 'none';
                document.querySelector('.upload-zone p').style.display = 'none';
            }
            reader.readAsDataURL(file);
        }
    });

    // Provide visual feedback during processing
    form.addEventListener('submit', function() {
        submitBtn.textContent = 'Analyzing...';
        submitBtn.disabled = true;
    });
});