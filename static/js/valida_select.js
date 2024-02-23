const btnCadastrar = document.getElementById('btnCadastrar')
const select = document.querySelectorAll('select')
function validaSelect() {
    if (select.values == '') {
        alert('Preencha todos os campos')
    }
}


btnCadastrar.addEventListener('submit', validaSelect)