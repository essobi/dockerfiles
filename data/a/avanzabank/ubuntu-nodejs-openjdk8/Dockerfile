####################################################################################  
# Creates a container with Node JS, npm, and OpenJDK 8  
####################################################################################  
  
# Command reference:  
# docker build -t avanzabank/ubuntu-nodejs-openjdk8:0.0.1 -t
avanzabank/ubuntu-nodejs-openjdk8:latest .  
# docker run -it avanzabank/ubuntu-nodejs-openjdk8 /bin/bash  
  
  
FROM avanzabank/ubuntu-openjdk8:0.1.2  
  
RUN apt-get update && apt-get install -y \  
nodejs=6.11.4~dfsg-1ubuntu1 \  
npm=3.5.2-0ubuntu4 && \  
rm -rf /var/lib/apt/lists  
  
WORKDIR /opt  

