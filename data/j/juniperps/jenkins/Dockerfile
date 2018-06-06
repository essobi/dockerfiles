FROM jenkins/jenkins:lts  
  
LABEL MAINTAINER="Stephen Steiner <ssteiner@juniper.net>"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JAVA_OPTS='-Xmx4096m -Djenkins.install.runSetupWizard=false
-Dhudson.model.DirectoryBrowserSupport.CSP=allow-same-origin'  
ENV JENKINS_USER admin  
ENV JENKINS_PASS admin  
  
USER root  
  
WORKDIR /var/tmp  
  
COPY requirements.txt /var/tmp/requirements.txt  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
COPY basic-security.groovy /var/jenkins_home/init.groovy.d/  
  
RUN apt-get update -qq && \  
apt-get install -yqq apt-utils git-core maven openjdk-8-jdk curl libssl-dev
build-essential libssl-dev libffi-dev python3-dev \  
sshpass && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/cache/apt/*  
  
RUN ( curl https://bootstrap.pypa.io/get-pip.py | python3 ) && \  
( curl -fsSL get.docker.com | bash ) && \  
pip3 install -r requirements.txt && \  
rm -rf /var/tmp/requirements.txt && \  
usermod -aG docker jenkins  
  
RUN xargs /usr/local/bin/install-plugins.sh <
/usr/share/jenkins/ref/plugins.txt  
RUN touch /var/run/docker.sock && chmod 777 /var/run/docker.sock  
  
VOLUME /usr/share/jenkins/ref/plugins  
VOLUME /var/jenkins_home  
  
WORKDIR /var/jenkins_home  
  
USER jenkins  
  
HEALTHCHECK \--interval=1m --timeout=3s CMD curl -s -w "%{http_code}"
http://localhost:8080 -o /dev/null || exit 1  

