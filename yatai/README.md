# Yatai

Yatai is like Github for models, and provides a central place for running models.  Taking care of some of the heavy lifting.

# Installation

Full instructions available on: [https://github.com/bentoml/Yatai/blob/main/docs/admin-guide.md](https://github.com/bentoml/Yatai/blob/main/docs/admin-guide.md)

But in short, the way I installed it is:

1. Install minikube, and helm (brew install works), if not installed.
2. `minikube delete` (if was installed, necessary due to secrets collisions)
3. `minikube start --cpus 4 --memory 4096` (I found the memory important in this
   one to get the nodes to run properly)
4. `helm install yatai yatai/yatai -n yatai-system --create-namespace`
   - This will install to multiple namespaces. Need to delete the namespaces
     individually if redeploying, but really it's better to reset minikube
     because of the way secrets are handled.
5. (wait awhile)
   - Run `kubectl get pods --all-namespaces` to see the status.  Until all are
     ready, don't touch it.  Including the directions it gives at top.
6. Run the `export` and `echo` commands it gives you at top.
7. Run `minikube tunnel` to tunnel to expose port 80.
8. Edit /etc/hosts to have `http://yatai.127.0.0.1.sslip.io/` go to localhost.
