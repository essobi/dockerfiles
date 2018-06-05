FROM node:9  
# To allow installing dependencies as well as accessing mounted volumes  
USER root  
  
# Install dependencies for mini-breakpad-server  
RUN apt-get update  
RUN apt-get -y install git python build-essential  
  
# Install mini-breakpad-server  
WORKDIR /  
RUN bash -l -c "git clone https://github.com/superhuman/mini-breakpad-
server.git"  
WORKDIR /mini-breakpad-server  
RUN bash -l -c "yarn install"  
  
# mini-breakpad-server listens on port 1127  
EXPOSE 1127  
CMD bash -l -c "node lib/app.js"  

