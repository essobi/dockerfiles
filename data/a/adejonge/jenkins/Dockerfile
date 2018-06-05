FROM jenkinsci/jenkins:2.0-rc-1  
USER root  
ADD https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 /usr/bin/docker  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.2.0/bin/linux/amd64/kubectl /usr/bin/kubectl  
RUN chmod +x /usr/bin/docker /usr/bin/kubectl  

