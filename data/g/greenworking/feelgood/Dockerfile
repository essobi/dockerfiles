FROM fridus/docker-rvm-nvm  
MAINTAINER Alexandre Chakroun <alexandre.chakroun@greenworking.com>  
  
ENV NODE_VERSION 6.9.5  
ENV RUBY_VERSION 2.3.0  
ENV NVM_DIR /root/.nvm  
ENV NPM_DIR /opt/deps  
  
RUN sudo apt-get update  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-key adv --keyserver pgp.mit.edu --recv-keys 5072E1F5 && \  
wget http://dev.mysql.com/get/mysql-apt-config_0.8.1-1_all.deb && \  
dpkg -i mysql-apt-config_0.8.1-1_all.deb && \  
apt-get update && \  
apt install -y mysql-client libmysqlclient-dev libgmp3-dev mysql-server  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN service mysql start && \  
mysql -u root -e "CREATE DATABASE feelgood_test" && \  
mysql -u root -e "CREATE USER 'test'@'localhost' IDENTIFIED BY 'test';" && \  
mysql -u root -e "GRANT ALL PRIVILEGES ON * . * TO 'test'@'localhost';" && \  
mysql -u root -e "FLUSH PRIVILEGES;"  
  
COPY feelgood-front /tmp/feelgood-front/  
  
RUN source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default && \  
cd /tmp/feelgood-front/user && npm install && \  
cd /tmp/feelgood-front/admin && npm install  
  
RUN mkdir -p $NPM_DIR/feelgood-front/user/ && \  
mkdir -p $NPM_DIR/feelgood-front/admin/ && \  
cp -r /tmp/feelgood-front/user/node_modules $NPM_DIR/feelgood-front/user/ && \  
cp -r /tmp/feelgood-front/admin/node_modules $NPM_DIR/feelgood-front/admin/  
  
RUN /bin/bash -l -c "rvm requirements" && \  
/bin/bash -l -c "rvm install $RUBY_VERSION"  
  
COPY feelgood-back /tmp/feelgood-back/  
  
RUN /bin/bash -l -c "cd /tmp/feelgood-back/ && rvm use $RUBY_VERSION && gem
install bundler --no-ri --no-rdoc && bundle"  
  
RUN rm -rf /tmp/*  
  
ENTRYPOINT /bin/bash  

