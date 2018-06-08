FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y curl git jq apt-utils build-essential
python g++ gcc libssl-dev  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get update && apt-get install nodejs -y  
  
RUN npm install -g pm2  
  
RUN git clone https://github.com/ethcore/fireworks.git  
RUN cd fireworks && npm install && npm install -g  
  
RUN curl -sSL https://get.docker.com/ | sh  
  

