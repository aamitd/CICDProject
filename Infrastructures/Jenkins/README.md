# Jenkins Deployment on Kubernetes using Helm

This guide will walk you through deploying Jenkins on a Kubernetes cluster using Helm.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- A running Kubernetes cluster.
- Helm installed on your local machine and configured to work with your cluster.
- Git repository for managing your Helm charts and deployment configurations.

### Ensure you are on default namespace

kubectl config set-context --current --namespace=default

### Create a `values.yaml` file with the following content:

controller:
    installPlugins:
    - kubernetes:3937.vd7b_82db_e347b_
    - workflow-aggregator:596.v8c21c963d92d
    - git:5.1.0
    - configuration-as-code:1670.v564dc8b_982d0
    - octopusdeploy:3.1.6
    serviceType: LoadBalancer


### Helm Chart Setup

Add the Jenkins Helm repository and update it:
shell
helm repo add jenkins https://charts.jenkins.io
helm repo update


Install Jenkins using the `values.yaml` file:
shell
helm install -f values.yaml helmjenkins jenkins/jenkins


To get the Jenkins admin password, run this command:
shell
kubectl exec --namespace default -it svc/helmjenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo


### Initial Configuration
Open your web browser and access the Jenkins Web UI at 

http://localhost:8080

Enter the initial admin password obtained in step 4 above.
Follow the on-screen instructions to complete the Jenkins setup process.


### Jenkins Configuration
With Jenkins up and running, you can configure it to suit your needs, including setting up build pipelines, adding plugins, and creating jobs for your projects.


### Cleanup
To uninstall Jenkins and remove its resources from your Kubernetes cluster, you can use the following Helm command:
helm uninstall helmjenkins --namespace default


### Additional Resources
- [https://www.jenkins.io/doc/](Jenkins Official Documentation)
- [https://helm.sh/docs/intro/](Helm Documentation)

Happy Jenkins automation!
