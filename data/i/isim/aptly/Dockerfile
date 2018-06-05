FROM ubuntu:wily  
MAINTAINER Ivan Sim "ihcsim@gmail.com"  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && \  
apt-get install -y wget apt-utils && \  
echo "deb http://repo.aptly.info/ squeeze main" >> /etc/apt/sources.list && \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 9E3E53F19C7DE460 && \  
wget -qO - https://www.aptly.info/pubkey.txt | apt-key add \- && \  
apt-get update && \  
apt-get install -y aptly  
EXPOSE 8080  
ENTRYPOINT ["aptly"]  

