# Personal-Voice-Assistant
 Introducing Pip27, your voice assistant powered by Google Speech Recognition. 
 ![image](https://github.com/AdarshRawat1/Personal-Voice-Assistant/assets/100958893/dca0a4a3-3412-4bdf-8b3e-7d513df0cbf1)

 ## Features - 
 - Open websites and Applications 
 - Search Wikipedia effortlessly using simple voice commands. 
 - WebSearcher accurately transcribes your voice, ensuring seamless interactions. 

 ## local installation 
Either you can download the .exe release https://github.com/AdarshRawat1/Personal-Voice-Assistant/releases or locally run the code yourself.

### To locally run the code 
 ## Prequisite 
    👻 Install Python 
    👻 Add python to `path` 
    👻 Check if `pip` is working 
    👻 Install git bash 

 ## Steps  
   - Clone the repository to your system using following command in git bash 

            git clone  https://github.com/AdarshRawat1/Personal-Voice-Assistant.git 

   - Now open cmd in this folder and run following command
    
            pip install -r requirements.txt

   - Run the Detection code 
  
           python Detetction.py 

   - Give the 'Wakeup' voice command.

## Adding the program to auto run at STARTUP

   - Press ```win``` + ```r```
   - type ```shell:startup```
   - copy a shortcut of ```Detection.py``` here 

## Current file structure 
```  
📂 Project 
├── 📂 body
│	├── 📄 automation.py
│ ├── 📄 cli_design.py
│ ├── 📄 intro.py
│	└── 📄 wish.py
├── 📂 Controls
│ └── 📄 control.py
├── 📂 DataStore
│	├── 📂 Captures
│	└── 📂 ScreenShot
├── 📂 utils
│	├── 📄 command.py
│	├── 📄 listen.py
│	└── 📄 speak.py
├── 📂 static
│	└── 📂 audio
│	│  	└──📄 intro.mp3
│ └── 📂 gif
│	│ 	 └──📄 loading.gif
├── 📄 main.py
├── 📄 Detection.py
├── 📄 requirements.txt
└── 📄 README.md

```
