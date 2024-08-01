

eel.expose(updateImageSrc);
function updateImageSrc(data) {
    let elem = document.getElementById('video');

    elem.src = "data:image/jpeg;base64," + data
}

function snapshot() {
    let date = Date.now();
    let filename = date.toString() + '.png';

    console.log(filename);

    eel.take_snapshot(filename);
}
