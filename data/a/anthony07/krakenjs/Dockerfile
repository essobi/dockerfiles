FROM ubuntu:trusty  
MAINTAINER anthony07  
  
# install dependencies  
RUN apt-get update  
RUN apt-get install -y --force-yes software-properties-common build-essential
python git-core  
  
# install nodejs  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y --force-yes nodejs  
  
# unleash the kraken  
RUN npm install -g yo bower generator-kraken  
  
# add non-root user to make yeoman run as it should  
RUN adduser --disabled-password --gecos "" launcher; echo "launcher ALL=(ALL)
NOPASSWD:ALL" >> /etc/sudoers  
ENV HOME /home/launcher  
USER launcher  
WORKDIR /home/launcher  
  
# expose the port  
EXPOSE 8000  
# default command  
CMD ["/bin/bash"]  

