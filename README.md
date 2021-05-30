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
python3.7 main.py
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
    ├── models                 # Package containing the definition of the models
    |   ├── Cell               # File containing the definition of class Cell
    |   ├── Grid               # File containing the definition of class Grid
    |   ├── Position           # File containing the definition of class Position
    |   └── State              # File containing the definition of class State
    ├── test                   # Source files (alternatively `lib` or `app`)
    |   └── Test   
    ├── wr                     # Source files (alternatively `lib` or `app`)
    |   └── Input      
    ├── .gitinore              # File specifies intentionally untracked files that Git should ignore
    ├── Dockerfie              # The declarative file for to build Docker container
    ├── main.py                # The entrypoint of the project
    ├── README.md              # Source files (alternatively `lib` or `app`)
    └── requirements.txt       # This file is used for specifying what python packages are required to run the project
    
