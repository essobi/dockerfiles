FROM jenkins/jenkins:lts  
USER root  
ENV ADMIN_USER=admin \  
ADMIN_PASSWORD=admin  
  
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/  
  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt) &&
\  
mkdir -p /usr/share/jenkins/ref/ && \  
echo lts > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state && \  
echo lts > /usr/share/jenkins/ref/jenkins.install.InstallUtil.lastExecVersion  
  
RUN apt-get -qq update && \  
apt-get -qq -y install curl && \  
curl -sSL https://get.docker.com/ | sh  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl && \  
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get |
bash

