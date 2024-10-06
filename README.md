# Python_Script
Creating python related script for task automation and task customization.


### Setup
In Linux (Debian based):<br>

<b> Quick Setup:</b>

1. clone this repo.

2. run this script:

```bash
chmod +x install.sh && ./install.sh
```

Setup the PYTHONPATH Variable

```bash
 echo 'export PYTHONPATH="/home/user/Python_Script/Module"' >> ~/.bashrc
```
```bash
 source ~/.bashrc
```

In Windows:
<br>
First clone this repository
<br>setup virtualenv(if you run the script in virtual env.):<br>

```ps1
python -m venv <enter_a_name_you_want>
```

```ps1
pip install -r requirement.txt
```

Note that, in .gitingore file add your myenv folder to avoid git track.
<br>Setup PYTHONPATH:<br>

1. Go to the <b>Control panel</b>
2. Then search for <b>Advanced System Settings</b>. (The link will under the 'System'). The link will look like <b>'View the advanced system settings'</b>
3. Click the link that will open <b>'System Properties"</b>. You will see a <b>"Environment Variables..."</b>. Click it. 
4. Now in the <b>"User variable section..."</b>(Actually top section). Click New.
5. Now edit these two section:<br> 
<b>Variable name:</b> PYTHONPATH<br><b>Variable value:</b> copy and paste the path of Module directory which in the Python_Script directory.
