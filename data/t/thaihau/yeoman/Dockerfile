# DOCKER-VERSION 1.8.1  
FROM thaihau/java8:latest  
MAINTAINER Thai Hau <thaihau.y@gmail.com>  
  
# install utilities  
RUN apt-get -y install git sudo zip bzip2 curl  
  
# install node.js  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -  
RUN apt-get install -y nodejs  
  
# install yeoman  
RUN npm install -g yo && \  
bower && \  
grunt-cli  
  
# expose the SSHD port, and run SSHD  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

