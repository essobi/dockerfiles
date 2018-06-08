FROM jenkins/jenkins:latest  
  
ENV DOCKERVERSION=18.03.1-ce  
  
WORKDIR ${JENKINS_HOME}  
  
USER root  
  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
nano tree \  
&& rm -rf /var/lib/apt/lists/*  
  
# install docker client  
RUN curl -fsSLO
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz
\  
&& mv docker-${DOCKERVERSION}.tgz docker.tgz \  
&& tar xzvf docker.tgz \  
&& mv docker/docker /usr/local/bin \  
&& rm -r docker docker.tgz  
  
RUN groupadd -g 998 docker  
RUN usermod -aG docker jenkins  
  
USER jenkins

