FROM ubuntu:precise  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm git git-core curl wget  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs build-essential  
  
COPY . /src  
WORKDIR /src  
  
RUN npm install  
RUN npm test  
CMD exit $?  

