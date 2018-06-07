FROM ubuntu:15.10  
RUN apt-get update && \  
apt-get install -y \  
curl \  
wget \  
git \  
vim \  
lynx && \  
apt-get clean  
  
COPY ./docker-entrypoint.sh /  
COPY ./.vimrc /root/  
  
WORKDIR /home  
  
# Download tools.  
RUN wget https://github.com/rancher/rancher-
compose/releases/download/v0.4.2/rancher-compose-linux-amd64-v0.4.2.tar.gz &&
\  
tar -xzf rancher-compose-linux-amd64-v0.4.2.tar.gz --strip 2 && \  
rm rancher-compose-linux-amd64-v0.4.2.tar.gz  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/bin/bash"]  

