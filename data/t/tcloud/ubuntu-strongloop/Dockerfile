# Version 1.2  
FROM tcloud/ubuntu-nodejs:latest  
MAINTAINER tcloud  
  
RUN useradd -ms /bin/bash strongloop && \  
chown -R strongloop /usr/local && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
USER strongloop  
  
RUN ENV NODE_VERSION 5.1.0  
ENV NVM_DIR ~/.nvm  
  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.29.0/install.sh |
bash  
  
RUN . ~/.nvm/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
npm install -g bower gulp strongloop strong-pm request  
  
VOLUME ["/data","/log"]  
  
WORKDIR /data  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

