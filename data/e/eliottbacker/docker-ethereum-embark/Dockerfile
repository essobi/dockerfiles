FROM eliottbacker/ethereum  
  
MAINTAINER Eliott BACKER "eliott.backer@gmail.com"  
# no question/dialog is asked during apt-get install  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && apt-get -y -qq upgrade  
  
RUN apt-get -y -qq install git nano curl npm sudo  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
RUN apt-get -qq update  
  
# embark, ethereumjs-testrpc and solidity (Smart Contracts)  
RUN npm install -g embark  
RUN npm install --unsafe-perm -g ethereumjs-testrpc  
RUN npm install -g sol  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8000  
# Start user in dapps directory ...  
WORKDIR /dapps  

