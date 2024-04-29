# Python_Script
Creating python related script for task automation and task customization.

### File Structure
[Python_Script](Python_Script)<br>

&nbsp; - [Module](https://github.com/mdzaif/Python_Script/tree/main/Module)<br>

&nbsp; &nbsp; &nbsp;-- [__pycache__](https://github.com/mdzaif/Python_Script/tree/main/Module/__pycache__)<br>

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;- [__init__.cpython-310.pyc](https://github.com/mdzaif/Python_Script/blob/main/Module/__pycache__/__init__.cpython-310.pyc)<br>

&nbsp; &nbsp; &nbsp;- [mail_module.py](https://github.com/mdzaif/Python_Script/blob/main/Module/mail_module.py)<br>

&nbsp;- [Scripts](https://github.com/mdzaif/Python_Script/tree/main/Scripts)<br>

&nbsp; &nbsp; &nbsp;-- [__pycache__](https://github.com/mdzaif/Python_Script/tree/main/Scripts/__pycache__)<br>

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;- [custom_mail.cpython-310.pyc](https://github.com/mdzaif/Python_Script/blob/main/Scripts/__pycache__/custom_mail.cpython-310.pyc)<br>

&nbsp; &nbsp; &nbsp;- [custom_mail.py](https://github.com/mdzaif/Python_Script/blob/main/Scripts/custom_mail.py)<br>

&nbsp; &nbsp; &nbsp;- [file.html](https://github.com/mdzaif/Python_Script/blob/main/Scripts/file.html)<br>

&nbsp; &nbsp; &nbsp;- [files.py](https://github.com/mdzaif/Python_Script/blob/main/Scripts/files.py)<br>

&nbsp; &nbsp; &nbsp;- [list.csv](https://github.com/mdzaif/Python_Script/blob/main/Scripts/list.csv)<br>

&nbsp; &nbsp; &nbsp;- [test.txt](https://github.com/mdzaif/Python_Script/blob/main/Scripts/test.txt)

### Setup
In Linux (Debian based):<br>
Download this github reppository. Edit the PYTHONPATH environment variable(Set the path of Module directory). <br>
You can copy this(change the user. and make sure that the file is in same directory also your default shell is bash):<br>

```bash
$ echo 'export PYTHONPATH="/home/user/Python_Script/Module"' >> ~/.bashrc
```
```bash
$ source ~/.bashrc
```
<br><b>Required version </b>:<br>
<b>Python:</b> Python 3.x<br>
<br><b>Required Python Libraries</b>:<br>
<b>Tkinter:</b> It open the file dialog box.<br>
<br>Installation:<br>

```shell
$ sudo apt-get install python3-tk
```
<br>
In Windows:
<br>
First you have to install python in windows system. Then download this github repository.
<br><b>Required version </b>:<br>
<b>Python:</b> Python 3.x<br>
<br><b>Required Python Libraries</b>:<br>
<b>Tkinter:</b> It open the file dialog box.<br>
<br>Installation:<br>

```cmd
 pip install tk
```

<br>Setup PYTHONPATH:<br>

1. Go to the <b>Control panel</b>
2. Then search for <b>Advanced System Settings</b>. (The link will under the 'System'). The link will look like <b>'View the advanced system settings'</b>
3. Click the link that will open <b>'System Properties"</b>. You will see a <b>"Environment Variables..."</b>. Click it. 
4. Now in the <b>"User variable section..."</b>(Actually top section). Click New.
5. Now edit these two section:<br> 
<b>Variable name:</b> PYTHONPATH<br><b>Variable value:</b> copy and paste the path of Module directory which in the Python_Script directory.

### File Description
In <b>Module:</b> We have  the <b>mail_module.py</b> file. which contains all methods under a single class.<br>
In <b>Scripts(executable files are store here):</b><br>
<b>custom_mail.py:</b> Use for custom official mail.<br>
<b>file.html:</b> html contents for custom mail.<br>
<b>files.py:</b> sending files with mail.<br>
<b>list.csv:</b> contains the reciver emails and the variables.<br>
<b>test.txt:</b> contains the text part for custom mail.