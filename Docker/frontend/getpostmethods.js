async function sendMessage() {
    var today = new Date();
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();  
    var hora = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var data_to_send = {}
    data_to_send["message"] = document.getElementById("sendArea").value;
    data_to_send["date"] = date+" | "+hora;
    await fetch('http://127.0.0.1:8000/messages/', {
    method:"POST",
    headers: {
        'Origin': '*',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        
    },
    body:JSON.stringify(data_to_send)
    })

    .then(resp => resp.json())
    .then(data => {
        document.getElementById("sendArea").value = "Your message was successfully sent";
    })
    .catch(error => console.log(error))
}


async function getMessage() {
    await fetch('http://127.0.0.1:8000/messages/', {
    method:"GET"     
    })
    .then(resp => resp.json())
    .then(data => {
        document.getElementById("getArea").value = JSON.stringify(data);
    })
    .catch(error => console.log(error))
}