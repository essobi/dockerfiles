FROM hseeberger/scala-sbt:8u141-jdk_2.12.3_0.13.16  
  
ENV NVM_VERSION 0.33.5  
ENV NODE_VERSION 4.0.0  
ENV DOCKER_VERSION 17.03.0-ce  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV NVM_DIR /usr/local/nvm  
  
# Install nvm with node and npm  
RUN curl
https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh |
bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH  
  
#Install Docker client  
RUN curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& mv /tmp/docker/* /usr/bin  
  
RUN apt-get update &&\  
apt-get install -y python-pip sshpass &&\  
pip install awscli==1.11.76 &&\  
pip install awscli --upgrade --user &&\  
rm -rf /var/lib/apt/lists/*  

