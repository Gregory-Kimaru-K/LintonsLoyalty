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
 * UX And Form Submission
 * ###############
 * ##########
 */

const forms = document.querySelectorAll('form');
const firstForm = document.querySelector('.first-form');
const thirdForm = document.querySelector('.third-form');
const colapse = document.querySelector('.colapse');
const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]');
const acceptance = document.querySelector('.acceptance');
const content = document.querySelector('.cont');
const loader = document.querySelector('.loader');

forms.forEach((form, index) => {
    const enter = form.querySelector('.enter');
    const back = form.querySelector('.back');

    enter.addEventListener('click', async function(event){
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

        if (valid && index == 1) {
            content.innerHTML = '';
            content.style.display = 'none';
            const pass1 = document.querySelector('input[name="passwrd"]');
            const pass2 = document.querySelector('input[name="confirm"]');
            const honey = document.querySelector('input[name="honey"]');
            if (pass1.value || pass2.value || (honey && honey.value)) {
                console.log('Thanks')
                return;
            }

            acceptance.style.display = 'flex';
            loader.style.display = 'grid';
            colapse.style.display = 'none';
            const formData = new FormData();
            const firstFormData = new FormData(firstForm);
            const thirdFormData = new FormData(thirdForm);
            firstFormData.forEach((value, key) => {
                formData.append(key, value);
            })

            thirdFormData.forEach((value, key) => {
                formData.append(key, value);
            })

            try{
                const response = await fetch('add/', {
                    method: 'POST',
                    body : formData,
                    headers : {
                        'X-CSRFToken' : csrf.value
                    }
                })
                if (!response.ok) {
                    const icon = document.createElement('ion-icon');
                    const span_suc = document.createElement('span');
                    const p = document.createElement('p');
                    icon.classList.add('bad');
                    icon.setAttribute('name', 'close-circle');
                    span_suc.classList.add('success');
                    span_suc.innerHTML = 'Failed';
                    p.innerHTML = 'Network Response Not okay!';
                    content.appendChild(icon);
                    content.appendChild(span_suc);
                    content.appendChild(p);
                }
        
                const data = await response.json()
                if (data.success == 'False'){
                    const icon = document.createElement('ion-icon');
                    const span_suc = document.createElement('span');
                    const p = document.createElement('p');
                    icon.classList.add('bad');
                    icon.setAttribute('name', 'close-circle');
                    span_suc.classList.add('success');
                    span_suc.innerHTML = 'Failed';
                    p.innerHTML = data.msg;
                    content.appendChild(icon);
                    content.appendChild(span_suc);
                    content.appendChild(p);
                }
                else if (data.success == 'True'){
                    const icon = document.createElement('ion-icon');
                    const span_suc = document.createElement('span');
                    const p = document.createElement('p');
                    const finputs = firstForm.querySelectorAll('input');
                    const tinputs = thirdForm.querySelectorAll('input');
                    icon.classList.add('good');
                    icon.setAttribute('name', 'checkmark-circle');
                    span_suc.classList.add('success');
                    span_suc.innerHTML = 'Success';
                    p.innerHTML = data.msg;
                    content.appendChild(icon);
                    content.appendChild(span_suc);
                    content.appendChild(p);
                    finputs.forEach(finput => {
                        finput.value = '';
                    })
                    tinputs.forEach(tinput => {
                        if (tinput.type !== 'radio'){
                            tinput.value = '';
                        }
                        else{
                            tinput.checked = false;
                        }
                    })

                }
            }
        
            catch (error) {
                console.log(error);
                const icon = document.createElement('ion-icon');
                const span_suc = document.createElement('span');
                const p = document.createElement('p');
                icon.classList.add('bad');
                icon.setAttribute('name', 'close-circle');
                span_suc.classList.add('success');
                span_suc.innerHTML = 'Failed';
                p.innerHTML ='Unexpected error occured!. Please try again later.';
                content.appendChild(icon);
                content.appendChild(span_suc);
                content.appendChild(p);
                return;
            }
            setTimeout(function(){
                loader.style.display = 'none';
                content.style.display = 'block';
                colapse.style.display = 'block';
            }, 3000);
        }
        
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
 * Acceptance Success 
 * ###############
 * ##########
 */
colapse.addEventListener('click', function(){
    acceptance.style.display = 'none';
    firstForm.style.display = 'flex';    
    thirdForm.style.display = 'none';
})