FROM jenkinsci/jnlp-slave  
  
USER root  
  
WORKDIR /opt  
  
# Add docker client  
ENV DOCKER_VERION 1.12.5  
RUN wget
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERION}.tgz  
RUN tar -zxvf docker-${DOCKER_VERION}.tgz  
RUN cp docker/docker /usr/bin/  
RUN rm -rf /opt/docker*  
  
# Add kubectl client  
ENV KUBECTL_VERSION 1.5.1  
RUN wget https://storage.googleapis.com/kubernetes-
release/release/v1.5.1/bin/linux/amd64/kubectl  
RUN chmod +x kubectl  
RUN mv kubectl /usr/bin/  
  
RUN apt-get update  
  
# Add python virtualenv and libs  
RUN apt-get install -y python-pip python-dev libxml2-dev libxslt1-dev
zlib1g-dev  
RUN pip install virtualenv  
  
# node.js  
RUN apt-get install -y npm nodejs-legacy  
RUN npm install -g jasmine-node  
  
# install junit  
RUN apt-get install -y junit  
  
# install bc - math expressions  
RUN apt-get install -y bc  
  
ENTRYPOINT ["jenkins-slave"]  

