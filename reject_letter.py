from docx import Document
from pathlib import Path

player_name_list = []
player_name = ''
while player_name != "conf_exit":
    player_name = input('Enter the player name (type "conf_exit" if there are no more names): ')
    if player_name != "conf_exit":
        player_name_list.append(player_name)

for player in player_name_list:
    document_load_path = Path(__file__).parent / "Team_Fidelity_Rejection_Letter_Template.docx"
    document = Document(document_load_path)
    document_save_path = Path(__file__).parent / f"Team_Fidelity_Rejection_Letter_{player}.docx"
    for paragraph in document.paragraphs:
        if '<player_name>' in paragraph.text:
            paragraph.text = f"Dear {player}"
    document.save(document_save_path)

print("Rejection letter(s) created")