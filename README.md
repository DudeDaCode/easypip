# easypip

An application made in python for installing and making pip packages easily.

![alt text](https://i.ibb.co/0V8Q4BH/capture123.png)

# USAGE

Install (Installs From Pips Server, Recommended) :

1) In the textbox type in the name of the required package(s) (For example :- ```discord.py scipy``` would install discord.py and scipy)
2) Select Install Package from the drop-down menu
3) Click Submit

Install from VCS (Installs From Git, VCS) :

1) In the textbox enter your package url (For example :- ```https://git.repo/some_pkg.git``` would install the given package)
2) Select Install from VCS
3) Click Submit 

Install from Text File (Installs From Text File) :

1) Type in the full directory of your text file
2) Select the Text option 
3) Click Submit

Install From Archive (Installs From An Archive) :

1) Type in the full directory of your archive
2) Select the Archive option 
3) Click Submit 

Install From Source (Installs From Source) :

1) Type in the full directory of your source folder
2) Seelct the Source option 
3) Click Submit


Make Package (Makes Package From Source) :

1) Type in the full directory of your packages source folder 
2) Select Make Package Option 
3) Click Submit


Upgrade (Upgrade A Package) :

1) In the textbox type in the name of the required package(s) (For example :- ```discord.py scipy``` would upgrade discord.py and scipy)
2) Select Upgrade Package 
3) Click Submit

# BUILDING FROM SOURCE
Step 1 - Clone the Repo
Step 2 - Modify the program
Step 3 - Build using pyinstaller ```pyinstaller --onefile --windowed main.py```

# REQUIREMENTS

Python (Tested On 3.8.5)\
Pip\
PySimpleGui\
Wheel (For Making Packages)\
Setuptools (For Making Packages)

