FROM openjdk:8-jdk  
  
RUN apt-get update && apt-get install -y curl apt-transport-https ca-
certificates python make gcc  
RUN echo 'deb https://apt.dockerproject.org/repo debian-jessie main' >>
/etc/apt/sources.list.d/docker.list  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y nodejs  
RUN npm install -g ionic@3.4.0

