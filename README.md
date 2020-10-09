# RockPaperScissorsGame
Rock Paper Scissors game developed using python and tkinter GUI
## Rules
The rules to play it are pretty simple.

The outcome of the game is determined by 3 simple rules:

- Rock wins against scissors.
- Scissors win against paper.
- Paper wins against rock.

## Preinstallations
You need Python 3 installed on your computer. 
Click [here](https://www.python.org/downloads/) to download

## Installation 
Clone the repository:

```git clone https://github.com/Praveena1109/RockPaperScissorGame.git```

Navigate to folder:

```cd RockPaperScissorGame```

```python GUI_RockPaperScissor.py```

## Adding required libraries
The ```requirements.txt``` file should list all Python libraries that this project depends on, and this can be installed using:

```pip install -r requirements.txt```


You can check if pip is available this by running:

```pip --version```

If you have installed Python from source, with an installer from python.org, you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately.

To install pip,  download ```get-pip.py``` by clicking [here](https://bootstrap.pypa.io/get-pip.py) 

Or use:

```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```

Run the command ```python get-pip.py``` in the folder where you have downloaded


## Modules used
- random - Generate pseudo-random numbers with various common distributions.

- tkinter - Interface to Tcl/Tk for graphical user interfaces. Tkinter is included with standard Linux, Microsoft Windows and Mac OS X installs of Python.
  
  Error -  It says ```tkinter ``` can't be imported. To solve this error :
  
  - For windows - ``` pip install python-tk ```
  - For Ubuntu - ```sudo apt-get install python-tk```
 
