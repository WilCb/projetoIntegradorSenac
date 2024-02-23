from flask import session, url_for, render_template, request, redirect, flash
from app import app, db
from helpers import FormularioCadastro
from models import Cadastro

@app.route('/formulario-de-cadastro')
def formulario_de_cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    form = FormularioCadastro()
    return render_template('formulario.html', form=form, titulo='SIGM - CADASTRO')

@app.route('/cadastrar-no-banco', methods=['POST',])
def cadastrar_no_banco():
    form = FormularioCadastro(request.form)

    if not form.validate_on_submit():
        nome=form.nome.data
        rg=form.rg.data
        cpf=form.cpf.data.replace('.', '').replace('-', '')
        orgao_expedidor=form.orgao_expedidor.data
        sexo=form.sexo.data
        pai=form.pai.data
        mae=form.mae.data
        naturalidade=form.naturalidade.data
        uf_identidade=form.ufIdentidade.data
        pais=form.pais.data
        cep=form.cep.data.replace('-', '')
        logradouro=form.logradouro.data
        numero=form.numero.data
        complemento=form.complemento.data
        bairro=form.bairro.data
        cidade=form.cidade.data
        uf_endereco=form.ufEndereco.data
        telefone=form.telefone.data.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        data_nascimento=form.dataNascimento.data
        estado_civil=form.estadoCivil.data
        nome_conjuge=form.nomeConjuge.data
        profissao=form.profissao.data
        escolaridade=form.escolaridade.data
        data_batismo=form.dataDeBatismo.data
        batizado_esp_santo=form.batizado.data
        entrada_rol_membros=form.entradaRol.data
        congregacao=form.congregacao.data
        funcao=form.funcao.data
        origem=form.origem.data
        situacao=form.situacao.data
        igreja_cidade=form.observacao.data

        membro = Cadastro.query.filter_by(cpf=cpf).first()

        if membro:
            flash('CPF já existe no banco!')
            return redirect(url_for('index'))
        
        novo_membro = Cadastro(
            nome=nome,
            rg=rg,
            cpf=cpf,
            orgao_expedidor=orgao_expedidor,
            sexo=sexo,
            pai=pai,
            mae=mae,
            naturalidade=naturalidade,
            uf_identidade=uf_identidade,
            pais=pais,
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            uf_endereco=uf_endereco,
            telefone=telefone,
            data_nascimento=data_nascimento,
            estado_civil=estado_civil,
            nome_conjuge=nome_conjuge,
            profissao=profissao,
            escolaridade=escolaridade,
            data_batismo=data_batismo,
            batizado_esp_santo=batizado_esp_santo,
            entrada_rol_membros=entrada_rol_membros,
            congregacao=congregacao,
            funcao=funcao,
            origem=origem,
            situacao=situacao,
            igreja_cidade=igreja_cidade
        )

        db.session.add(novo_membro)
        db.session.commit()
        
        flash('Cadastrado realizado')
        return redirect(url_for('lista_de_membros'))

    return redirect(url_for('erro_no_cadastro'))

@app.route('/cadastrado')
def cadastrado():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    return render_template('erros/confirmacao_de_cadastro.html', titulo='SIGM - CADASTRADO')
    
@app.route('/lista-de-membros')
def lista_de_membros():
    lista = Cadastro.query.order_by(Cadastro.cpf)
    return render_template('listar_membros.html', membros=lista, titulo='SIGM - LISTA')

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('lista_de_membros')))
    Cadastro.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('lista_de_membros'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    membro = Cadastro.query.filter_by(id=id).first()
    form = FormularioCadastro()
    form.nome.data = membro.nome.strip()
    form.rg.data = membro.rg
    if membro.cpf:
            cpf_str = str(membro.cpf)
            cpf_formatado = f'{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}'
            form.cpf.data = cpf_formatado
    form.orgao_expedidor.data = membro.orgao_expedidor.strip()
    form.sexo.data = membro.sexo
    form.pai.data = membro.pai.strip()
    form.mae.data = membro.mae.strip()
    form.naturalidade.data = membro.naturalidade.strip()
    form.ufIdentidade.data = membro.uf_identidade
    form.pais.data = membro.pais.strip()
    if membro.cep:
            cep_str = str(membro.cep)
            cep_formatado = f'{cep_str[:5]}-{cep_str[5:]}'
            form.cep.data = cep_formatado
    form.logradouro.data = membro.logradouro.strip()
    form.numero.data = membro.numero
    form.complemento.data = membro.complemento.strip()
    form.bairro.data = membro.bairro.strip()
    form.cidade.data = membro.cidade.strip()
    form.ufEndereco.data = membro.uf_endereco
    if membro.telefone:
            tel_str = str(membro.telefone)
            tel_formatado = f'({tel_str[:2]}) {tel_str[2:7]}-{tel_str[7:]}'
            form.telefone.data = tel_formatado
    form.dataNascimento.data = membro.data_nascimento
    form.estadoCivil.data = membro.estado_civil
    form.nomeConjuge.data = membro.nome_conjuge.strip()
    form.profissao.data = membro.profissao.strip()
    form.escolaridade.data = membro.escolaridade
    form.dataDeBatismo.data = membro.data_batismo
    form.batizado.data = membro.batizado_esp_santo
    form.entradaRol.data = membro.entrada_rol_membros
    form.congregacao.data = membro.congregacao
    form.funcao.data = membro.funcao
    form.origem.data = membro.origem
    form.situacao.data = membro.situacao
    form.observacao.data = membro.igreja_cidade
    return render_template('editar.html', id=id, form=form, titulo='SIGM - EDITAR')

@app.route('/atualizar-membro', methods=['POST',])
def atualizar_membro():
    form = FormularioCadastro(request.form)
    membro = Cadastro.query.filter_by(id=request.form['id']).first()
    membro.nome = form.nome.data
    membro.rg = form.rg.data
    membro.cpf = form.cpf.data.replace('.', '').replace('-', '')
    membro.orgao_expedidor = form.orgao_expedidor.data
    membro.sexo = form.sexo.data
    membro.pai = form.pai.data
    membro.mae = form.mae.data
    membro.naturalidade = form.naturalidade.data
    membro.uf_identidade = form.ufIdentidade.data
    membro.pais = form.pais.data
    membro.cep = form.cep.data.replace('-', '')
    membro.logradouro = form.logradouro.data
    membro.numero = form.numero.data
    membro.complemento = form.complemento.data
    membro.bairro = form.bairro.data
    membro.cidade = form.cidade.data
    membro.uf_endereco = form.ufEndereco.data
    membro.telefone = form.telefone.data.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    membro.data_nascimento = form.dataNascimento.data
    membro.estado_civil = form.estadoCivil.data
    membro.nome_conjuge = form.nomeConjuge.data
    membro.profissao = form.profissao.data
    membro.escolaridade = form.escolaridade.data
    membro.data_batismo = form.dataDeBatismo.data
    membro.batizado_esp_santo = form.batizado.data
    membro.entrada_rol_membros = form.entradaRol.data
    membro.congregacao = form.congregacao.data
    membro.funcao = form.funcao.data
    membro.origem = form.origem.data
    membro.situacao = form.situacao.data
    membro.igreja_cidade = form.observacao.data

    db.session.add(membro)
    db.session.commit()

    return redirect(url_for('lista_de_membros'))


@app.route('/consultar-membro')
def consultar_membro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    form = FormularioCadastro()
    return render_template('consultar_membro.html', form=form, titulo='SIGM - CONSULTA')

@app.route("/receber_dados", methods=['POST',])
def receber_dados():
    try:
        form = FormularioCadastro(request.form)
        membro = Cadastro.query.filter_by(cpf=request.form['cpf'].replace('.', '').replace('-', '')).first()
        form.nome.data = membro.nome
        form.rg.data = membro.rg

        if membro.cpf:
            cpf_str = str(membro.cpf)
            cpf_formatado = f'{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}'
            form.cpf.data = cpf_formatado

        form.orgao_expedidor.data = membro.orgao_expedidor.strip()
        form.sexo.data = membro.sexo
        form.pai.data = membro.pai.strip()
        form.mae.data = membro.mae.strip()
        form.naturalidade.data = membro.naturalidade.strip()
        form.ufIdentidade.data = membro.uf_identidade
        form.pais.data = membro.pais.strip()

        if membro.cep:
            cep_str = str(membro.cep)
            cep_formatado = f'{cep_str[:5]}-{cep_str[5:]}'
            form.cep.data = cep_formatado

        form.logradouro.data = membro.logradouro.strip()
        form.numero.data = membro.numero
        form.complemento.data = membro.complemento.strip()
        form.bairro.data = membro.bairro.strip()
        form.cidade.data = membro.cidade.strip()
        form.ufEndereco.data = membro.uf_endereco

        if membro.telefone:
            tel_str = str(membro.telefone)
            tel_formatado = f'({tel_str[:2]}) {tel_str[2:7]}-{tel_str[7:]}'
            form.telefone.data = tel_formatado

        form.dataNascimento.data = membro.data_nascimento.strftime('%d/%m/%Y')
        form.estadoCivil.data = membro.estado_civil
        form.nomeConjuge.data = membro.nome_conjuge.strip()
        form.profissao.data = membro.profissao.strip()
        form.escolaridade.data = membro.escolaridade
        if membro.data_batismo:
            form.dataDeBatismo.data = membro.data_batismo.strftime('%d/%m/%Y')
        form.batizado.data = membro.batizado_esp_santo
        if membro.entrada_rol_membros:
            form.entradaRol.data = membro.entrada_rol_membros.strftime('%d/%m/%Y')
        form.congregacao.data = membro.congregacao
        form.funcao.data = membro.funcao
        form.origem.data = membro.origem
        form.situacao.data = membro.situacao
        form.observacao.data = membro.igreja_cidade

        return render_template('consultar_membro.html', form=form, titulo='SIGM - CONSULTA')
    except AttributeError:
        flash(f'CPF Inválido ou não cadastrado ! ')
        return redirect(url_for('consultar_membro'))