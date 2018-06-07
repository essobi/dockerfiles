FROM debian:stretch  
  
RUN apt-get update && \  
apt-get install -yqq \  
curl \  
gnupg && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y \  
nodejs \  
nginx \  
build-essential \  
gettext-base \  
git  
  
RUN rm -rf /var/log/nginx/*.log && \  
ln -s /dev/stderr /var/log/nginx/error.log && \  
ln -s /dev/stdout /var/log/nginx/access.log  

