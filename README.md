# Remarkable 2 templates and resources
Use the ```install.sh``` script to upload the suspension cover and templates provided in this repository. It takes the local ip of your Remarkable device as an argument, *e.g.* ```./install.sh 192.168.50.235```.

The script will ask you for your Remarkable ssh password thrice, once for downloading a pristine copy of the ```templates.json``` file, the second to upload the files to the device, the third to *reboot your reMarkable UI*.

Refer to the page [SSH Access on the reMarkableWiki](https://remarkablewiki.com/tech/ssh) for instructions on how to set passwordless login. Occasionally, after an update, passwordless access will stop working. This can be fixed by deleting the Remarkable ip entry from ```~/.ssh/known_hosts```.

### Positivity journal
The template is to serve both as a logging tool and a daily exercise in positivity.

[![PositivityJournal](https://github.com/r1cc4rdo/Remarkable2/blob/main/images/PositivityJournal_HowTo_thumb.png?raw=true)](https://github.com/r1cc4rdo/Remarkable2/blob/main/images/PositivityJournal_HowTo.png?raw=true)

It's been inspired by the following pages:
* [Five Minute Journal - Daily Journal Techniques and Tips](https://briansunter.com/blog/five-minute-journal/)
* [Deciphering Glyph :: Unproblematize](https://glyph.twistedmatrix.com/2021/08/unproblematize.html)

### Motivational sleep cover
This is to remind myself of good daily habits, and meant to be used to substitute the default ```suspended.png``` image in ```/usr/share/remarkable/```.

[![EverydayMantra](https://github.com/r1cc4rdo/Remarkable2/blob/main/images/EverydayMantra_thumb.png?raw=true)](https://github.com/r1cc4rdo/Remarkable2/blob/main/modified/suspended.png?raw=true)
