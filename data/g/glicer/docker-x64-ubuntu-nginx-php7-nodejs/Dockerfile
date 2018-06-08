FROM ubuntu:16.04  
MAINTAINER Emmanuel ROECKER <emmanuel.roecker@glicer.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
# install cron ca-certificates, supervisor, nginx, sqlite3  
RUN apt-get install -y cron ca-certificates supervisor nginx sqlite3 curl  
  
# install php 7  
RUN apt-get install -y php7.0 php7.0-fpm php7.0-sqlite3 php7.0-xml php7.0-curl
php7.0-intl php7.0-gd  
  
# install redis  
RUN apt-get install -y redis-server  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 6.10.3  
# install nvm and nodejs  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash &&
\  
source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default  
  
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# set the maximum number of open file descriptors  
RUN echo "ulimit -n 4096" >> /etc/default/redis  
  
# configure projects user, disable service nginx mode & default directories
and delete default nginx site  
RUN useradd -m projects && \  
echo "include /etc/nginx/nginx_shared_core.conf;" >> /etc/nginx/nginx.conf &&
\  
mkdir -p /run/php && mkdir -p /home/projects/www && rm /etc/nginx/sites-
enabled/default  
  
# shared log directory  
VOLUME ["/var/log"]  
  
# Configure Services  
COPY build/start.sh /start.sh  
ENTRYPOINT ["/bin/bash", "/start.sh"]  
  
# Configure ports  
EXPOSE 25 80 443 465  

