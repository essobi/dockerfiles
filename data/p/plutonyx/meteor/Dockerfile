FROM ubuntu:latest  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y git make build-essential vim curl less ruby python  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
  
RUN apt-get install -y nodejs  
  
RUN curl https://install.meteor.com/ | sh  

