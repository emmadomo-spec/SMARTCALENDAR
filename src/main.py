import flet as ft

def main(page: ft.Page):
    # --- Configuration de la page ---
    page.title = "SmartCalendrier - Phase 1"
    page.padding = 10
    
    # ==========================================
    # EXERCICE 1 & 2 : Formulaire Interactif
    # ==========================================
    texte_bienvenue = ft.Text("Bienvenue sur SmartCalendrier", size=20, weight=ft.FontWeight.BOLD)
    champ_nom = ft.TextField(label="Entrez votre nom", width=300)
    message_resultat = ft.Text("", color=ft.colors.GREEN_700, weight=ft.FontWeight.W_500)
    
    def valider_clic(e):
        if champ_nom.value:
            message_resultat.value = f"Bonjour {champ_nom.value}, ravi de vous accueillir !"
        else:
            message_resultat.value = "Veuillez entrer un nom valide."
        page.update()

    bouton_valider = ft.ElevatedButton(text="Valider", on_click=valider_clic)
    
    # Zone formulaire (regroupée dans une colonne)
    zone_formulaire = ft.Column(
        controls=[
            texte_bienvenue,
            champ_nom,
            bouton_valider,
            message_resultat
        ],
        spacing=15
    )

    # ==========================================
    # EXERCICE 3 & 4 : Alignement et Containers (Base de Cartes)
    # ==========================================
    # Ligne 1 : Aligné à gauche
    row1 = ft.Row(
        controls=[
            ft.Icon(ft.icons.CALENDAR_MONTH, color=ft.colors.BLUE),
            ft.Text("Événement du matin : Cours de Python")
        ],
        alignment=ft.MainAxisAlignment.START
    )
    
    # Ligne 2 : Espacée (SPACE_BETWEEN) dans un Container stylisé (Exercice 4)
    # Ce conteneur servira de base visuelle pour nos futures cartes
    carte_evenement = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.icons.CALENDAR_MONTH, color=ft.colors.WHITE),
                ft.Text("Réunion SmartCalendrier - 14h00", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor=ft.colors.BLUE_700,
        padding=20,
        border_radius=10,
        width=400
    )
    
    # Ligne 3 : Aligné au centre
    row3 = ft.Row(
        controls=[
            ft.Icon(ft.icons.CALENDAR_MONTH, color=ft.colors.RED),
            ft.Text("Rappel : Rendu du projet de POO")
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    # Zone d'affichage des lignes d'exercices
    zone_affichage_lignes = ft.Column(
        controls=[
            ft.Text("Démonstration des Layouts & Stykes :", size=16, weight=ft.FontWeight.BOLD),
            row1,
            carte_evenement,
            row3
        ],
        spacing=20
    )

    # ==========================================
    # EXERCICE 5 : La Maquette du Dashboard (Layout global)
    # ==========================================
    # Menu latéral (Navigation Rail)
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.START_OUTLINED, selected_icon=ft.icons.START, label="Accueil"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CALENDAR_MONTH_OUTLINED, selected_icon=ft.icons.CALENDAR_MONTH, label="Calendrier"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, label="Réglages"
            ),
        ]
    )
    
    # Zone de contenu principal (colonne de droite)
    contenu_principal = ft.Container(
        content=ft.Column(
            controls=[
                zone_formulaire,
                ft.Divider(height=30, thickness=1), # Ligne de séparation visuelle
                zone_affichage_lignes
            ],
            scroll=ft.ScrollMode.AUTO
        ),
        bgcolor=ft.colors.GREY_50,
        padding=30,
        expand=True, # Prend tout l'espace disponible restant à droite
        border_radius=15
    )
    
    # Assemblage final de la page dans une grande Row principale
    page.add(
        ft.Row(
            controls=[
                navigation_rail,       # Colonne de gauche (Menu)
                contenu_principal      # Colonne de droite (Contenu)
            ],
            expand=True # Prend toute la hauteur de la fenêtre de l'application
        )
    )

# Lancement de l'application
if __name__ == "__main__":
    ft.app(target=main)
