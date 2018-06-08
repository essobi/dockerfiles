# Install Java & NodeJS, Vim, Wget & Curl  
# Start script pulls code from S3 and deploys.  
# Script relies on environment variables being passed to the docker image on
creation.  
FROM ubuntu  
RUN apt-get update && apt-get install -y \  
vim \  
wget \  
curl \  
nodejs \  
default-jdk  
RUN export JAVA_HOME=/usr/bin  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
ADD start.sh /root  
RUN chmod 755 /root/start.sh

