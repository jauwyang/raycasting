*Created by Joshua Auw-Yang*

This program uses ray casting to render a 3D world similar to computer games.


# Getting Started


## Installing pip

First, make sure you have ```pip``` installed on your system. Running the following command will display the current version of pip installed on your system:
* Windows
```sh
py -m pip --version
```
* Unix/MacOS
```sh
python3 -m pip --version
```


## Installing and creating a virtual environment
Next, make sure you have virtual environments installed using the following command:
* Windows
```sh
py -m pip install --user virtualenv
```
* Unix/MacOS
```sh
python3 -m pip install --user virtualenv
```


Now, create a virtual environment called ```env``` by running the following command in the root directory of the project:
* Windows
```sh
py -m venv env
```
* Unix/MacOS
```sh
python3 -m venv env
```

To activate the environment run ```env\Scripts\activate``` on Windows and ```source env/bin/activate``` for Unix/MacOS.
To deactivate run ```deactivate```

To install the required packages to run the project, use ```py -m pip install -r requirements.txt``` on Windows and ```python3 -m pip install -r requirements.txt``` on Unix/MacOS.

# How to Use

To start the program, run the `app.py` script.

The player will spawn in the middle of the map filled with randomly generated walls. The left screen will display a bird's eye view of the map with the player as a red dot. There is a cone on the map indicating the FOV that the player can see on the left screen.

The left screen is the user's first person perspective of the map. Objects that are closer to the user will appear larger and brighter and vice versa.

The following keys are used to control the player:

* *W* - Move up
* *A* - Move left
* *S* - Move down
* *D* - Mode right

* *LEFT_ARROW* - Rotate screen left
* *RIGHT_ARROW* - Rotate screen right

## Configuration

The settings of the simulation can be adjusted in the ```config.py``` file. The following parameters can be adjusted:

* *FOV* - Adjusts the field of view seen by the left screen
* *WALLS* - Controls the number of randomly generated walls on the map