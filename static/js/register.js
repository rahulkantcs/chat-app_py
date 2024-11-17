const form = document.querySelector('form')
const first_name = document.querySelector('#first_name')
const last_name = document.querySelector('#last_name')
const middle_name = document.querySelector('#middle_name')
const email_address = document.querySelector('#email_address')
const phone_number = document.querySelector('#phone_number')
const password = document.querySelector('#password')
const password2 = document.querySelector('#confirm_password')
const display = document.querySelector('.error')
form.addEventListener('submit', async (e) => {
    e.preventDefault()
    display.textContent = ''
    if (password.value != password2.value) {
        display.textContent = 'Passwords does not match'
        return
    }
    const inputData = {
        first_name: first_name.value,
        last_name: last_name.value,
        middle_name: middle_name.value,
        email_address: email_address.value,
        phone_number: phone_number.value,
        password: password.value
    }
    try {
        console.log('inputData::', inputData)
        fetch('/user/create', {
            method: 'POST',
            body: JSON.stringify(inputData),
            headers: { 'Content-Type': 'application/json' }
        })
            .then(res => res.json())
            .then(data => {
                console.log('data:::', data.detail)
                if (!data || data.email_address !== inputData.email_address) {
                    return display.textContent = `${data.message}. ${data.error ? data.error : ''}`
                }
                window.location.href = '/users'
            }).catch(err => {
                console.log(err)
            })
    } catch (err) {
        console.log(err)
    }

})