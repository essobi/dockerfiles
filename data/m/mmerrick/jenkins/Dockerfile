FROM jenkins:latest  
USER root  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh  
RUN apt-get update && apt-get install -y build-essential python3 nodejs
openjdk-8-jre libc6-dev-i386 e2fslibs-dev  
USER jenkins  

