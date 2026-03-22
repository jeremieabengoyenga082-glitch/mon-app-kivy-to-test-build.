from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
import webbrowser

class JeremieMontagePro(App):
    def build(self):
        # Création ya Layout (Structure ya App)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # 1. Logo (Elilingi mpo na Nature)
        layout.add_widget(AsyncImage(source='https://img.icons8.com/color/144/nature.png'))

        # 2. Titre ya Application
        layout.add_widget(Label(text="JÉRÉMIE MONTAGE PRO", font_size='26sp', color=(0, 1, 0.5, 1), bold=True))

        # 3. Fonction mpo ba boutons esala mosala
        def open_link(instance):
            links = {
                "Voir mes Vidéos": "https://youtube.com/@jeremieabengostudio243",
                "Commander Montage": "https://wa.me/243820030730",
                "Partager l'App": "https://wa.me/?text=Tala montage ya banyama na App ya JÉRÉMIE MONTAGE PRO! Télécharge yango awa: [Lien]"
            }
            # Tokofungola lien oyo ekokani na nkombo ya bouton
            text_btn = instance.text
            webbrowser.open(links[text_btn])

        # 4. Kobakisa ba Boutons na ekrani
        for name in ["Voir mes Vidéos", "Commander Montage", "Partager l'App"]:
            btn = Button(text=name, size_hint=(1, 0.2), background_color=(0.1, 0.5, 0.3, 1))
            btn.bind(on_release=open_link)
            layout.add_widget(btn)

        return layout

# Kobanda Application
if __name__ == "__main__":
    JeremieMontagePro().run()

