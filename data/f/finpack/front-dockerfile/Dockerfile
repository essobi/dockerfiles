FROM circleci/node:8.2.1  
ENV DOCKER_VERSION 17.03.0-ce  
  
#Install aws-cli  
RUN sudo apt-get install python-setuptools python-dev build-essential  
RUN sudo easy_install pip  
RUN sudo pip install --upgrade virtualenv  
RUN sudo pip install \  
awscli==1.11.76  
RUN sudo pip install awscli --upgrade --user  
  
#Instal frontend deps  
RUN sudo npm install -g grunt-cli \  
&& sudo npm install -g karma \  
&& sudo npm install -g bower  
  
#Install Docker client  
RUN sudo curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz \  
&& sudo tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& sudo mv /tmp/docker/* /usr/bin  

