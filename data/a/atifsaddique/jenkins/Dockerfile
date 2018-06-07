FROM jenkins:latest  
  
# Provide the docker group global id as command line env when running
container.  
ENV DOCKER_GID=993  
USER root  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y sudo libltdl-dev lxc  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
RUN groupadd -g ${DOCKER_GID} docker \  
&& curl -sSL https://get.docker.com/ | sh \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*.bin  
  
RUN usermod -aG docker jenkins  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  
# Here you can install some Jenkins plugins if you want

