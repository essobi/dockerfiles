# Base image  
FROM ubuntu:16.04  
# Install curl  
RUN apt-get update && apt-get install -y curl  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
ENV echo NODE_PATH $(npm root -g)  
RUN echo export NODE_PATH=$(npm root -g) >> ~/.bash_profile  
  
# Install yo and generator-hubot  
RUN npm install -g yo generator-hubot  
  
# Grant permission to home directory  
RUN chmod g+rwx -R /root # FIXME This command didn't seem to work  

