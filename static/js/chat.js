const decodeHTML = function (html) {
    const txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
}

const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

const getFormatedDate = (sent) => {
    const sentDate = moment(sent)
    const currentDate = moment()
    let sentOn = ""
    const diffDays = currentDate.diff(sentDate, 'days');
    if (diffDays > 364) {
        return sentDate.format("DD-MM-YYYY")
    } else if (diffDays > 30) {
        return sentDate.format("DD-MMM")
    }
    return 'today ' + sentDate.format("HH:mm")
}

const setMessage = ({
    userFrom,
    userTo,
    message,
    sentOn
}) => {
    const fromName = userFrom == currUser.email_address ? 'You' : otherUser.username
    getFormatedDate(sentOn)
    const item = document.createElement('div');
    item.className = userFrom == currUser.email_address ? "bubble right" : "bubble left"
    item.innerHTML = `
            <div class="name">${fromName}</div>
            <div class="msg">${message}</div>
            <div class="sent_on">${getFormatedDate(sentOn)}</div>
        `;
    messages.appendChild(item);
}

const head = document.getElementById('head');
const form = document.getElementById('form');
const input = document.getElementById('input');
const messages = document.getElementById('messages');


const chatSetup = async () => {
    otherUser.username = `${otherUser.first_name} ${otherUser.middle_name} ${otherUser.last_name}`;
    currUser.username = `${currUser.first_name} ${currUser.middle_name} ${currUser.last_name}`;

    const chatHistory = await fetch(`/api/chathistory/${otherUser.email_address}`, {
        headers: {
            'Content-Type': 'application/json',
            'x-id-token': getCookie('x-id-token')
        }
    }).then(res => res.json())
    if (chatHistory && chatHistory.length) {
        chatHistory.forEach(msg => {
            setMessage({
                userFrom: msg.sender,
                userTo: msg.receiver,
                message: msg.message,
                sentOn: msg.sentOn
            })
        })
    }
    const socket = io('localhost:7777', {
        path: "/chats/",
        auth: {
            'x-id-token': getCookie('x-id-token')
        }
    })

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        if (input.value) {
            socket.emit("private message", {
                message: input.value,
                from: currUser.email_address,
                to: otherUser.email_address
            });
            setMessage({
                userFrom: currUser.email_address,
                userTo: otherUser.email_address,
                message: input.value,
                sentOn: new Date()
            })
            input.value = '';
        }
    })

    socket.on("private message", (msg) => {
        setMessage(msg)
        window.scrollTo(0, document.body.scrollHeight);
    });

    head.innerHTML = otherUser.username
}
