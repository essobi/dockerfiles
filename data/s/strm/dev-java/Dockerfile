FROM debian:jessie  
  
MAINTAINER opsxcq <opsxcq@thestorm.com.br>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl wget unrar-free unzip \  
emacs \  
openjdk-8-jdk-headless maven2 ant\  
eclipse eclipse-jdt \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp/ && \  
wget https://github.com/ervandew/eclim/releases/download/2.6.0/eclim_2.6.0.jar
&& \  
java -Declipse.home=/opt/eclipse -jar eclim_2.6.0.jar install  
  
EXPOSE 8080  
VOLUME /src  
WORKDIR /src  
  
ENTRYPOINT ["/bin/bash"]  
  

