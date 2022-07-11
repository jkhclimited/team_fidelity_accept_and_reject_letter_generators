from docx import Document
from pathlib import Path
import datetime

today = datetime.date.today()
next_week = today + datetime.timedelta(days=7)
formatted_next_week = next_week.strftime("%b %d %Y")

player_name_list = []
player_name = ''
while player_name != "conf_exit":
    player_name = input('Enter the player name (type "conf_exit" if there are no more names): ')
    if player_name != "conf_exit":
        player_name_list.append(player_name)

for player in player_name_list:
    document_load_path = Path(__file__).parent / "Team_Fidelity_Offer_Letter_Template.docx"
    document = Document(document_load_path)
    document_save_path = Path(__file__).parent / f"Team_Fidelity_Offer_Letter_{player}.docx"
    for paragraph in document.paragraphs:
        if '<player_name>' in paragraph.text:
            paragraph.text = f"Dear {player}"
        if '<response_date>' in paragraph.text:
            paragraph.text = f"We would like to have your response by {formatted_next_week} 11:59pm EST. In the meantime, please feel free to contact anyone on the Administrator team by tagging anyone with the Administrator role should you have any questions."
    document.save(document_save_path)

print("Acceptance letter(s) created")