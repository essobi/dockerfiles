FROM ubuntu:wily  
MAINTAINER Justin McMurdie <mcmurdiej@gmail.com>  
  
ENV HOME /root  
  
RUN apt-get update && \  
apt-get install -y git curl sudo && \  
apt-get install -y build-essential python python-pip libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create the user we will run as moving foward (not root)  
ENV DOCKER_USER docker-user  
RUN adduser --disabled-password --gecos "" $DOCKER_USER && \  
usermod -G root $DOCKER_USER && \  
echo "$DOCKER_USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers  
  
ENV HOME /home/$DOCKER_USER  
USER docker-user  
RUN sudo mkdir /src && \  
sudo chown $DOCKER_USER /src  
  
# Install node  
ENV NODE_VERSION=5.7.0  
ENV NPM_VERSION=3  
ENV NODE_PATH=/usr/lib/node_modules/  
  
ENV NODE_HOME $HOME/node  
RUN curl -sSL https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz -o $HOME/node.tar.gz && \  
mkdir -p $HOME/node && \  
cd $HOME && tar -C $HOME/node --strip-components 1 -xzf node.tar.gz && \  
rm -f $HOME/node.*  
  
ENV PATH $PATH:$HOME/node/bin  
  
ENV NPM_VERSION=3.7.5  
ENV npm_install=$NPM_VERSION  
RUN curl -L https://npmjs.org/install.sh | sudo sh && \  
mkdir -p $HOME/.npm-user && \  
npm config set prefix '~/.npm-user'  
  
ENV PATH $HOME/.npm-user/bin:$PATH  
  
WORKDIR /src  
  
ENTRYPOINT ["/bin/bash", "--login", "-i", "-c"]  
CMD ["/bin/bash"]

