/**
 * ##########
 * ###############
 * Password eye
 * ###############
 * ##########
 */
const pass_inputs = document.querySelectorAll('.password');

pass_inputs.forEach(pass_input => {
    const pass_in = pass_input.querySelector('.pass_in');
    const eye_icon = pass_input.querySelector('.eye-icon');
    eye_icon.addEventListener('click', function(){
        if (eye_icon.getAttribute('name') === 'eye-outline'){
            eye_icon.setAttribute('name', 'eye-off-outline');
            pass_in.setAttribute('type', 'text');
        } else {
            eye_icon.setAttribute('name', 'eye-outline');
            pass_in.setAttribute('type', 'password');
        }
    })
});

/**
 * ##########
 * ###############
 * 
 * ###############
 * ##########
 */

