const textarea = document.querySelector('textarea');
const hozon = document.querySelector('.hozon');

hozon.disabled = true;  // 最初は無効

textarea.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 300) + 'px';
    
    if (this.value === '') {
        hozon.disabled = true;
    } else {
        hozon.disabled = false;
    }
});
document.getElementById('iconInput').addEventListener('change', function(e) {
  const file = e.target.files[0];
  const reader = new FileReader();
  
  reader.onload = function(e) {
    document.getElementById('iconPreview').src = e.target.result;
  };
  
  reader.readAsDataURL(file);
});
const commentInput = document.querySelector('.comment');

commentInput.addEventListener('blur', function() {
    // フォーカスが外れたとき
    fetch('/save_comment/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1]
        },
        body: JSON.stringify({comment: this.value})
    });
});

commentInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        this.blur();
    }
});