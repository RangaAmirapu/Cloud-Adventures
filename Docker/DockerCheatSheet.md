> Written with [StackEdit](https://stackedit.io/).

# Docker cheat sheet

# Installing Docker on Linux

 - **Update Libraries :** 
	 - `sudo yum update`
	 
 - **Install Docker :** 
	 - `sudo yum install docker`
	 
 - **Install Docker Swarm:** 
	 - `sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
 - **Add executable permission:** 
	 - `sudo chmod +x /usr/local/bin/docker-compose`
	 
 - **Check installation:** 
	 - `docker info` `docker-compose --version`
	 
 - **Start Docker Service:** 
	 - `sudo service docker start`
	 
  - **Add current user to Docker group:**
	  - `sudo usermod -a -G docker ec2-user` 
*reboot if needed*
 
 

# Building and running docker  containers

 - **Hello World**
	 -     `docker run hello-world`
   
 - **Pulling and running an linux alpine container in interactive mode with opening container shell**
	 - `docker run -it alpine sh`

 - **Build a Docker image**
	 - `docker image build -t <tagName> <Directory>`
	 - Eg: `docker image build -t  netCoreapp .`

 - **Inspect a Docker image**
	 - `docker image inspect netCoreapp`

 - **List Docker images**
	 - `docker image ls`

 - **Remove Docker images**
	 - `docker image rm <imageid>`
	 
 - **Run a Docker container**
	 - `docker container run <imageName>`

 - **Run a Docker container with custom name**
	 - `docker container run --name <containerName> <imageName>`

 - **Run a Docker container with ports**
	 - `docker container run <imageName> -p 5000:5000`

 - **Run a Docker container  in detached mode**
	 - `docker container run -d <imageName> `

 - **Run a Docker container and handle commands in terminal**
	 - `docker container run -it <imageName>`

- **Run a Docker container and delete when stopped**
	 - `docker container run --rm <imageName>`

- **Run a Docker container with environment variables**
	 - `docker container run -e <envVariable>=<variable> <imageName>`

- **Run a Docker container with restart on failure**
	 - `docker container run --restart on-failure <imageName>`

- **Run a Docker container with volumes**
	 - `docker container run -v "$PWD:/app" <imageName>`

- **Start shell in container**
	 - `docker container exec -it <containerName>`
	 
- **List running containers**
	 - `docker container ls`

- **List all containers**
	 - `docker container ls -a`

 - **Stop a running container**
	 - `docker container stop <containerID>`

 - **Delete a container**
	 - `docker container rm <containerID>`

 - **View logs in a container**
	 - `docker container logs <containerName>`

 - **View logs in real time in a container**
	 - `docker container logs -f <containerName>`

 - **View statistics about running containers**
	 - `docker container stats`


# Docker Networking

 - **View docker networks**
	 - `docker network ls`

 - **Inspect a network**
	 - `docker inspect <networkname>`

 - **Create a network**
	 - `docker network create --driver bridge <networkname>`

- **Run a Docker container with custom network**
	 - `docker container run --rm -itd -p <port>:<port> --net <networkname> --name <containername> <imageName>`

 - **Find IP address of a container**
	 - `docker exec <containername> ifconfig`

 - **Ping a container form another**
	 - `docker exec <containername> ping <IPAddressofAnotherContainer>`


# Docker house keeping

 - **Check disk space**
	 - `docker system df`

 - **Clean unused space**
	 - `docker system prune -f`

 - **Clean all unused images**
	 - `docker system prune -a`

 - **Stop all containers**
	 - `docker container stop $(docker container ls -a -q)`

# Docker Compose

 - **Build an image**
	 - `docker-compose build`
	 
 - **Pull an image**
	 - `docker-compose pull`

 - **Start a project**
	 - `docker-compose up`

 - **Build and start a project**
	 - `docker-compose up --build`

 - **Run in  background**
	 - `docker-compose up --build -d`

 - **List Containers**
	 - `docker-compose ps`

 - **View Logs**
	 - `docker-compose logs -f`

 - **Restart all containers**
	 - `docker-compose restart`

 - **Restart specific containers**
	 - `docker-compose restart <containerName>`

 - **Get into interactive prompt in a running container**
	 - `docker-compose exec <containerName> sh`

 - **Start a container**
	 - `docker-compose up <containerName>`

 - **Remove stopped containers**
	 - `docker-compose rm -f`
	 - `docker-compose prune -f`