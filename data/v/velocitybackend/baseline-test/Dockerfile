FROM ubuntu:16.04  
MAINTAINER backend@velocityapp.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEPLOY_MODE test  
ENV NODE_ENV test  
ENV NVM_DIR /usr/local/nvm  
ENV NVM_VERSION 0.33.6  
ENV NODE_VERSION 6.12.0  
ENV PORT 8000  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
RUN ln -sf /bin/bash /bin/sh  
  
# Set debconf to run non-interactively  
RUN export DEBIAN_FRONTEND=noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install base dependencies  
RUN apt-get update -y -q && \  
apt-get upgrade -y -q && \  
apt-get install -y -q --no-install-recommends \  
apt-transport-https \  
apt-utils \  
build-essential \  
ca-certificates \  
curl \  
git \  
libssl-dev \  
python \  
pwgen \  
rpl \  
rsync \  
wget  
  
# Install MySQL  
RUN apt-get install -y -q --no-install-recommends mysql-server mysql-client  
VOLUME /var/lib/mysql  
  
# CleanUp Apt Cache  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV DATABASE_NAME test_database  
ENV DATABASE_URL mysql://root@localhost/$DATABASE_NAME  
RUN service mysql start && \  
mysql -h localhost --user=root -e "CREATE DATABASE $DATABASE_NAME CHARACTER
SET utf8mb4; FLUSH PRIVILEGES;" && \  
service mysql stop  
  
# Exclude the NPM cache from the image  
VOLUME /root/.npm  
  
RUN mkdir -p /usr/src/app/  
WORKDIR /usr/src/app  
  
# Install nvm with node and npm, then migrate the local database  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
ENV DEBIAN_FRONTEND ""  
# Open port 3306 for mysql, 8000 for the app  
EXPOSE 3306  
EXPOSE 8000  

