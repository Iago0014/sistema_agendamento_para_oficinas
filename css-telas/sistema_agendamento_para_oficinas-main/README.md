<h1>Sistema de agendameto para oficinas</h1>
<p>Nossa oficina apresenta um problema em relação a logística de atendimento, o que ocasiona espera em filas e acaba muitas vezes incomodando nossos clientes, esse problema também faz em alguns casos com que perdemos clientes.</p>


<h2>Requisitos funcionais para os clientes:</h2>
  <p>Tela para o cliente efetuar um cadastro, onde o cliente informara o seu nome, endereço, contato e informações dos veículos.</p>
  <p>O cliente não poderá acessar o sistema de agendamento sem criar seu login.</p>
  <p>Interface para efetuar o agendamento opções, diferentes tipos de manutenção, informações sobre o estado do veículo e a demanda que o cliente necessita.</p>
  <p>Para efetuar o agendamento o sistema precisara ter um calendário contendo os dias e horários disponíveis para que ele possa enfim realizar o agendamento.</p>
  <p>O agendamento criado similarmente a uma ordem de serviço.</p>
  <p>Categorias das demandas. </p>
<h2>Requisitos funcionais para os funcionários:</h2>
  <p>Tela de cadastros dos funcionários.</p>
  <p>Login para os funcionários entrar no sistema.</p>
  <p>Acesso a agenda do dia ver a demanda a ser realizada.</p>
  <p>Poder efetuar um agendamento ou ordem de serviço.</p> 
  <p>Filtrar a demanda por categoria.</p>
  <p>Passar um orçamento para o cliente.</p>
  <p>Agendar a entrega do veículo para o cliente.</p>
  <p>Finalizar a ordem de serviços, mudando o status dela.</p>
  <p>Criar relatórios mensais.</p>

<h2>Requisitos não funcionais:</h2>
  <p>O sistema deve ser acessado via internet. Em ambos os casos da parte do cliente e da parte da oficina.</p>
  <p>Sistema web criado em Python, Html, Css, Bootstrap, Javascript.</p>
  <p>O sistema deve ser intuitivo. </p>
  
<h2> Regras de negócios : </h2>
  <p>O sistema é feito para agilizar e facilitar a logística da empresa evitando filas e maiores dores de cabeça na hora do atendimento. </p>
  <p>E como funciona ? </p>
  <p>De forma simples e fácil o usuário agenda sua manutenção pelo site da TOP Elétrica informando o tipo de manutenção, data e horário.</p>
  <p>Após receber essas informações o sistema irá gravar em seu banco de dados e vai bloquear a manutenção que foi escolhida naquele horário.</p>
  <p>Tendo feito isso o sistema deve enviar um email para a oficina informando data horário e tipo de manutenção que foi agendada.</p>
  <p>Na interface da oficina o sistema também informará os horários e manutenções de cada dia.</p>
  
 <h2> Diagrama de Caso de Uso</h2>
 
![diagramaCU](https://user-images.githubusercontent.com/96276519/166842558-6d899bf1-9665-4e54-bf24-cea2e42ea100.PNG)


<b>Criar Login:</b><text> O cliente poderá criar seu registro de usuário para poder usar os recursos do sistema. O Mecânico Administrador poderá criar seu registro de usuário, para gerenciar sua agenda como os usuários dos clientes. </text> 

<b> Agendamento da ordem de serviço: </b><text> O cliente poderá agendar sua consulta ao mecânico. </text>

<b>Cancelar Agendamento: </b><text> Nessa tela o cliente poderá cancelar o serviço, e o mecânico administrador também poderá cancelar a ordem de serviço. </text>

<b> Acompanhamento da Ordem de Serviço: </b> 
  <text> O Cliente poderá acompanhar a situação do serviço solicitado, e o mecânico administrador, poderá reportar ao cliente a situação do trabalho solicitado. </text>

<b> Filtrar ordem de serviço por Data e Categoria: </b> <text> O mecânico administrador poderá ordenar as ordens de serviços, por data, categoria e urgência das chamadas.</text>

<b> Criar Relatório Final: </b><text> Mecânico administrador poderá criar um relatório sobre as ordens de serviços da semana, mês ou ano. </text>

<h2>Diagrama de atividade</h2>

![diagramaAtividade](https://user-images.githubusercontent.com/100955133/167508263-b2eadb86-946b-4014-a88c-fe2ebb4ce655.PNG)


