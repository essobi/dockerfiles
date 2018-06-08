FROM ubuntu:latest  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get install wget -y  
RUN cd /tmp && wget
http://www.multichain.com/download/multichain-1.0-alpha-27.tar.gz && \  
tar -xvzf multichain-1.0-alpha-27.tar.gz && \  
cd multichain-1.0-alpha-27 && \  
mv multichaind multichain-cli multichain-util /usr/local/bin  
EXPOSE 9087  

