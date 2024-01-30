let chk = document.getElementById('chk')
chk.addEventListener('click', function () {
    let input = document.getElementById('pwd')
    if (input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text')
    } else {
        input.setAttribute('type', 'password')
    }
})