# 🌸 Análise de Dados sobre Violência contra a Mulher e Desenvolvimento de um Portal de Mapa da Violência no Município de Óbidos
Projeto de extensão desenvolvido no IFPA – Campus Óbidos, em parceria com a Secretaria Municipal da Mulher (SEMM), com o objetivo de informatizar o processo de coleta, armazenamento e análise dos dados de acolhimento de mulheres em situação de violência. Através da criação de um sistema digital, busca-se substituir os registros físicos e possibilitar o acompanhamento em tempo real por meio de dashboards interativos.

## 📈 Fase 
🚧Projeto em desenvolvimento🚧<br>
Organização das telas flet.

# 📌 Índice
- 🎯 Objetivo
- 📍 Justificativa e Motivação
- 🧩 Funcionalidades do Sistema
- 🛠️ Tecnologias Utilizadas
- 🔎 Metodologia
- 📁 Estrutura do Projeto
- 🤝 Equipe
- 📄 Licença

# 🎯 Objetivo
Desenvolver uma plataforma digital para a SEMM de Óbidos-PA com foco em:
- Substituição de registros físicos por sistema informatizado.
- Armazenamento seguro das fichas de atendimento e de caso.
- Análise e visualização interativa dos dados por meio de dashboards.
- Apoio à criação de campanhas preventivas e políticas públicas direcionadas.

# 📍 Justificativa e Motivação
A violência contra a mulher é um problema estrutural que exige ações assertivas e embasadas. A falta de informatização no registro dos atendimentos na SEMM dificulta a gestão e análise dos casos. Este projeto visa melhorar o processo administrativo da secretaria e oferecer suporte para ações preventivas com base em dados reais e atualizados, fortalecendo a rede de proteção às mulheres de Óbidos.

# 🧩 Funcionalidades do Sistema
- 📝 Registro das fichas de atendimento preliminar e ficha de caso com dados sensíveis protegidos.
- 👥 Cadastro de funcionárias, solicitantes, agressores, e locais de ocorrência.
- 📊 Dashboard com gráficos e filtros por bairro, tipo de violência, faixa etária etc.
- 🔐 Controle de acesso para profissionais responsáveis.
- 📂 Armazenamento estruturado em banco de dados relacional.

# 🛠️ Tecnologias Utilizadas
- ```Python```
- ```Flet``` – Criação da interface gráfica
- ```MySQL``` – Banco de dados relacional (falta implementar)
- ```Pandas``` – Manipulação e organização de dados (falta implementar)
- ```DrawDB``` – Modelagem do banco
- ```Matplotlib / Plotly``` – Geração de gráficos e visualizações (falta implementar)

# 🔎 Metodologia
Para entender o fluxo de atendimento da SEMM, foi realizada uma entrevista com a secretária geral da instituição. O processo inicia-se com um atendimento preliminar na recepção e, posteriormente, um atendimento completo feito por assistentes sociais, com informações sigilosas.<br>
Com base nesse fluxo, foi criado um diagrama funcional com a inclusão de novos campos para melhorar a análise dos dados: escolaridade, etnia, religião, renda familiar e profissão. A modelagem do banco de dados foi feita utilizando o DrawDB e exportada para MySQL.<br>
As principais tabelas criadas foram:<br>
- ```funcionario``` e ```solicitante``` – dados pessoais básicos
- Tabelas de referência: ```razaoacolhimento```, ```agressor```, ```localocorrencia```, ```tipoocorrencia```
- ```fichadeatendimento``` – ficha inicial do acolhimento
- ```fichadecaso``` – ficha detalhada preenchida por profissionais específicos

Essas estruturas visam facilitar a digitalização do processo e garantir consistência e agilidade na coleta e análise dos dados.

# 📁 Estrutura do Projeto
(detalhar ainda)

# 🤝 Equipe
- 👩‍💻 **Extensionista – Colaboradora**: Raila Carvalho Araújo

- 👨‍🏫 **Coordenador do Projeto**: João Lúcio de Souza Júnior

- 🙋‍♂️ **Voluntários**:

- - Arthur Castro da Silva Paula

- - Fernanda dos Santos Neves <br><br>

- **Local de Desenvolvimento**:
📍 Instituto Federal do Pará – Campus Óbidos

# 📄 Licença
(planejar ainda)

# Sobre a mim 👩‍💻
Olá! Eu sou Raila Carvalho, estudante de Análise e Desenvolvimento de Sistemas no Instituto Federal do Pará - Campus Óbidos.

## Conecte-se Comigo 🧑‍🤝‍🧑
- **LinkedIn**: [https://www.linkedin.com/in/railacarvalhoaraujo/](https://www.linkedin.com/in/railacarvalhoaraujo/)
- **GitHub**: [https://github.com/RailaCarvalho](https://github.com/RailaCarvalho)
- **Perfil público na DIO**: [https://www.dio.me/users/railacarvalho60](https://www.dio.me/users/railacarvalho60)