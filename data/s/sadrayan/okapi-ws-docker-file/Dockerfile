############################################################  
# Dockerfile to build Okapi Installed Containers  
# Based on Ubuntu:latest  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Maintaner Sadra Ab <sadrayan@gmail.com>  
  
EXPOSE 8080  
  
# Pre-requisite for compiling Okapi  
RUN dpkg --add-architecture i386  
RUN apt-get update  
RUN apt-get install -y \  
gcc \  
gcc-multilib \  
libc6-i386 \  
make \  
bison \  
flex \  
openjdk-8-jdk:i386 \  
git \  
maven \  
curl \  
ant \  
vim  
  
# jdk 8 and gcc 5.3.1  
RUN cp /usr/lib/jvm/java-8-openjdk-i386/include/jni.h
/usr/lib/gcc/x86_64-linux-gnu/5.3.1/include  
  
  
RUN mkdir -p /home/okapi  
RUN git clone https://github.com/YorkUIRLab/okapi.git /home/okapi  
RUN git clone https://github.com/YorkUIRLab/okapi-web-service.git /home/okapi-
web-service  
RUN git config --global user.email "sadrayan@gmail.com"  
RUN git config --global user.name "sadrayan"  
  
# initialize okapi  
RUN /home/okapi/scripts/init.sh  
  
# Setup env variables  
RUN cp /home/okapi/environmentSettings.bshrc ~/.bashrc  
RUN /bin/bash -c 'source ~/.bashrc ; echo $OKAPI_BINDIR'  
  
# run Okapi WS  
#RUN /home/okapi-web-service/init.sh  
  
  
#VOLUME /tmp  
#RUN cp /home/okapi-web-service/output/okapi-web-service-0.1.0.jar app.jar  
#RUN bash -c 'touch /app.jar'  
#ENTRYPOINT ["java", "-jar", "/app.jar"]  
  
#WORKDIR /home/okapi  

