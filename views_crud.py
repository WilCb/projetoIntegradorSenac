from flask import session, url_for, render_template, request, redirect, flash
from app import app, db
from helpers import FormularioCadastro, BuscarMembro
from models import Cadastro

@app.route('/formulario-de-cadastro')
def formulario_de_cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    form = FormularioCadastro()
    return render_template('formulario.html', form=form)

@app.route('/cadastrar-no-banco', methods=['POST',])
def cadastrar_no_banco():
    form = FormularioCadastro(request.form)

    if not form.validate_on_submit():
        nome=form.nome.data
        rg=form.rg.data
        cpf=form.cpf.data
        orgao_expedidor=form.orgao_expedidor.data
        sexo=form.sexo.data
        pai=form.pai.data
        mae=form.mae.data
        naturalidade=form.naturalidade.data
        uf_identidade=form.ufIdentidade.data
        pais=form.pais.data
        cep=form.cep.data
        logradouro=form.logradouro.data
        numero=form.numero.data
        complemento=form.complemento.data
        bairro=form.bairro.data
        cidade=form.cidade.data
        uf_endereco=form.ufEndereco.data
        telefone=form.telefone.data
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

        return redirect(url_for('cadastrado'))

    return redirect(url_for('erro_no_cadastro'))

@app.route('/cadastrado')
def cadastrado():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    return render_template('erros/confirmacao_de_cadastro.html')
    
@app.route('/lista-de-membros')
def lista_de_membros():
    lista = Cadastro.query.order_by(Cadastro.cpf)
    
    return render_template('listar_membros.html', membros=lista)

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    Cadastro.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('lista_de_membros'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    membro = Cadastro.query.filter_by(id=id).first()
    form = FormularioCadastro()
    form.nome.data = membro.nome
    form.rg.data = membro.rg
    form.cpf.data = membro.cpf
    form.orgao_expedidor.data = membro.orgao_expedidor
    form.sexo.data = membro.sexo
    form.pai.data = membro.pai
    form.mae.data = membro.mae
    form.naturalidade.data = membro.naturalidade
    form.ufIdentidade.data = membro.uf_identidade
    form.pais.data = membro.pais
    form.cep.data = membro.cep
    form.logradouro.data = membro.logradouro
    form.numero.data = membro.numero
    form.complemento.data = membro.complemento
    form.bairro.data = membro.bairro
    form.cidade.data = membro.cidade
    form.ufEndereco.data = membro.uf_endereco
    form.telefone.data = membro.telefone
    form.dataNascimento.data = membro.data_nascimento
    form.estadoCivil.data = membro.estado_civil
    form.nomeConjuge.data = membro.nome_conjuge
    form.profissao.data = membro.profissao
    form.escolaridade.data = membro.escolaridade
    form.dataDeBatismo.data = membro.data_batismo
    form.batizado.data = membro.batizado_esp_santo
    form.entradaRol.data = membro.entrada_rol_membros
    form.congregacao.data = membro.congregacao
    form.funcao.data = membro.funcao
    form.origem.data = membro.origem
    form.situacao.data = membro.situacao
    form.observacao.data = membro.igreja_cidade

    return render_template('editar.html', id=id, form=form)

@app.route('/atualizar-membro', methods=['POST',])
def atualizar_membro():
    form = FormularioCadastro(request.form)
    if form.validate_on_submit():
        membro = Cadastro.query.filter_by(id=request.form['id']).first()
        membro.nome = form.nome.data
        membro.rg = form.rg.data
        membro.cpf = form.cpf.data
        membro.orgao_expedidor = form.orgao_expedidor.data
        membro.sexo = form.sexo.data
        membro.pai = form.pai.data
        membro.mae = form.mae.data
        membro.naturalidade = form.naturalidade.data
        membro.uf_identidade = form.ufIdentidade.data
        membro.pais = form.pais.data
        membro.cep = form.cep.data
        membro.logradouro = form.logradouro.data
        membro.numero = form.numero.data
        membro.complemento = form.complemento.data
        membro.bairro = form.bairro.data
        membro.cidade = form.cidade.data
        membro.uf_endereco = form.ufEndereco.data
        membro.telefone = form.telefone.data
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
    form = BuscarMembro()
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))   
    lista = Cadastro.query.order_by(Cadastro.cpf)
    return render_template('consultar_membro.html', form=form)