function criaMascara(mascaraInput) {
    const maximoInput = document.getElementById(`${mascaraInput}`).maxLength;
    let valorInput = document.getElementById(`${mascaraInput}`).value;
    let valorSemPonto = document.getElementById(`${mascaraInput}`).value.replace(/([^0-9])+/g, "");
    const mascaras = {
        cpf: valorInput.replace(/[^\d]/g, "").replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4"),
        telefone: valorInput.replace(/[^\d]/g, "").replace(/^(\d{2})(\d{5})(\d{4})/, "($1) $2-$3"),
        cep: valorInput.replace(/[^\d]/g, "").replace(/(\d{5})(\d{3})/, "$1-$2"),
        rg: valorInput.replace(/[^\d]/g, ""),
        cnpj: valorInput.replace(/[^\d]/g, "").replace(/(\d{7})(\d{2})(\d{4})(\d{1})(\d{2})(\d{4})/, "$1-$2.$3.$4.$5.$6"),
    };

    valorInput.length === maximoInput ? document.getElementById(`${mascaraInput}`).value = mascaras[mascaraInput]
        : document.getElementById(`${mascaraInput}`).value = valorSemPonto;
};