document.getElementById('origin-display').textContent = document.origin;

document.getElementById('notes').addEventListener('submit', function (e) {
	e.preventDefault();
	window.localStorage.setItem('message', e.target.body.value);
});

document.getElementById('notes').body.value = window.localStorage.getItem('message') || '';
document.getElementById('notes').body.disabled = false;
document.getElementById('notes-submit').disabled = false;
document.getElementById('notes').body.focus();
