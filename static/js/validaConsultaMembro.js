let cpf = document.getElementById('buscaPorCpf')
const btn = document.getElementById('buscarCpf')

cpf.addEventListener('input', ativarBtn)

function ativarBtn() {
    // Se o valor do input não estiver vazio
    if (cpf.value.trim() !== '') {
        // Remove o atributo "disabled" do botão
        btn.removeAttribute("disabled");
    } else {
        // Adiciona o atributo "disabled" ao botão
        btn.setAttribute("disabled", "disabled");
    }
}
