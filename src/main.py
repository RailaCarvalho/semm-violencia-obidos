import flet as ft

def tela_inicial(page):
    # Variável para armazenar o botão selecionado
    botao_selecionado = "Início"

    # 1----Função para definir ações dos cliques nos botões do menu----
    def menu_click(e):
        nonlocal botao_selecionado
        botao_selecionado = e.control.data  # Atualiza o botão selecionado
        atualizar_menu()  # Atualiza os botões do menu
        page.update()
    
    #2---------------Função do filtro de data------------
    def zerar_filtro_click(e):
        pass  # Implementar ação de resetar o filtro

    # 1-------Função para clique no ícone de notificações----
    def notificacao_click(e):
        pass  # Implementar ação do clique

    # 1----Função para clique no ícone de três pontinhos (opções)-----
    def opcoes_click(e):
        pass  # Implementar ação do clique

#======================ÉREA DE CRIAÇÃO DA TELA INICIAL=======================================================
    #------------Barra superior com ícones de Notificação------------------------
    barra_superior = ft.Row(
            controls=[
                ft.Text("Dashboard", style="headlineMedium", weight=ft.FontWeight.BOLD),
                # Espaço expansível para empurrar os ícones para a direita
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.NOTIFICATIONS,on_click=notificacao_click),
                ft.IconButton(icon=ft.icons.MORE_VERT, on_click=opcoes_click),
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    
    # -----------------Área da barra de filtro----------------------------------
    filtro_periodo = ft.Container(
        content=ft.Row(
            [
                ft.Text("Filtrar por período:", size=14),
                ft.TextField(
                    label="Data inicial", hint_text="dd/mm/aaaa", expand=True
                ),
                ft.TextField(
                    label="Data final", hint_text="dd/mm/aaaa", expand=True
                ),
                ft.IconButton(ft.icons.CLEAR, on_click=zerar_filtro_click),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=10,
        margin=ft.margin.only(top=10),
    )

    #-------------------- Gráficos -----------------------------------
    grafico_1 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Motivos do Acolhimento", size=14, weight=ft.FontWeight.BOLD),
                ft.Image(src="assets/grafico1.png", height=150),
                ft.Text("Gráfico 1: Dados dos motivos", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=250,
        margin=ft.margin.only(right=5),
        bgcolor=ft.Colors.WHITE,  # Fundo branco
        border_radius=8,  # Cantos arredondados
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.Colors.BLACK12,  # Sombra suave
            offset=ft.Offset(1, 1),
            blur_style=ft.ShadowBlurStyle.NORMAL,
            ),
        )
    
    grafico_2 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Idade das Vítimas", size=14, weight=ft.FontWeight.BOLD),
                ft.Image(src="assets/grafico1.png", height=150),
                ft.Text("Gráfico 2: Dados de idades", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=250,
        margin=ft.margin.only(left=5),
        bgcolor=ft.Colors.WHITE,  # Fundo branco
        border_radius=8,  # Cantos arredondados
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.Colors.BLACK12,  # Sombra suave
            offset=ft.Offset(1, 1),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        ),
    )

    grafico_3 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Etnia/Raça", size=14, weight=ft.FontWeight.BOLD),
                ft.Image(src="assets/grafico1.png", height=150),
                ft.Text("Gráfico 3: Dados de etnia/raça", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=250,
        margin=ft.margin.only(right=5),
        bgcolor=ft.Colors.WHITE,  # Fundo branco
        border_radius=8,  # Cantos arredondados
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.Colors.BLACK12,  # Sombra suave
            offset=ft.Offset(1, 1),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        ),
    )

    grafico_4 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Bairros das Vítimas", size=14, weight=ft.FontWeight.BOLD),
                ft.Image(src="assets/grafico1.png", height=150),
                ft.Text("Gráfico 4: Dados de bairros", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=250,
        margin=ft.margin.only(right=5),
        bgcolor=ft.Colors.WHITE,  # Fundo branco
        border_radius=8,  # Cantos arredondados
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.Colors.BLACK12,  # Sombra suave
            offset=ft.Offset(1, 1),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        ),
    )

    grafico_5 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Religião das Vítimas", size=14, weight=ft.FontWeight.BOLD),
                ft.Image(src="assets/grafico1.png", height=150),
                ft.Text("Gráfico 5: Dados de religião", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=250,
        margin=ft.margin.only(right=5),
        bgcolor=ft.Colors.WHITE,  # Fundo branco
        border_radius=8,  # Cantos arredondados
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.Colors.BLACK12,  # Sombra suave
            offset=ft.Offset(1, 1),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        ),
    )

    grafico_6 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Renda Familiar", size=14, weight=ft.FontWeight.BOLD),
                ft.Image(src="assets/grafico1.png", height=150),
                ft.Text("Gráfico 6: Dados de renda", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=250,
        margin=ft.margin.only(right=5),
        bgcolor=ft.Colors.WHITE,  # Fundo branco
        border_radius=8,  # Cantos arredondados
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.Colors.BLACK12,  # Sombra suave
            offset=ft.Offset(1, 1),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        ),
    )
    
    # 2-----Organização da área dos gráficos para rolagem-----
    area_graficos = ft.Column(
        controls=[
            ft.Row(
                [grafico_1, grafico_2],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Row(
                [grafico_3, grafico_4],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Row(
                [grafico_5, grafico_6],
                alignment=ft.MainAxisAlignment.START,
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,  # Habilita a rolagem
        spacing=5,
        alignment=ft.MainAxisAlignment.CENTER,
        )

    # 1---------------------Função do Botão Inicial--------------------
    def b_inicial(e):
        nonlocal botao_selecionado
        botao_selecionado = "Início"
        atualizar_menu()

        # 2-------------- Area para mostrar o conteúdo ----------------------
        area_conteudo.content = ft.Column(
            [
                barra_superior,
                filtro_periodo,
                area_graficos,
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
            scroll="auto", 
        )

        page.update()  

#===================FIM DA TELA INICIAL, COMEÇO DA TELA CADASTRO========================================
    def b_cadastros(e):
        nonlocal botao_selecionado
        botao_selecionado = "Cadastros"
        atualizar_menu()

        # Continuar
        def enviar_dados(e):
            page.dialog = ft.AlertDialog(
                title=ft.Text("Cadastro enviado com sucesso!"),
                on_dismiss=lambda e: print("Fechado")
            )
            page.dialog.open = True
            page.update()
        
        # Funções para navegar entre abas
        def proxima_aba(e):
            if formulario_tabs.selected_index < len(formulario_tabs.tabs) - 1:
                formulario_tabs.selected_index += 1
                page.update()

        def voltar_aba(e):
            if formulario_tabs.selected_index > 0:
                formulario_tabs.selected_index -= 1
                page.update()
            
        def botoes_navegacao(mostrar_proximo=True, mostrar_voltar=True, ultimo=False):
            botoes = []
            if mostrar_voltar:
                botoes.append(ft.ElevatedButton("Voltar", on_click=voltar_aba))
            if mostrar_proximo:
                botoes.append(ft.ElevatedButton("Próximo", on_click=proxima_aba))
            if ultimo:
                botoes = [ft.ElevatedButton("Voltar", on_click=voltar_aba), ft.ElevatedButton("Enviar Cadastro", on_click=enviar_dados)]
            return ft.Row(botoes, alignment="end")
        
        # Identificação
        aba_identificacao = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.TextField(label="Nome completo"),
                ft.Dropdown(label="Gênero", options=[
                    ft.dropdown.Option("Feminino"),
                    ft.dropdown.Option("Masculino"),
                    ft.dropdown.Option("Outro")
                ]),
                ft.TextField(label="Data de nascimento", hint_text="dd/mm/aaaa"),
                ft.TextField(label="Naturalidade"),
                ft.TextField(label="Nacionalidade"),
                ft.TextField(label="Endereço completo"),
                ft.TextField(label="Telefone"),
                ft.TextField(label="Email"),
                botoes_navegacao(mostrar_voltar=False)
            ],
            scroll="auto"
            ),
            expand=True
        )

        # Documentação
        aba_documentacao = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.TextField(label="CPF"),
                ft.TextField(label="RG"),
                ft.TextField(label="NIS"),
                ft.TextField(label="Certidão de nascimento/casamento"),
                ft.TextField(label="Carteira de trabalho"),
                botoes_navegacao()
            ],
            scroll="auto"
            ),
            expand=True
        )
        
        # Dados familiares
        aba_dados_familiares = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.TextField(label="Nome da mãe"),
                ft.TextField(label="Nome do pai (opcional)"),
                ft.Dropdown(label="Estado civil", options=[
                    ft.dropdown.Option("Solteira"),
                    ft.dropdown.Option("Casada"),
                    ft.dropdown.Option("Separada"),
                    ft.dropdown.Option("Viúva")
                ]),
                ft.TextField(label="Responsável legal (se menor)"),
                ft.TextField(label="Com quem reside"),
                botoes_navegacao()
            ],
            scroll="auto"
            ),
            expand=True
        )

        # Dados educacionais
        aba_dados_educacionais = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.Dropdown(label="Escolaridade", options=[
                    ft.dropdown.Option("Ensino Fundamental"),
                    ft.dropdown.Option("Ensino Médio"),
                    ft.dropdown.Option("Superior"),
                    ft.dropdown.Option("Não alfabetizada")
                ]),
                ft.RadioGroup(content=ft.Row([
                    ft.Radio(label="Está frequentando a escola?", value="Sim"),
                    ft.Radio(label="Não", value="Não")
                ])),
                ft.TextField(label="Nome da instituição"),
                ft.Dropdown(label="Turno", options=[
                    ft.dropdown.Option("Manhã"),
                    ft.dropdown.Option("Tarde"),
                    ft.dropdown.Option("Noite")
                ]),
                botoes_navegacao()
            ],
            scroll="auto"
            ),
            expand=True
        )

        # Situação do caso
        aba_situacao_caso = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.Text("Situação de violência", size=16, weight="bold"),
                ft.TextField(label="Tipo de violência"),
                ft.TextField(label="Autor da violência"),
                ft.TextField(label="Frequência"),
                ft.Divider(),

                ft.Text("Situação de saúde", size=16, weight="bold"),
                ft.TextField(label="Problemas de saúde"),
                ft.TextField(label="Uso de medicamentos"),
                ft.TextField(label="Já procurou atendimento médico?"),
                ft.Divider(),

                ft.Text("Situação de drogadição", size=16, weight="bold"),
                ft.TextField(label="Uso de substâncias"),
                ft.TextField(label="Frequência"),
                ft.TextField(label="Faz tratamento?"),
                botoes_navegacao()
            ],
            scroll="auto"
            ),
            expand=True
        )

        # Encaminhamentos (última aba)
        aba_encaminhamentos = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.TextField(label="Encaminhada para"),
                ft.TextField(label="Data do encaminhamento", hint_text="dd/mm/aaaa"),
                ft.TextField(label="Responsável pelo atendimento"),
                ft.TextField(label="Observações"),
                botoes_navegacao(mostrar_proximo=False, ultimo=True)
            ],
            scroll="auto"
            ),
            expand=True
        )

        formulario_tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(text="Identificação", content=aba_identificacao),
                ft.Tab(text="Documentação", content=aba_documentacao),
                ft.Tab(text="Dados familiares", content=aba_dados_familiares),
                ft.Tab(text="Dados educacionais", content=aba_dados_educacionais),
                ft.Tab(text="Situação do caso", content=aba_situacao_caso),
                ft.Tab(text="Encaminhamentos", content=aba_encaminhamentos),
            ],
            expand=True
        )

        area_conteudo.content = ft.Column(
            [
                ft.Text("Cadastro de Dados da Vítima", size=22, weight="bold"),
                formulario_tabs,
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        page.update()  

    # 1-----Função para estilizar o botão com base no estado
    def estilo_botao(nome):
        if botao_selecionado == nome:
            return ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE_300,  # Cor para o botão selecionado
                color=ft.Colors.WHITE,  # Texto branco
                shape=ft.RoundedRectangleBorder(radius=8)
            )
        else:
            return ft.ButtonStyle(
                bgcolor=ft.Colors.GREY_200,  # Cor para botões não selecionados
                color=ft.Colors.BLACK,
                shape=ft.RoundedRectangleBorder(radius=8)
            )

    def criar_menu():
        return ft.Column(
            [
                # Cabeçalho com logo e título
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Image(src="brasaoobidos.png", width=140, fit="contain"),
                            ft.Text("SECRETARIA DA MULHER", size=15, weight=ft.FontWeight.BOLD),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.BLUE_GREY_50,
                ),
                ft.Divider(thickness=1, color=ft.Colors.GREY),

                # Botões do menu
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.HOME),
                            ft.Text("Início"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Início",
                    on_click=b_inicial,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Início"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PERSON_ADD),
                            ft.Text("Cadastros"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Cadastros",
                    on_click=b_cadastros,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Cadastros"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.BAR_CHART),
                            ft.Text("Relatórios"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Relatórios",
                    on_click=menu_click,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Relatórios"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.INFO),
                            ft.Text("Informações"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Informações",
                    on_click=menu_click,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Informações"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.LOCATION_ON),
                            ft.Text("Localização"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Localização",
                    on_click=menu_click,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Localização"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.GAVEL),
                            ft.Text("Legislação"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Legislação",
                    on_click=menu_click,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Legislação"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.SETTINGS),
                            ft.Text("Configurações"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Configurações",
                    on_click=menu_click,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Configurações"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PERSON),
                            ft.Text("Usuário"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    data="Usuário",
                    on_click=menu_click,
                    expand=True,
                    width=270,
                    height=50,
                    style=estilo_botao("Usuário"),
                ),

                # Informações do usuário
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Usuário: Raila", 
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK87,
                            ),
                            ft.Text(
                                "Versão: 0.0.1", 
                                size=13,
                                color=ft.Colors.BLACK54,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.GREY_200,
                    border_radius=ft.border_radius.all(8),
                    margin=ft.margin.only(top=20),
                ),
            ],
            spacing=3,
        )

    # 1-----Função para atualizar o menu lateral
    def atualizar_menu():
        menu_lateral.content = criar_menu()

    # 1----Container Esquerdo dos Botões----
    menu_lateral = ft.Container(
        content=criar_menu(),
        bgcolor=ft.Colors.GREY_200,
        padding=1,
        width=270,
        expand=False,
    )

    # 1----Container das informações----
    area_conteudo = ft.Container(
        content=ft.Column([
            ft.Column([
                barra_superior,
                filtro_periodo,
                area_graficos,
            ],
            scroll="auto", 
            expand=True,
            )
        ], alignment=ft.MainAxisAlignment.CENTER
        ),
        expand=True,
        padding=1,
        alignment=ft.alignment.center,
    )

    # 1----Layout geral (divisão entre lateral e área de conteúdo)----------
    layout = ft.Row(
        [menu_lateral, area_conteudo],
        expand=True,
    )

    # 1----Configuração da página--------
    page.title = "Tela Inicial"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(layout)

# Executa o aplicativo
ft.app(target=tela_inicial)