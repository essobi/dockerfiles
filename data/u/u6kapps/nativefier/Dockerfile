FROM ubuntu:latest  
MAINTAINER u6k <u6k.apps@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y build-essential curl && \  
curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \  
apt-get install -y nodejs && \  
npm install nativefier -g && \  
apt-get clean && \  
mkdir /mnt/dest  
  
ENTRYPOINT [ "nativefier" ]  
CMD [ "-h" ]  

