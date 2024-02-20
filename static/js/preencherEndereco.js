async function buscaEndereco(cep) {
    const mensagemErro = document.getElementById('erro');
    mensagemErro.innerHTML = '';
    try {
        let consultaCEP = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        let consultaCEPConvertida = await consultaCEP.json();
        if (consultaCEPConvertida.erro) {
            throw Error('CEP não existente!');
        }
        let cidade = document.getElementById('cidade');
        let logradouro = document.getElementById('logradouro');
        let estado = document.getElementById('ufEndereco');
        let bairro = document.getElementById('bairro')

        cidade.value = consultaCEPConvertida.localidade;
        logradouro.value = consultaCEPConvertida.logradouro;
        estado.value = consultaCEPConvertida.uf;
        bairro.value = consultaCEPConvertida.bairro;
        console.log(consultaCEPConvertida);
        return consultaCEPConvertida;
    } catch (erro) {
        mensagemErro.innerHTML = `<p>CEP inválido. Tente Novamente! </p>`;
        console.log(erro);
    }
}

const cep = document.getElementById('cep');
cep.addEventListener('focusout', () => buscaEndereco(cep.value));