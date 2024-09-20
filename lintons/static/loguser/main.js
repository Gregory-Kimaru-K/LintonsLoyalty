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
 * UX and Form Submission 
 * ###############
 * ##########
 */

const forms = document.querySelectorAll('form');

forms.forEach(form => {
    const enter = form.querySelector('.enter');
    const back = form.querySelector('.back');

    enter.addEventListener('click', function(event){
        event.preventDefault();
        const inputs = form.querySelectorAll('input[required]');
        let valid = true;

        inputs.forEach(input => {
            if (!input.checkValidity()) {  // Use built-in validity check
                valid = false;
                if (input.validity.typeMismatch) {
                    alert(`The value for ${input.name} is not a valid ${input.type}`);
                } else if (input.validity.valueMissing) {
                    alert(`Please fill the ${input.name} field`);
                } else if (input.validity.patternMismatch) {
                    alert(`The value for ${input.name} does not match the expected pattern`);
                }
            }
        });

        if (valid) {
            // Proceed to next form or save data
            form.style.display = 'none';
            const nextForm = form.nextElementSibling;
            if (nextForm) {
                nextForm.style.display = 'flex';
            }
        }
    });

    if (back) {
        back.addEventListener('click', function(event){
            event.preventDefault();
            form.style.display = 'none';
            const previousForm = form.previousElementSibling;
            if (previousForm) {
                previousForm.style.display = 'flex';
            }
        });
    }
});

// Initially hide all forms except the first one
forms.forEach((form, index) => {
    if (index !== 0) {
        form.style.display = 'none';
    }
});
