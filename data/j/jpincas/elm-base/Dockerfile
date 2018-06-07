FROM debian:jessie  
  
RUN apt-get update -y  
RUN apt-get install nodejs-legacy -y  
RUN apt-get install npm -y  
RUN npm install -g elm@0.18.0  
RUN apt-get install curl -y  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install nodejs -y  
RUN node -v  
RUN npm install -g webpack webpack-dev-server -y  
  
WORKDIR /home/docker/workspace  
  
CMD elm -v

