var socket


socket = io.connect(window.location.protocol + '//' + document.domain + ':' + location.port + '/camera', {
    transports: ['websocket']
})

console.log(window.location.protocol + '//' + document.domain + ':' + location.port + '/camera')

socket.on('connect', () => {
    console.log("Attempting connection")
    socket.emit('connect')
})

socket.on('disconnect', () => {
    console.log('Disconnecting connection')
    socket.emit('disconnect')
})

socket.on('status', (response) => {
    console.log(response)
})


setInterval(function() {
    socket.emit('stream')
}, 100)

socket.on('input_image', function(image) {
    // set python streamed image as photo src
    console.log('js stream')
    photo.setAttribute('src', image);
})

// console.log("HOla")
// socket.emit('something')