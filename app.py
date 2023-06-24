from flask import *
from xhtml2pdf import pisa
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return pdf(request.form["nomea"], request.form["nomeb"], request.form["natua"], request.form["natub"], request.form["profia"], request.form["profib"], request.form["identa"], request.form["identb"], request.form["orga"], request.form["orgb"], request.form["dataa"], request.form["datab"], request.form["cpfa"], request.form["cpfb"], request.form["enda"], request.form["endb"], request.form["cidadea"], request.form["cidadeb"], request.form["estadoa"], request.form["estadob"])
    
    return render_template("contract.html")

@app.route("/pdf", methods=["GET"])
def pdf(nomea, nomeb, natua, natub, profia, profib, identa, identb, orga, orgb, dataa, datab, cpfa, cpfb, enda, endb, cidadea, cidadeb, estadoa, estadob):
   
    html = """
    
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=windows-1252"/>
	<title></title>
	<meta name="generator" content="LibreOffice 7.1.0.3 (Windows)"/>
	<meta name="author" content="Jorge Leopoldo Sobb&eacute;"/>
	<meta name="created" content="2022-11-29T22:10:00"/>
	<meta name="changedby" content="Jorge Leopoldo Sobb&eacute;"/>
	<meta name="changed" content="2023-03-29T17:46:00"/>
	<meta name="AppVersion" content="16.0000"/>
	<meta name="ContentTypeId" content="0x010100A9E10A494B0C914CBF6ED168A706A486"/>
	<meta name="DocSecurity" content="4"/>
	<style type="text/css">
		@page { size: 21cm 29.7cm; margin-left: 3cm; margin-right: 3cm; margin-top: 2.5cm; margin-bottom: 2.5cm }
		p { margin-bottom: 0.25cm; direction: ltr; line-height: 115%; text-align: left; orphans: 2; widows: 2; background: transparent }
	</style>
</head>
<body lang="pt-BR" link="#000080" vlink="#800000" dir="ltr"><p align="center" style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>Contrato
de Namoro</b></font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">A
e B,  abaixo qualificados, cientes e compromissados passam a expor as
regras e limites de sua conviv&ecirc;ncia: </font></font>
</p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">Qualifica&ccedil;&atilde;o
de ambas as partes:</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">A)
(nome completo a), (naturalidade a), (profissao a), Carteira de
Identidade (identidade a), expedida por (orgao a), na
data de (data a), CPF n&ordm; (cpf a),
residente e domiciliado na (endereco a), na cidade de (cidade a), no estado (estado a).</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">B)
(nome completo b), (naturalidade b), (profissao b), Carteira de
Identidade (identidate b), expedida por (orgao b), na
data de (data b), CPF n&ordm; (cpf b),
residente e domiciliado na (endereco b), na cidade de (cidade b), no estado (estado b).</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<br/>
<br/>

</p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>Cl&aacute;usulas:</b></font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>Primeira:</b></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
As partes deste contrato declaram que possuem um relacionamento
amoroso, afetivo e firmam conceito como sendo um namoro.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
primeiro:</u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
O termo inicial deste namoro se dar&aacute; na assinatura deste
contrato, sendo vedada a assinatura retroativa.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>Segunda:</b></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
As partes declaram n&atilde;o possuir qualquer pretens&atilde;o de
constitu&iacute;rem fam&iacute;lia, ou qualquer v&iacute;nculo
matrimonial.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
primeiro:</u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
Para haver modifica&ccedil;&atilde;o dos termos deste contrato de
namoro &eacute; necess&aacute;rio um aditivo contendo o fim do
relacionamento; ou uma escritura p&uacute;blica de Uni&atilde;o
Est&aacute;vel; ou certid&atilde;o de casamento.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
segundo:</u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
O termo final deste contrato ser&aacute; formal, sendo irrevog&aacute;vel
esta decis&atilde;o, que coincidir&aacute; com o termo final da
rela&ccedil;&atilde;o de namoro.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
terceiro:</u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
 Ocorrendo qualquer das hip&oacute;teses o contrato estar&aacute;
extinto.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
quarto</u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>:</b></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
As partes deste contrato (n&atilde;o) prometem fidelidade.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
quinto</u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
:  As partes deste contrato declaram serem independentes
economicamente uma da outra, n&atilde;o havendo qualquer v&iacute;nculo
patrimonial, al&eacute;m de residirem em endere&ccedil;os distintos.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
sexto : </u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">Em
momentos de coabita&ccedil;&atilde;o, pernoite na mesma resid&ecirc;ncia,
viagens, e demais eventos sociais, a condi&ccedil;&atilde;o do
relacionamento n&atilde;o se altera por conta de hip&oacute;tese n&atilde;o
descrita formalmente.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u>Par&aacute;grafo
s&eacute;timo:</u></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
Qualquer postagem disponibilizada  por qualquer das partes ou por
terceiros, em redes sociais ou similares, n&atilde;o altera e n&atilde;o
extingue este contrato de namoro.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>Terceiro:</b></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
Em caso de t&eacute;rmino do namoro, os presentes havidos durante o
per&iacute;odo da vig&ecirc;ncia deste contrato ser&atilde;o
decididos livremente.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>Quarto:</b></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
Em caso de &oacute;bito de qualquer das partes, n&atilde;o ascender&aacute;
ao sobrevivente qualquer direito sobre bens e valores.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><b>Quinto:</b></font></font><font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">
As partes declaram ainda que t&ecirc;m plena ci&ecirc;ncia e
integral, produzindo efeito tamb&eacute;m perante terceiros
conhecimento de todos os termos, efic&aacute;cia e amplitude do
presente contrato, deliberando qualquer  altera&ccedil;&atilde;o,
modifica&ccedil;&atilde;o ou acr&eacute;scimo somente produzir&aacute;
efeitos atrav&eacute;s de outro contrato em que ambos dever&atilde;o
comparecer obrigatoriamente para a formaliza&ccedil;&atilde;o do ato.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt"><u><b>Condi&ccedil;&otilde;es
gerais: </b></u></font></font>
</p>
<ol>
	<li><p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
	<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">Qualquer
	aditamento e altera&ccedil;&atilde;o do presente instrumento dever&aacute;
	ser feita por escrito e assinado pelas partes da mesma forma que o
	presente contrato.</font></font></p>
	<li><p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
	<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">As
	partes declaram que foram devidamente alertadas sobre as
	consequ&ecirc;ncias da responsabilidade civil e pena da lavratura
	deste ato, por todas as declara&ccedil;&otilde;es por elas
	prestadas.</font></font></p>
	<li><p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
	<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">As
	partes declaram que todos os dados que sozinhas inseriram neste
	contrato s&atilde;o verdadeiros e conferem com os documentos de
	identifica&ccedil;&atilde;o de cada uma, visto que estes n&atilde;o
	s&atilde;o verificados por terceira pessoa ou por sistema digital.</font></font></p>
</ol>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">E,
assim justos e contratados firmam a presente escritura como
reprodu&ccedil;&atilde;o fiel da verdade e de boa-f&eacute;, aceitam,
ratificam e assinam.</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">As
partes elegem o foro da comarca de qualquer das partes para dirimir
eventuais d&uacute;vidas sobre o presente contrato de namoro</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<br/>
<br/>

</p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">Porto Alegre, dia 12 de março de 2023</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<br/>
<br/>

</p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<br/>
<br/>

</p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">____________________________________</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">A</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<br/>
<br/>

</p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<br/>
<br/>

</p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">______________________________________</font></font></p>
<p style="margin-top: 0.21cm; margin-bottom: 0.21cm; line-height: 150%">
<font face="Calibri Light, serif"><font size="3" style="font-size: 13pt">B</font></font></p>
<p style="margin-bottom: 0.28cm; line-height: 108%"><br/>
<br/>

</p>
<p style="margin-bottom: 0.28cm; line-height: 108%"><br/>
<br/>

</p>
<p style="margin-bottom: 0.28cm; line-height: 108%"><br/>
<br/>

</p>
</body>
</html>
    
    """.replace("(nome completo a)", nomea).replace("(nome completo b)", nomeb).replace("(naturalidade a)", natua).replace("(naturalidade b)", natub).replace("(profissao a)", profia).replace("(profissao b)", profib).replace("(identidade a)", identa) .replace("(identidade b)", identb).replace("(orgao a)", orga).replace("(orgao b)", orgb).replace("(data a)", dataa).replace("(data b)", datab).replace("(cpf a)", cpfa).replace("(cpf b)", cpfb).replace("(endereco a)", enda).replace("(endereco b)", endb).replace("(cidade a)", cidadea).replace("(cidade b)", cidadeb).replace("(estado a)", estadoa).replace("(estado b)", estadob)

    output = io.BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=output)
    
    return Response(
        output.getvalue(),
        mimetype='application/pdf'
    )
if __name__ == "__main__":
    app.run(host='0.0.0.0')

# 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