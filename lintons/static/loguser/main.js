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
const acceptance = document.querySelector('.acceptance');
const loader = document.querySelector('.loader');
const content = document.querySelector('.cont');
const colapse = document.querySelector('.colapse');
const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]')

send.addEventListener('click', async function(event) {
    event.preventDefault();
    acceptance.style.display = 'flex';
    loader.style.display = 'grid';
    colapse.style.display = 'none';
    const h1_1 = document.createElement('p');

    const firstForm = document.querySelector('.first-form');
    const thirdForm = document.querySelector('.third-form');
    const pass1 = document.querySelector('input[name="passwrd"]');
    const pass2 = document.querySelector('input[name="confirm"]');
    const honey = document.querySelector('input[name="honey"]');
    if (pass1.value || pass2.value || (honey && honey.value)) {
        h1_1.innerHTML = 'Thank you very important!';
        loader.appendChild(h1_1);
        return;
    }
    const name = document.querySelector('input[name="customername"]')
    h1_1.innerHTML = `Beauty in progress! 💅✨`;
    loader.appendChild(h1_1);

    const formData = new FormData();

    const firstFormData = new FormData(firstForm);
    firstFormData.forEach((value, key) => {
        formData.append(key, value);
    });

    const thirdFormData = new FormData(thirdForm);
    thirdFormData.forEach((value, key) => {
        formData.append(key, value);
    });

    try{
        const response = await fetch('add/', {
            method: 'POST',
            body : formData,
            headers : {
                'X-CSRFToken' : csrf.value
            }
        })
    }

    catch (error) {
        console.log(error);
        alert('Unexpected error occured!. Please try again later.')
        return;
    }
    setTimeout(function(){
        loader.style.display = 'none';
        content.style.display = 'block';
        colapse.style.display = 'block';
    }, 5000);
});

/**
 * ##########
 * ###############
 * Acceptance Success 
 * ###############
 * ##########
 */
colapse.addEventListener('click', function(){
    acceptance.style.display = 'none';
})