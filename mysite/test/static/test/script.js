const textarea = document.querySelector('textarea');
const hozon = document.querySelector('.hozon');

hozon.disabled = true;  // 最初は無効

textarea.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 72) + 'px';
    
    if (this.value === '') {
        hozon.disabled = true;
    } else {
        hozon.disabled = false;
    }
});