FROM debian:latest  
MAINTAINER Manuel Mueller(biothin@gmail.com)  
  
# get packages  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install build-essential apt-utils git python nano curl wget  
ENV NVM_DIR="/root/.nvm"  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install --lts \  
&& npm install --global storjshare-daemon --unsafe-perm  
  
EXPOSE 4000  
EXPOSE 4001  
EXPOSE 4002  
EXPOSE 4003  

