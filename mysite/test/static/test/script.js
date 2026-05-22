const textarea = document.querySelector('textarea');
textarea.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 72) + 'px';
});
const text = textarea.value;
const hozon = document.querySelector('.hozon');
if (text === '') {
    hozon.disabled = true;
}
else {
    hozon.disabled = false;
};