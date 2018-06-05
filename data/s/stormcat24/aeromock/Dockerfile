FROM ubuntu:14.04  
MAINTAINER stormcat24 <a.yamada24@gmail.com>  
  
# misc  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y openjdk-7-jdk  
  
# aeromock-brew  
RUN git clone https://github.com/CyberAgent/aeromock-brew.git  
RUN cd aeromock-brew && \  
./gradlew use -PaeromockVersion=0.2.4  
  
# config  
ADD config.yaml /root/.aeromock/config.yaml  
  
# run  
ENTRYPOINT ~/.aeromock/applications/current/aeromock  
EXPOSE 3183  

