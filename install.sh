scp root@$1:../../usr/share/remarkable/templates/templates.json modified/templates/templates.json
python tweak_templates.py modified/templates/templates.json
scp -r modified/* root@$1:../../usr/share/remarkable/
