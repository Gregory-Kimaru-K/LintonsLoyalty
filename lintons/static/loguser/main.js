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
 * UX
 * ###############
 * ##########
 */

const forms = document.querySelectorAll('form');

forms.forEach((form, index) => {
    const enter = form.querySelector('.enter');
    const back = form.querySelector('.back');

    enter.addEventListener('click', function(event){
        event.preventDefault();
        const inputs = form.querySelectorAll('input[required]');
        let valid = true;

        inputs.forEach(input => {
            const inbox = input.parentElement;
            const feedrongs = inbox.querySelectorAll('.feedrong');
            feedrongs.forEach(feedrong => feedrong.remove());
            if (!input.checkValidity()) {
                valid = false;
                if (input.validity.typeMismatch) {
                    const feedback = document.createElement('p');
                    feedback.classList.add('feedrong');
                    const msg = `This value is not a valid ${input.type}`
                    feedback.innerHTML = msg;
                    inbox.appendChild(feedback);
                } else if (input.validity.valueMissing) {
                    const feedback = document.createElement('p');
                    feedback.classList.add('feedrong');
                    const msg = `Please fill this field`
                    feedback.innerHTML = msg;
                    inbox.appendChild(feedback);
                } else if (input.validity.patternMismatch) {
                    const feedback = document.createElement('p');
                    feedback.classList.add('feedrong');
                    const msg = `This value does not match the expected pattern`
                    feedback.innerHTML = msg;
                    inbox.appendChild(feedback);
                }
            }
        });
        
        // if (index === 1) {
        //     const confirm = document.querySelector('.confirm');
        //     const passwrd = document.querySelector('.passent');
        //     const pass1 = passwrd.querySelector('.pass_in');
        //     const pass2 = confirm.querySelector('.pass_in');
        //     if (pass1.value != pass2.value) {
        //         valid = false;
        //         const feedback = document.createElement('p');
        //         const feedback1 = document.createElement('p');
        //         feedback.classList.add('feedrong');
        //         feedback1.classList.add('feedrong');
        //         const msg = 'Must be the same';
        //         feedback.innerHTML = msg;
        //         feedback1.innerHTML =msg;
        //         confirm.appendChild(feedback);
        //         passwrd.appendChild(feedback1);
        //     }
        // }
        
        if (valid) {
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

forms.forEach((form, index) => {
    if (index !== 0) {
        form.style.display = 'none';
    }
});

/**
 * ##########
 * ###############
 * Form Submission 
 * ###############
 * ##########
 */

const send = document.querySelector('.save');

send.addEventListener('click', function(event) {
    event.preventDefault();
    
    const firstForm = document.querySelector('.first-form');
    const thirdForm = document.querySelector('.third-form');

    const formData = new FormData();

    const firstFormData = new FormData(firstForm);
    firstFormData.forEach((value, key) => {
        formData.append(key, value);
    });

    const thirdFormData = new FormData(thirdForm);
    thirdFormData.forEach((value, key) => {
        formData.append(key, value);
    });

    console.log(formData)
    for (let [key, value] of formData.entries()) {
        console.log(`${key}, ${value}`);
    }
})