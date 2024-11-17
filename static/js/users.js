const ul = document.querySelector("ul")
const getUsers = () => {
    fetch("/api/getUsers")
    .then(res => res.json())
    .then( data => {
        data.map(mappedUser => {
            let li = `<li> 
                <a href='/chat/${mappedUser.email_address}'>
                <p class="name"> 
                ${mappedUser.first_name}
                ${mappedUser.middle_name}
                ${mappedUser.last_name}
                </p>
                </a>
                </li>`
            ul.innerHTML += li
        })
    })
}
getUsers()