const eye = document.querySelector('.eye-icon');
const password = document.querySelector('.pass_in');

eye.addEventListener('click', function() {
    if (eye.getAttribute('name') === 'eye-outline'){
        eye.setAttribute('name', 'eye-off-outline');
        password.setAttribute('type', 'text');
    } else {
        eye.setAttribute('name', 'eye-outline');
        password.setAttribute('type', 'password');
    }
})