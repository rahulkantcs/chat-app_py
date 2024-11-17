const form = document.querySelector('form')
const email_address = document.querySelector('#email_address')
const password = document.querySelector('#password')
const display = document.querySelector('.error')
form.addEventListener('submit', async (e) => {
    e.preventDefault()
    display.textContent = ''
    try {
        const inputData = { email_address: email_address.value, password: password.value }
        await fetch('/user/login', {
            method: 'POST',
            body: JSON.stringify(inputData),
            headers: { 'Content-Type': 'application/json' }
        })
            .then(res => {
                return res.json()
            })
            .then(data => {
                if (!data || data.detail) {
                    return display.textContent = `${data.detail}. ${data.error ? data.error : ''}`
                }
                window.location.href = '/users'
            }).catch(err => console.log('err:::', err))

    } catch (err) {
        console.log('1', err)
    }
})