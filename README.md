# DeadOrAlive project
Author : **SANOU Abou**

## How launch the project
The project uses Python Language in its version 3.8. The required packages to install are listed in the file requirement.txt
In order to install the needed package, you have to install pip. Once done, you have to run the following command.

```shell script
pip install -r requirements.txt
```

Once the required package installed, let's run from the root folder of project the following command to launch the project.
```shell script
python main.py
```
## Run on Docker Container

You can also run the project inside a Docker Container. For this purpose the file Dockerfile was created.

```dockerfile
 docker build -t deadoralive .
 docker run deadoralive
```

## Explaining of the organization of project 


    .
    ├── data                   # static files of the project
    ├── core    
    |   ├──models              # Package containing the definition of the models
    |   |   ├── Cell           # File containing the definition of class Cell
    |   |   ├── Grid           # File containing the definition of class Grid
    |   |   ├── Position       # File containing the definition of class Position
    |   |   └── State          # File containing the definition of class State  
    |   └──io                  # Package for input and output logic
    |       └── Input          # File Containing the Intializer of the Grid with initial and final petri state
    ├── .gitinore              # File specifies intentionally untracked files that Git should ignore
    ├── Dockerfie              # The declarative file for to build Docker container
    ├── main.py                # The entrypoint of the project
    ├── README.md              # Source files (alternatively `lib` or `app`)
    └── requirements.txt       # This file is used for specifying what python packages are required to run the project

## Explaining of the algorithm:

The petri is modeled like a graph by using the adjacency matrix.
The choice of the graph approach is explained by the fact that we can apply very simply a lot 
of algorithm o that such as BFS, DFS in order to find for instance the shortest path.

##### How to activate virtual environment created.
For Linux
```shell script
source {path_where_store_virtual_env}/bin/activate
```
For Windows
```shell script
.\env\Scripts\activate
```
## Standard of entities'naming in the project 

We have chosen to use the standard PEP 8 of python community in the entities naming in 
our project.
Let's check out this [link](https://pep8.org/)


## Best pratices for develop 
One of most useful best practices in Python is to use virtual environment.

##### How create a virtual environment.
```shell script
python3 -m venv {path_where_store_virtual_env}
```
The next state is to activate the virtual env has been created
Once activated, let's install the requirement file package by running the following command

```shell script
pip install -r requirements.txt
```




