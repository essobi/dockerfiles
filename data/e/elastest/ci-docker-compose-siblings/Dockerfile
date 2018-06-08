##########################  
#  
# Docker file to extend elastest/docker-siblings:latest with  
# - Docker-compose  
# - npm  
# - node  
# - angular  
#  
########################  
  
FROM elastest/ci-docker-siblings:latest  
  
MAINTAINER Guiomar Tuñon <gtunon@naevatec.com>  
  
# user for setting the environment  
USER root  
  
## Install DOCKER-COMPOSE  
RUN curl -L https://github.com/docker/compose/releases/download/1.14.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
## Install Node  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get install -y nodejs  
RUN npm install node-sass  
  
## Install angular-cli  
RUN npm install -g @angular/cli --unsafe && npm cache clean --force  
  
## git  
RUN apt-get -y install git  
  
# set envs  
ENV WORKSPACE /home/jenkins  
  
USER jenkins  
  
WORKDIR ${WORKSPACE}  
  
# launch container  
ENTRYPOINT ["/bin/bash"]  

