FROM ubuntu:16.04  
ENV LAST_UPDATE=2017-03-22  
# Install.  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential ruby ruby-dev wget sshpass && \  
wget https://github.com/pivotalservices/cfops/releases/download/v3.0.5/cfops
&& \  
chmod 755 cfops && \  
mv cfops /usr/bin && \  
gem install cf-uaac  
  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& useradd -m -s /bin/bash pcfdev \  
&& echo 'pcfdev ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  

