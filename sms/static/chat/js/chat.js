

let url = `ws://${window.location.host}/ws/socket-server/`

let userID = document.getElementById('userID')
let myID = document.getElementById('myID')
let message = document.getElementById('message')

const chatSocket = new WebSocket(url)

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    console.log('Data', data)
    console.log('MyID', myID.textContent)

    if (data.userID === myID.textContent){
        if(data.type === 'chat'){
            let  messages = document.getElementById('messages')

            messages.insertAdjacentHTML('beforeend', `<div>
                                        <p>${data.message}</p>
                                        </div>`)
        }
    }
}

function myFunction() {
  chatSocket.send(JSON.stringify({
        'message': message.value,
        'userID': userID.value,
    }))
}