FROM debian:jessie  
  
ENV APP_CWD='/app/code' \  
APP_USER='application' \  
APP_GROUP='application' \  
VHOST_ROOT='/app/code' \  
VHOST_INDEX='index.html' \  
NODE_VERSION='6.9.1' \  
NPM_VERSION='index.html'  
  
COPY . /docker  
  
RUN apt-get update && apt-get install git vim wget curl -y && \  
cat /docker/sources.list >> /etc/apt/sources.list && \  
wget http://nginx.org/packages/keys/nginx_signing.key && \  
cat nginx_signing.key | apt-key add \- && \  
/bin/bash /docker/installnodejs4.sh && \  
apt-get update && apt-get install nginx nodejs bzip2 -y && apt-get clean &&
apt-get autoclean && apt-get autoremove  
  
# NODEJS 4.4.3 NPM >= 3.8.9  
  
RUN /usr/bin/npm update -g npm && \  
/usr/bin/npm install -g n && \  
/usr/bin/n $NODE_VERSION && \  
/bin/mv /usr/bin/node /usr/bin/node.old && \  
/bin/cp /usr/local/n/versions/node/$NODE_VERSION/bin/node /usr/bin/node && \  
/bin/mv /usr/local/bin/npm /usr/local/bin/npm.2.15.1 && \  
/bin/ln -s /usr/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm  
  
#expose ports  
EXPOSE 80 443  
  
ENTRYPOINT ["bash", "/docker/scripts/entrypoint.sh"]  
CMD ["start-nginx"]

