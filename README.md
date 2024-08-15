# api_flask_case24

### How to use docker image.
1. First, you need to install Docker on your system. You can download and install Docker from its official website.
2. To run Docker commands, you need to open terminal or command prompt.
3. To use the Docker image, you need to pull it. You can type the `docker pull ysufemrlty/case24:latest` command  to pull the image.
4. You can type the `docker container run sufemrlty/case24` command to run the Docker image.
-----
### Descriptions of commands
1. The `docker pull` command is used to download the Docker image from a Docker hub or other Docker image repository (registry). This command pulls the specified image into your local Docker environment, allowing you to use that image later.
2. The `docker container run` command is used to create and run a new Docker container from the Docker image. This command allows you to start a container based on the Docker image.
3. The `ysufemrlty/case24` we ​​type at the end of the commands is the name of our docker image.

### Screenshot while container is running  
![container running1](https://github.com/user-attachments/assets/868d82c1-6413-4a5f-a764-833e0a9f3cdb)
![container running2](https://github.com/user-attachments/assets/0f6434db-15c3-4262-94ae-f468405f7d05)

### How to use Kubernetes
1. I used `AWS EKS` to set up a `Kubernetes cluster`.
2. To set up the cluster I needed, I went to the AWS EKS service, clicked the `Add Cluster` button and configured the settings according to my needs.
3. To set up the necessary `nodes`, I created my nodes by clicking the `add node groups` button from the `compute` screen in the cluster and configuring the settings according to my needs.
4. I needed to install `kubectl` to perform various management and configuration operations on Kubernetes (https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
5. Since I use AWS, I also downloaded the `AWS CLI` to my system. (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
6. I accessed my AWS account using the AWS CLI. While doing this, I first configured the CLI using my AWS Access Key ID and Secret Access Key information.
7. I filled in the `AWS Access Key ID`, `AWS Secret Access Key`, `Default region name`, `Default output format` information according to my AWS account.
8. I needed to connect to my EKS cluster with kubectl commands via AWS CLI. To do this I used the command `aws eks --region eu-central-1 update-kubeconfig --name case24`
9. I needed to deploy my Kubernetes cluster and Docker image. I used Kubernetes `deployment.yaml` and `service.yaml` files for this process.
10. I deployed my application to Kubernetes with `kubectl apply -f deployment.yaml`, `kubectl apply -f service.yaml` commands and created a LoadBalancer service
11. I used `kubectl get pods`, `kubectl get services` commands to check whether deployment and services are working correctly.
12. To test the application's external access, I typed the command `curl a0713c4d11b6947e6a4a57dfc08e7bc5-2015334342.eu-central-1.elb.amazonaws.com`.
13. To check the health status of the application, I typed the command `curl a0713c4d11b6947e6a4a57dfc08e7bc5-2015334342.eu-central-1.elb.amazonaws.com/health`.
