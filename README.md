# AS_PROYECTO
Three different ways to deploy the application
## DOCKER
Move into the Docker directory
### Prerequisites
Install docker and docker-compose packages

### Deply the app
* Detached mode: Run containers in the background
  ```sh
  docker-compose up -d
  ```
* Run containers in the foreground
  ```sh
  docker-compose up
  ```
The app will be available in:
* Deployed in localhost: [http://localhost:8000](http://localhost:8000)
* Deployed in the cloud: [http://{machine_ip}:8000](http://{machine_ip}:8000)

## KUBERNETES
Move into the Kubernetes directory
### Prerequisites
These files are prepared to be executed in Google Kubernetes Engine.
If you want to use Minikube to execute them, change both type and port in django/service.yml to NodePort and a number between 30000-32768.

Besides all these files, another file called volume.yml is also provided. If you are using GKE (Google Kubernetes Engine or Minukube), it's not necessary to apply this file.
### Deply the app
* Deploy the app
  ```sh
  cd postgres
  kubectl apply -f volume_claim.yml
  kubectl apply -f secrets.yml
  kubectl apply -f deployment.yml
  kubectl apply -f service.yml
  cd ../django
  kubectl apply -f deployment.yml
  kubectl apply -f service.yml
  ```
The app will be available in:
* Deployed in localhost: [http://localhost:8000](http://localhost:8000)
* Deployed in GKE: [http://{loadbalancer_assigned_ip}:8000](http://{machine_ip}:8000)

## VAGRANT
Move into the Vagrant directory
### Prerequisites
Install vagrant and virtualbox

### Deply the app
* Switch on the machine
  ```sh
  vagrant up
  ```
* Shut down the machine
  ```sh
  vagrant halt
  ```
* Execute the shell script again
  ```sh
  vagrant provision
  ```
The app will be available in:
* Deployed in localhost: [http://localhost:8000](http://localhost:8000)
