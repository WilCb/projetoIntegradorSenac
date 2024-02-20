let nome = document.getElementById('nome')
let rg = document.getElementById('rg')
let cpf = document.getElementById('cpf')
let orgaoExpedidor = document.getElementById('orgaoExpedidor')
let sexo = document.getElementById('sexo')
let pai = document.getElementById('pai')
let mae = document.getElementById('mae')
let naturalidade = document.getElementById('naturalidade')
let ufRG = document.getElementById('estados')
let pais = document.getElementById('pais')
let cepFormulario = document.getElementById('cep')
let logradouro = document.getElementById('logradouro')
let numero = document.getElementById('numero')
let bairro = document.getElementById('bairro')
let cidade = document.getElementById('cidade')
let ufEndereco = document.getElementById('uf')
let telefone = document.getElementById('telefone')
let dataNascimento = document.getElementById('dataNascimento')
let estadoCivil = document.getElementById('estadoCivil')
let nomeConjuge = document.getElementById('nomeConjuge')
let profissao = document.getElementById('profissao')
let escolaridade = document.getElementById('escolaridade')
let dataDeBatismo = document.getElementById('dataDeBatismo')
let batismo = document.getElementById('batismo')
let rol = document.getElementById('rol')
let congregacao = document.getElementById('congregacao')
let funcao = document.getElementById('funcao')
let origem = document.getElementById('origem')
let situacao = document.getElementById('situacao')
let observacao = document.getElementById('observacao')

let btnCadastrar = document.getElementById('btnCadastrar')

nome.addEventListener('input', ativarBtn)
rg.addEventListener('input', ativarBtn)
cpf.addEventListener('input', ativarBtn)
orgaoExpedidor.addEventListener('input', ativarBtn)
sexo.addEventListener('input', ativarBtn)
pai.addEventListener('input', ativarBtn)
mae.addEventListener('input', ativarBtn)
naturalidade.addEventListener('input', ativarBtn)
ufRG.addEventListener('input', ativarBtn)
pais.addEventListener('input', ativarBtn)
cepFormulario.addEventListener('input', ativarBtn)
logradouro.addEventListener('input', ativarBtn)
numero.addEventListener('input', ativarBtn)
bairro.addEventListener('input', ativarBtn)
cidade.addEventListener('input', ativarBtn)
ufEndereco.addEventListener('input', ativarBtn)
telefone.addEventListener('input', ativarBtn)
dataNascimento.addEventListener('input', ativarBtn)
estadoCivil.addEventListener('input', ativarBtn)
nomeConjuge.addEventListener('input', ativarBtn)
profissao.addEventListener('input', ativarBtn)
escolaridade.addEventListener('input', ativarBtn)
dataDeBatismo.addEventListener('input', ativarBtn)
batismo.addEventListener('input', ativarBtn)
rol.addEventListener('input', ativarBtn)
congregacao.addEventListener('input', ativarBtn)
funcao.addEventListener('input', ativarBtn)
origem.addEventListener('input', ativarBtn)
situacao.addEventListener('input', ativarBtn)
observacao.addEventListener('input', ativarBtn)


function ativarBtn() {
    // Se o valor do input não estiver vazio
    if (nome.value.trim() !== '' &&
        rg.value.trim() !== '' &&
        cpf.value.trim() !== '' &&
        orgaoExpedidor.value.trim() !== '' &&
        sexo.value.trim() !== '' &&
        pai.value.trim() !== '' &&
        mae.value.trim() !== '' &&
        naturalidade.value.trim() !== '' &&
        ufRG.value.trim() !== '' &&
        pais.value.trim() !== '' &&
        cepFormulario.value.trim() !== '' &&
        logradouro.value.trim() !== '' &&
        numero.value.trim() !== '' &&
        bairro.value.trim() !== '' &&
        cidade.value.trim() !== '' &&
        ufEndereco.value.trim() !== '' &&
        telefone.value.trim() !== '' &&
        dataNascimento.value.trim() !== '' &&
        estadoCivil.value.trim() !== '' &&
        nomeConjuge.value.trim() !== '' &&
        profissao.value.trim() !== '' &&
        escolaridade.value.trim() !== '' &&
        dataDeBatismo.value.trim() !== '' &&
        batismo.value.trim() !== '' &&
        rol.value.trim() !== '' &&
        congregacao.value.trim() !== '' &&
        funcao.value.trim() !== '' &&
        origem.value.trim() !== '' &&
        situacao.value.trim() !== '' &&
        observacao.value.trim() !== '') {
        // Remove o atributo "disabled" do botão
        btnCadastrar.removeAttribute("disabled");
    } else {
        // Adiciona o atributo "disabled" ao botão
        btnCadastrar.setAttribute("disabled", "disabled");
    }
}

