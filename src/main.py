import flet as ft
import requests

# Função para buscar estados do IBGE
def buscar_estados():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    resposta = requests.get(url)
    estados = resposta.json()
    estados_ordenados = sorted(estados, key=lambda estado: estado["nome"])
    return [{"sigla": estado["sigla"], "nome": estado["nome"]} for estado in estados_ordenados]

# Função para buscar cidades do estado selecionado
def buscar_cidades(uf):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    resposta = requests.get(url)
    cidades = resposta.json()
    return [cidade["nome"] for cidade in cidades]

def tela_inicial(page):
    # variavel que chama a função de buscar estados
    estados = buscar_estados()
    # Variável para armazenar o botão selecionado
    botao_selecionado = "Início"

    # 1----Função para definir ações dos cliques nos botões do menu----
    def menu_click(e):
        nonlocal botao_selecionado
        botao_selecionado = e.control.data  # Atualiza o botão selecionado
        atualizar_menu()  
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

#======================ÁREA DE CRIAÇÃO DA TELA INICIAL=======================================================
    #------------Barra superior com ícones de Notificação------------------------
    barra_superior = ft.Row(
            controls=[
                ft.Text("Dashboard", style="headlineMedium", weight=ft.FontWeight.BOLD),
                # Espaço expansível para empurrar os ícones para a direita
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.NOTIFICATIONS,on_click=notificacao_click),
                ft.IconButton(icon=ft.Icons.MORE_VERT, on_click=opcoes_click),
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
                ft.IconButton(ft.Icons.CLEAR, on_click=zerar_filtro_click),
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
                ft.PieChart(
                    sections=[
                        ft.PieChartSection(value=40, title="Violência", color=ft.Colors.RED),
                        ft.PieChartSection(value=30, title="Abandono", color=ft.Colors.BLUE),
                        ft.PieChartSection(value=20, title="Negligência", color=ft.Colors.GREEN),
                        ft.PieChartSection(value=10, title="Outros", color=ft.Colors.ORANGE),
                    ],
                    sections_space=2,
                    center_space_radius=30,
                    height=200,
                    width=300
                ),
                ft.Text("Gráfico 1: Dados dos motivos", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=300,
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
                ft.LineChart(
                    data_series=[
                        ft.LineChartData(
                            data_points=[
                                ft.LineChartDataPoint(x=0, y=10),
                                ft.LineChartDataPoint(x=1, y=25),
                                ft.LineChartDataPoint(x=2, y=20),
                                ft.LineChartDataPoint(x=3, y=5),
                        ],
                        color=ft.Colors.BLUE,
                        stroke_width=4,
                        curved=True,
                        )
                    ],
                    min_x=0,
                    max_x=3,
                    min_y=0,
                    max_y=30,
                    left_axis=ft.ChartAxis(
                        labels=[
                            ft.ChartAxisLabel(value=0, label=ft.Text("0")),
                            ft.ChartAxisLabel(value=10, label=ft.Text("10")),
                            ft.ChartAxisLabel(value=20, label=ft.Text("20")),
                            ft.ChartAxisLabel(value=30, label=ft.Text("30")),
                        ],
                        labels_size=40,
                    ),
                    bottom_axis=ft.ChartAxis(
                        labels=[
                            ft.ChartAxisLabel(value=0, label=ft.Text("0-5")),
                            ft.ChartAxisLabel(value=1, label=ft.Text("6-10")),
                            ft.ChartAxisLabel(value=2, label=ft.Text("11-15")),
                            ft.ChartAxisLabel(value=3, label=ft.Text("16-18")),
                        ],
                        labels_size=40,
                    ),
                    tooltip_bgcolor=ft.Colors.BLUE_GREY,
                    height=200,
                    width=250,
                ),
                ft.Text("Gráfico 2: Dados de idades", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=300,
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
                ft.PieChart(
                    sections=[
                        ft.PieChartSection(value=47.3, title="Brancos", color=ft.Colors.BLUE),
                        ft.PieChartSection(value=43.1, title="Pardos", color=ft.Colors.GREEN),
                        ft.PieChartSection(value=7.6, title="Negros", color=ft.Colors.BROWN),
                        ft.PieChartSection(value=2.1, title="Amarelos", color=ft.Colors.YELLOW),
                        ft.PieChartSection(value=0.3, title="Indígenas", color=ft.Colors.RED),
                    ],
                    sections_space=2,
                    center_space_radius=40,
                    height=200,
                    width=200,
                ),
                ft.Text("Gráfico 3: Dados de etnia/raça", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=300,
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
                ft.BarChart(
                    bar_groups=[
                        ft.BarChartGroup(
                            x=0,
                            bar_rods=[
                                ft.BarChartRod(from_y=0, to_y=18, color=ft.Colors.RED, width=20, border_radius=0)
                            ],
                        ),
                        ft.BarChartGroup(
                            x=1,
                            bar_rods=[
                                ft.BarChartRod(from_y=0, to_y=10, color=ft.Colors.GREEN, width=20, border_radius=0)
                            ],
                        ),
                        ft.BarChartGroup(
                            x=2,
                            bar_rods=[
                                ft.BarChartRod(from_y=0, to_y=14, color=ft.Colors.BLUE, width=20, border_radius=0)
                            ],
                        ),
                        ft.BarChartGroup(
                            x=3,
                            bar_rods=[
                                ft.BarChartRod(from_y=0, to_y=7, color=ft.Colors.ORANGE, width=20, border_radius=0)
                            ],
                        ),
                    ],
                    groups_space=10,
                    left_axis=ft.ChartAxis(
                        labels_size=30,
                        title=ft.Text("Nº de vítimas")
                    ),
                    bottom_axis=ft.ChartAxis(
                        labels=[
                            ft.ChartAxisLabel(value=0, label=ft.Text("Centro", size=10)),
                            ft.ChartAxisLabel(value=1, label=ft.Text("P. Socorro", size=10)),
                            ft.ChartAxisLabel(value=2, label=ft.Text("C. Nova", size=10)),
                            ft.ChartAxisLabel(value=3, label=ft.Text("S. Francisco", size=10)),
                        ],
                        labels_size=20
                    ),
                    max_y=20,
                    width=300,
                    height=200
                ),
                ft.Text("Gráfico 4: Dados de bairros", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=300,
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
                ft.PieChart(
                    sections=[
                        ft.PieChartSection(
                            value=40,
                            color=ft.Colors.BLUE,
                            title="Católica",
                            title_style=ft.TextStyle(size=10, color=ft.Colors.WHITE)
                        ),
                        ft.PieChartSection(
                            value=30,
                            color=ft.Colors.GREEN,
                            title="Evangélica",
                            title_style=ft.TextStyle(size=10, color=ft.Colors.WHITE)
                        ),
                        ft.PieChartSection(
                            value=20,
                            color=ft.Colors.ORANGE,
                            title="Sem religião",
                            title_style=ft.TextStyle(size=10, color=ft.Colors.WHITE)
                        ),
                        ft.PieChartSection(
                            value=10,
                            color=ft.Colors.PINK,
                            title="Outras",
                            title_style=ft.TextStyle(size=10, color=ft.Colors.WHITE)
                        ),
                    ],
                    sections_space=2,
                    center_space_radius=35,
                    height=200,
                    width=200,
                ),
                ft.Text("Gráfico 5: Dados de religião", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=300,
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
                ft.BarChart(
                    bar_groups=[
                        ft.BarChartGroup(
                            x=0,
                            bar_rods=[ft.BarChartRod(from_y=0, to_y=25, color=ft.Colors.RED, width=20, border_radius=0)],
                        ),
                        ft.BarChartGroup(
                            x=1,
                            bar_rods=[ft.BarChartRod(from_y=0, to_y=30, color=ft.Colors.BLUE, width=20, border_radius=0)],
                        ),
                        ft.BarChartGroup(
                            x=2,
                            bar_rods=[ft.BarChartRod(from_y=0, to_y=15, color=ft.Colors.GREEN, width=20, border_radius=0)],
                        ),
                        ft.BarChartGroup(
                            x=3,
                            bar_rods=[ft.BarChartRod(from_y=0, to_y=10, color=ft.Colors.ORANGE, width=20, border_radius=0)],
                        ),
                    ],
                    groups_space=30,
                    max_y=35,
                    height=200,
                    width=300,
                    left_axis=ft.ChartAxis(
                        labels_size=30,
                        title=ft.Text("Nº de Famílias")
                    ),
                    bottom_axis=ft.ChartAxis(
                        labels=[
                            ft.ChartAxisLabel(value=0, label=ft.Text("Até 1 SM", size=10)),
                            ft.ChartAxisLabel(value=1, label=ft.Text("1 a 2 SM", size=10)),
                            ft.ChartAxisLabel(value=2, label=ft.Text("2 a 3 SM", size=10)),
                            ft.ChartAxisLabel(value=3, label=ft.Text("+3 SM", size=10)),
                        ],
                        labels_size=20
                    ),
                ),
                ft.Text("Gráfico 6: Dados de renda", size=12),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        height=300,
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
    
    # 2-----Organização da área dos gráficos para rolagem----------------------------------
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

    # 1---------------------Função do Botão Inicial-----------------------------------------
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
    #---------Funções da biblioteca request necessárias pra tela de cadastro----------------------
    estado_dropdown = ft.Dropdown(
        label="Estado",
        options=[ft.dropdown.Option(est["sigla"], text=est["nome"]) for est in estados],
        width=200,
    )

    cidade_dropdown = ft.Dropdown(
        label="Cidade",
        options=[],
        width=300,
    )

    def atualizar_cidades(e):
        uf = estado_dropdown.value
        if uf:
            cidades = buscar_cidades(uf)
            cidade_dropdown.options = [ft.dropdown.Option(cidade) for cidade in cidades]
            cidade_dropdown.value = None
            page.update()
    
    estado_dropdown.on_change = atualizar_cidades

    def b_cadastros(e):
        nonlocal botao_selecionado
        botao_selecionado = "Cadastros"
        atualizar_menu()

        # -------Função para o envio dos dados (falta implementar)----------
        def enviar_dados(e):
            page.dialog = ft.AlertDialog(
                title=ft.Text("Cadastro enviado com sucesso!"),
                on_dismiss=lambda e: print("Fechado")
            )
            page.dialog.open = True
            page.update()
        
        # ------Funções para navegar entre abas----------------------------
        def proxima_aba(e):
            if formulario_tabs.selected_index < len(formulario_tabs.tabs) - 1:
                formulario_tabs.selected_index += 1
                page.update()

        def voltar_aba(e):
            if formulario_tabs.selected_index > 0:
                formulario_tabs.selected_index -= 1
                page.update()
            
        #-------------Botões abaixo do formulário-----------------------------
        def botoes_navegacao(mostrar_proximo=True, mostrar_voltar=True, ultimo=False):
            botoes = []
            if mostrar_voltar:
                botoes.append(
                    ft.ElevatedButton(
                        text="Voltar", 
                        icon=ft.Icons.ARROW_BACK, 
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREY_200,
                            color=ft.Colors.BLACK87,
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=10
                            ),
                        on_click=voltar_aba
                        )
                    )
                
            if mostrar_proximo:
                botoes.append(
                    ft.ElevatedButton(
                        text="Próximo", 
                        icon=ft.Icons.ARROW_FORWARD,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_600,
                            color=ft.Colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=10
                        ),
                        on_click=proxima_aba)
                    )
                
            if ultimo:
                botoes = [
                    ft.ElevatedButton(
                        text="Voltar", 
                        icon=ft.icons.ARROW_BACK,
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.GREY_200,
                            color=ft.colors.BLACK87,
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=10
                        ),
                        on_click=voltar_aba
                        ), 
                    ft.ElevatedButton(
                        text="Enviar Cadastro", 
                        icon=ft.icons.SEND_ROUNDED,
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.GREEN_600,
                            color=ft.colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=10
                        ),
                        on_click=enviar_dados
                        )
                    ]
            
            return ft.Row(botoes, alignment="end")
         
        # ----Aba de Identificação
        aba_identificacao = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.Row([
                    ft.TextField(label="Nome completo", expand=1),
                    ft.TextField(label="Idade",
                    keyboard_type=ft.KeyboardType.NUMBER,
                    max_length=3,
                    width=100  # Controla o tamanho do campo
                )
                ]),

                ft.Row([
                    ft.TextField(
                    label="Data de Nascimento",
                    hint_text="dd/mm/aaaa",
                    keyboard_type=ft.KeyboardType.DATETIME,
                    prefix_icon=ft.Icons.CALENDAR_MONTH, #Ver como substituit esse prefix_icon por algo a altura🥲
                    max_length=10,
                    expand=True
                ),
                ft.Text("Naturalidade:", size=18),
                estado_dropdown, 
                cidade_dropdown
                ]),

                ft.Column(
                [
                    ft.Text("Endereço", size=18, weight=ft.FontWeight.BOLD),

                    ft.TextField(
                        label="Endereço",
                        hint_text="Rua, avenida, travessa...",
                        prefix_icon=ft.Icons.HOME,
                        expand=True
                    ),

                    ft.Row(
                        [
                            ft.TextField(
                                label="Bairro",
                                hint_text="Ex: Centro",
                                prefix_icon=ft.Icons.LOCATION_CITY,
                                expand=True
                            ),
                            ft.Dropdown(
                                label="Perímetro",
                                hint_text="Escolha",
                                prefix_icon=ft.Icons.MAP,
                                options=[
                                    ft.dropdown.Option("Urbano"),
                                    ft.dropdown.Option("Rural")
                                ],
                                width=200
                            ),
                        ],
                        spacing=10
                    )
                ]
            ),

                ft.Column(
                    [
                        ft.Text("Contato", size=18, weight=ft.FontWeight.BOLD),
                        
                        ft.Row([
                            ft.TextField(
                            label="Telefone / Celular 1",
                            hint_text="(XX) XXXXX-XXXX",
                            keyboard_type=ft.KeyboardType.PHONE,
                            prefix_icon=ft.Icons.PHONE,
                            expand=True
                            ),

                            ft.TextField(
                            label="Telefone / Celular 2",
                            hint_text="(XX) XXXXX-XXXX",
                            keyboard_type=ft.KeyboardType.PHONE,
                            prefix_icon=ft.Icons.PHONE,
                            expand=True
                            ),
                        ]),
                        ft.TextField(label="Email"),

                        ft.Text("Escolaridade", size=18, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            [
                                ft.Dropdown(
                                    label="Escolaridade",
                                    hint_text="Escolha a escolaridade",
                                    prefix_icon=ft.Icons.BOOKMARK,
                                    options=[
                                        ft.dropdown.Option("Ensino Fundamental"),
                                        ft.dropdown.Option("Ensino Médio"),
                                        ft.dropdown.Option("Ensino Técnico"),
                                        ft.dropdown.Option("Ensino Superior"),
                                        ft.dropdown.Option("Outro")
                                    ],
                                    width=300
                                ),
                                ft.TextField(
                                    label="Instituição",
                                    hint_text="Nome da instituição",
                                    prefix_icon=ft.Icons.SCHOOL,
                                    expand=True
                                ),

                                ft.Dropdown(
                                    label="Turno",
                                    hint_text="Escolha o turno",
                                    prefix_icon=ft.Icons.SUNNY,
                                    options=[
                                        ft.dropdown.Option("Matutino"),
                                        ft.dropdown.Option("Vespertino"),
                                        ft.dropdown.Option("Noturno")
                                    ],
                                    width=200
                                ),
                            ],
                            spacing=10
                        ),
                    ]
                ),
                ft.Text("Informações Complementares", size=18, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        ft.TextField(
                            label="Profissão",
                            hint_text="Ex: Professora",
                            prefix_icon=ft.Icons.WORK,
                            expand=True
                        ),
                        ft.TextField(
                            label="Horário de trabalho",
                            hint_text="Ex: 08h às 18h",
                            prefix_icon=ft.Icons.ACCESS_TIME,
                            width=250
                        ),
                    ],
                    spacing=10
                ),

                ft.Row(
                    [
                        ft.TextField(
                            label="Nome do Pai",
                            prefix_icon=ft.Icons.MAN,
                            expand=True
                        ),
                        ft.TextField(
                            label="Nome da Mãe",
                            prefix_icon=ft.Icons.WOMAN,
                            expand=True
                        ),
                    ],
                    spacing=10
                ),

                botoes_navegacao(mostrar_voltar=False)
            ],
            scroll="auto"
            ),
            expand=True
        )

        #------Campos necessários da aba de DOCUMENTAÇÃO-------------------------
        # -----Dificuldade especial
        dificuldade_opcoes = ft.Row([
            ft.Checkbox(label="Visual total"),
            ft.Checkbox(label="Auditiva parcial"),
            ft.Checkbox(label="Auditiva total"),
            ft.Checkbox(label="De linguagem"),
            ft.Checkbox(label="Física"),
            ft.Checkbox(label="Mental"),
        ], spacing=5, visible=False)

        # -----Campo da outra instituição
        campo_outra_instituicao = ft.TextField(
            label="Qual instituição (se sim)",
            width=400,
            visible=False
        )

        # ----Criando os radio groups Sim Não dificuldade e acompanhamento--------
        dificuldade_radio = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="sim", label="Sim"),
                ft.Radio(value="nao", label="Não"),
            ])
        )

        acompanhamento_radio = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="sim", label="Sim"),
                ft.Radio(value="nao", label="Não"),
            ])
        )

        # -------Funções de mudança de dificuldade e acompanhamento
        def dificuldade_changed(e):
            dificuldade_opcoes.visible = dificuldade_radio.value == "sim"
            page.update()

        def acompanhamento_changed(e):
            campo_outra_instituicao.visible = acompanhamento_radio.value == "sim"
            page.update()

        # Adiciona os handlers
        dificuldade_radio.on_change = dificuldade_changed
        acompanhamento_radio.on_change = acompanhamento_changed

        # Valor inicial dificuldade e acompanhamento
        dificuldade_radio.value = "nao"
        acompanhamento_radio.value = "nao"

        # -------Aba Documentação----------
        aba_documentacao = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                ft.Text("Documentos disponíveis:", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.Checkbox(label="RN"),
                    ft.Checkbox(label="RG"),
                    ft.Checkbox(label="CPF"),
                    ft.Checkbox(label="TEC"),
                    ft.Checkbox(label="CTPS"),
                    ft.Checkbox(label="C. SUS"),
                ], spacing=40),

                ft.Divider(),

                ft.Text("Possui dificuldade especial?", size=16, weight=ft.FontWeight.BOLD),
                dificuldade_radio,
                ft.Text("Se sim, qual?", size=14, weight=ft.FontWeight.W_500),
                dificuldade_opcoes,
                ft.Divider(),

                ft.TextField(label="Motivo do encaminhamento", multiline=True),
                ft.Row([
                    ft.TextField(label="Quem encaminhou", expand=True),        
                    ft.TextField(
                        label="Data do encaminhamento",
                        hint_text="dd/mm/aaaa",
                        keyboard_type=ft.KeyboardType.DATETIME,
                        prefix_icon=ft.Icons.CALENDAR_MONTH,
                        max_length=10,
                        width=300
                    ),
                ]),
                
                ft.Text("Já é acompanhado por outra instituição?", size=16, weight=ft.FontWeight.BOLD),
                acompanhamento_radio,
                campo_outra_instituicao,

                botoes_navegacao()
            ],
            scroll="auto"
            ),
            expand=True
        )
        
        #======Função para serem usadas na aba de DADOS FAMILIARES======
        familiares = []

        def adicionar_familiar(e):
            nova_linha = ft.Row([
                ft.TextField(label="Nome", width=280, expand=True),
                ft.TextField(label="Parentesco", width=125),
                ft.TextField(label="Necessidades especiais", width=140),
                ft.TextField(label="Idade", width=67),
                ft.Dropdown(
                    label="Sexo",
                    options=[
                        ft.dropdown.Option("Masculino"),
                        ft.dropdown.Option("Feminino"),
                        ft.dropdown.Option("Outro"),
                    ],
                    width=108
                ),
                ft.Row([
                    ft.Checkbox(label="RG"),
                    ft.Checkbox(label="CPF"),
                    ft.Checkbox(label="TE"),
                    ft.Checkbox(label="RN"),
                    ft.Checkbox(label="CT")
                ], spacing=2),
            ], scroll="auto")
            familiares.append(nova_linha)
            lista_familiares.controls.append(nova_linha)
            page.update()

        lista_familiares = ft.Column()
        botao_adicionar = ft.ElevatedButton(text="Adicionar familiar", on_click=adicionar_familiar)
        posicao_referencia = ft.TextField(label="Posição de referência na família", width=300)
        tipo_familia = ft.Row([
            ft.Text("Tipo de família:", size=16),
            ft.RadioGroup(
                content=ft.Row([
                    ft.Radio(value="Nuclear", label="Nuclear"),
                    ft.Radio(value="Monoparental", label="Monoparental"),
                    ft.Radio(value="Homoparental", label="Homoparental"),
                    ft.Radio(value="Extensiva", label="Extensiva"),
                ])
            )
        ])

        # --------Aba Dados familiares
        aba_dados_familiares = ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column([
                #=====Exemplos de dados, atualizar para reais necessários semm=====
                ft.Text("Pessoas que moram com a vítima:", size=16, weight=ft.FontWeight.BOLD),
                botao_adicionar,
                lista_familiares,
                ft.Divider(),
                posicao_referencia,
                tipo_familia,
        
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
                ft.Tab(tab_content=ft.Text("Identificação", size=16, weight=ft.FontWeight.BOLD), content=aba_identificacao),
                ft.Tab(tab_content=ft.Text("Documentação", size=16, weight=ft.FontWeight.BOLD), content=aba_documentacao),
                ft.Tab(tab_content=ft.Text("Dados familiares", size=16, weight=ft.FontWeight.BOLD), content=aba_dados_familiares),
                ft.Tab(tab_content=ft.Text("Dados educacionais", size=16, weight=ft.FontWeight.BOLD), content=aba_dados_educacionais),
                ft.Tab(tab_content=ft.Text("Situação do caso", size=16, weight=ft.FontWeight.BOLD), content=aba_situacao_caso),
                ft.Tab(tab_content=ft.Text("Encaminhamentos", size=16, weight=ft.FontWeight.BOLD), content=aba_encaminhamentos),
            ],
            expand=True
        )

        area_conteudo.content = ft.Column(
            [
                ft.Text("Cadastro de Dados da Vítima", style="headlineMedium", weight=ft.FontWeight.BOLD),
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
                            ft.Icon(ft.Icons.HOME),
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
                            ft.Icon(ft.Icons.PERSON_ADD),
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
                            ft.Icon(ft.Icons.BAR_CHART),
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
                            ft.Icon(ft.Icons.INFO),
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
                            ft.Icon(ft.Icons.LOCATION_ON),
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
                            ft.Icon(ft.Icons.GAVEL),
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
                            ft.Icon(ft.Icons.SETTINGS),
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
                            ft.Icon(ft.Icons.PERSON),
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
                    content=ft.Row(
                        [
                            ft.Icon(ft.Icons.PERSON, size=30, color=ft.Colors.BLACK87),
                            ft.Column(
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
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=2,
                            ),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.GREY_200,
                    border_radius=ft.border_radius.all(12),
                    margin=ft.margin.only(top=20),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=8,
                        color=ft.Colors.BLACK12,
                        offset=ft.Offset(1, 1),
                    ),
                )

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

    # 1---------Layout geral (divisão entre lateral e área de conteúdo)-------------
    layout = ft.Row(
        [menu_lateral, area_conteudo],
        expand=True,
    )

    # 1---------------Configuração da página---------------------
    page.title = "Tela Inicial"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(layout)
 
ft.app(target=tela_inicial)