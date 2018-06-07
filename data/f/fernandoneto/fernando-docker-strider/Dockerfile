# DOCKER-VERSION 1.0.0  
FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update  
  
# Node.js and Git are required  
RUN apt-get -y install nodejs npm git mysql-client-5.6 mysql-server-5.6  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
# git wants this  
RUN locale-gen en_US.UTF-8  
  
# Get the slave  
RUN npm install -g strider-docker-slave@1.*.*  
#CMD strider-docker-slave  
RUN mkdir -p /home/findhit/workspace  
  
ADD run.sh /home/findhit/workspace/run.sh  
RUN chmod 755 /home/findhit/workspace/run.sh  
  
WORKDIR /home/findhit/workspace  
ENV HOME /home/findhit  
  
CMD ["/home/findhit/workspace/run.sh"]

