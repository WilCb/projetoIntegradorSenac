let nome = document.getElementById('nome')
let rg = document.getElementById('rg')
let btnProximo = document.getElementById('btnProximo')

nome.addEventListener('input', ativarBtn)
rg.addEventListener('input', ativarBtn)

function ativarBtn() {
    // Se o valor do input não estiver vazio
    if (nome.value.trim() !== '' && rg.value.trim() !== '') {
        // Remove o atributo "disabled" do botão
        btnProximo.removeAttribute("disabled");
    } else {
        // Adiciona o atributo "disabled" ao botão
        btnProximo.setAttribute("disabled", "disabled");
    }
}

