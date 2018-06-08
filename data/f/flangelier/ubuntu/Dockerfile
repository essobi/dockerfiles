FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
git \  
openssh-client \  
openssh-server \  
mysql-client \  
wget \  
curl \  
vim  
  
VOLUME /root/.ssh  
  
RUN echo "alias ll='ls -la --color=auto'" >> /root/.bashrc  

