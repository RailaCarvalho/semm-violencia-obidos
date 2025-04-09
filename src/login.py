import flet as ft

def main(page):
    def entrar(e):
        usuario = usuario_field.value
        senha = senha_field.value

        if usuario == "admin" and senha == "1234":
            print("Login bem-sucedido!")
            erro_texto.value = "Login bem-sucedido!"
            erro_texto.color = "green"
        
        elif usuario == "" or senha == "":
            if not usuario_field.value:
                usuario_field.error_text = "Por favor preencha o usuário."
            if not senha_field.value:
                senha_field.error_text = "Por favor preencha sua senha."

        else:
            usuario_field.error_text = ""
            senha_field.error_text = ""
            print("Usuário ou senha incorretos.")
            erro_texto.value = "Usuário ou senha incorretos."
            erro_texto.color = "red"
        
        page.update()

    #Componentes
    erro_texto = ft.Text("", color="red")
    usuario_field = ft.TextField(label="Usuário", autofocus=True, width=400)
    senha_field = ft.TextField(label="Senha", password=True, width=400)
    login_button = ft.ElevatedButton("Entrar", on_click=entrar)

    # Layout da tela
    layout = ft.Column(
        [
            ft.Image(src="assets/brasaoobidos.png", width=100),
            ft.Text("Login SEMM", size=30, weight=ft.FontWeight.BOLD),
            usuario_field,
            senha_field,
            login_button,
            erro_texto,
        ],
        # Alinhamento
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    # Configurações da página
    page.title = "Tela de Login"
    page.window_resizable = True
    page.window_maximized = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(layout)

# Executa o aplicativo
ft.app(target=main)
# ft.app(target=main, view="web_browser", assets_dir="assets") # Não quer aparecer a imagem