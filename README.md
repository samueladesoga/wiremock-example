Example repo for mocking external APIs using wiremock in python
==================
Setting up your system
---
1) Make sure you have a working Python 3 installation. Get it from [here](https://www.python.org/downloads/) if you haven't got that already.
2) Download and unzip or clone this project
3) From the project root, run `pip install -r requirements.txt` to install the necessary dependencies

Some API that you can use 
---

- [Zippopotam.us API](http://api.zippopotam.us/)


Pass mapping files in WireMock
---

docker run -it --rm -p 8080:8080 --name wiremock -v $PWD:/home/wiremock wiremock/wiremock:2.35.1-1



Tha ks to chatGPT: Let's break down the command `docker run -it --rm -p 8080:8080 --name wiremock -v $PWD:/home/wiremock wiremock/wiremock:2.35.1-1`:

1. `docker run`: This is the command used to run a Docker container.

2. `-it`: These are two options combined:
   - `-i`: Keep STDIN open even if not attached (so you can interact with the container).
   - `-t`: Allocate a pseudo-TTY (a terminal).

   Together, they provide an interactive terminal session inside the container.

3. `--rm`: This option removes the container automatically when it exits. This is useful for disposable containers.

4. `-p 8080:8080`: This option maps port 8080 of the host machine to port 8080 of the container. It allows communication with services running inside the container via port 8080 from the host.

5. `--name wiremock`: This names the container as "wiremock".

6. `-v $PWD:/home/wiremock`: This option mounts the current directory (`$PWD`) onto the `/home/wiremock` directory inside the container. This is useful for sharing files between the host and the container. Here, `$PWD` is a shell variable representing the present working directory.

7. `wiremock/wiremock:2.35.1-1`: This is the name and tag of the Docker image used to create the container. Docker will pull this image from Docker Hub if it's not available locally. In this case, it's pulling an image named "wiremock" with version 3.5.2 from the "wiremock" repository on Docker Hub.

So, in summary, this command is running a Docker container based on the "wiremock" image, setting it up for interactive use (`-it`), exposing port 8080 for communication with the host, mounting the current directory onto the `/home/wiremock` directory inside the container, and naming the container "wiremock".
