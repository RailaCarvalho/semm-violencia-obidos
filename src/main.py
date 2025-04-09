import flet as ft

def tela_inicial(page):
    # Variável para armazenar o botão selecionado
    botao_selecionado = "Início"

    # 1----Função para definir ações dos cliques nos botões do menu----
    def menu_click(e):
        nonlocal botao_selecionado
        botao_selecionado = e.control.data  # Atualiza o botão selecionado
        conteudo_tela.value = f"Você clicou em: {e.control.data}"
        atualizar_menu()  # Atualiza os botões do menu
        page.update()
    
    def zerar_filtro_click(e):
        pass  # Implementar ação de resetar o filtro

    # 1-------Função para clique no ícone de notificações----
    def notificacao_click(e):
        pass  # Implementar ação do clique

    # 1----Função para clique no ícone de três pontinhos (opções)-----
    def opcoes_click(e):
        pass  # Implementar ação do clique

    # 1---------------------Função do Botão Inicial--------------------
    def b_inicial(e):
        nonlocal botao_selecionado
        botao_selecionado = "Início"
        atualizar_menu()
        
        # 2------------Barra superior com ícones de Notificação------------------------
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

        # 2-----------------Área do filtro----------------------------------
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

        # 2-------------------- Gráficos -----------------------------------
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
            bgcolor=ft.colors.WHITE,  # Fundo branco
            border_radius=8,  # Cantos arredondados
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.colors.BLACK12,  # Sombra suave
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
            bgcolor=ft.colors.WHITE,  # Fundo branco
            border_radius=8,  # Cantos arredondados
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.colors.BLACK12,  # Sombra suave
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
            bgcolor=ft.colors.WHITE,  # Fundo branco
            border_radius=8,  # Cantos arredondados
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.colors.BLACK12,  # Sombra suave
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
            bgcolor=ft.colors.WHITE,  # Fundo branco
            border_radius=8,  # Cantos arredondados
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.colors.BLACK12,  # Sombra suave
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
            bgcolor=ft.colors.WHITE,  # Fundo branco
            border_radius=8,  # Cantos arredondados
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.colors.BLACK12,  # Sombra suave
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
            bgcolor=ft.colors.WHITE,  # Fundo branco
            border_radius=8,  # Cantos arredondados
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.colors.BLACK12,  # Sombra suave
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

        # 2-------------- Area para mostrar o conteúdo ----------------------
        area_conteudo.content = ft.Column(
            [
                barra_superior,
                filtro_periodo,
                area_graficos,
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER
        )

        page.update()  

    # 1-----Função para estilizar o botão com base no estado
    def estilo_botao(nome):
        if botao_selecionado == nome:
            return ft.ButtonStyle(
                bgcolor=ft.colors.BLUE_300,  # Cor para o botão selecionado
                color=ft.colors.WHITE,  # Texto branco
                shape=ft.RoundedRectangleBorder(radius=8)
            )
        else:
            return ft.ButtonStyle(
                bgcolor=ft.colors.GREY_200,  # Cor para botões não selecionados
                color=ft.colors.BLACK,
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
                    bgcolor=ft.colors.BLUE_GREY_50,
                ),
                ft.Divider(thickness=1, color=ft.colors.GREY),

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
                    on_click=menu_click,
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
                                color=ft.colors.BLACK87,
                            ),
                            ft.Text(
                                "Versão: 0.0.1", 
                                size=13,
                                color=ft.colors.BLACK54,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREY_200,
                    border_radius=ft.border_radius.all(8),
                    margin=ft.margin.only(top=20),
                ),
            ],
            spacing=3,
        )

    # 1-----Função para atualizar o menu lateral
    def atualizar_menu():
        menu_lateral.content = criar_menu()

    # 1----Container Esquerdo----
    menu_lateral = ft.Container(
        content=criar_menu(),
        bgcolor=ft.colors.GREY_200,
        padding=1,
        width=270,
        expand=False,
    )

    # 1----Container das informações----
    conteudo_tela = ft.Text("Selecione uma opção no menu", size=20)
    area_conteudo = ft.Container(
        content=ft.Column([conteudo_tela], alignment=ft.MainAxisAlignment.CENTER
),
        expand=True,
        padding=1,
        alignment=ft.alignment.center,
    )

    # 1----Layout geral (divisão entre lateral e área de conteúdo)
    layout = ft.Row(
        [menu_lateral, area_conteudo],
        expand=True,
    )

    # 1----Configuração da página
    page.title = "Tela Inicial"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(layout)

# Executa o aplicativo
ft.app(target=tela_inicial)