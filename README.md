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
## With Docker

You can also run the project inside a Docker Container. For this purpose the file Dockerfile was created.


```dockerfile
FROM python:3.8
ADD my_solution.py .
ADD checker.py .
ENV RUN_IN_DOCKER Yes
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENTRYPOINT [ "python3", "./my_solution.py"]
```
