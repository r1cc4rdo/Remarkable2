import sys
from pathlib import Path

checklist_portrait = r"""    {
      "name": "Checklist",
      "filename": "P Checklist",
      "iconCode": "\ue98f",
      "categories": [
        "Life/organize"
      ]
    },"""

positivity_journal = r"""    {
      "name": "Positivity Journal",
      "filename": "PositivityJournal",
      "iconCode": "\ue98f",
      "categories": [
        "Life/organize"
      ]
    },"""


def add_entry(filename, to_find, to_add):
    with Path(filename).open('r') as json_file_in:
        json_data = json_file_in.read()

    if not json_data.find(to_find):
        print('Cannot find the hook template.')
        return

    if json_data.find(to_add):
        print('The template to be added is already there.')
        return

    json_data.replace(to_find, to_find + '\n' + to_add + '\n')
    with Path(filename).open('w') as json_file_in:
        json_file_in.write(json_data)


if __name__ == '__main__':
    if (len(sys.argv) < 2) or not sys.argv[1].endswith('.json'):
        print('Usage: tweak_templates path/to/templates.json')

    print(f'Modifying {sys.argv[1]}')
    add_entry(sys.argv[1], checklist_portrait, positivity_journal)
