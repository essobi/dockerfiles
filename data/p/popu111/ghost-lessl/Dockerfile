######################################  
# Docker Ghost Onekey Installer #  
# With Let's Encypt #  
# By boboLiu <admin@boboweb.net> #  
######################################  
FROM debian:8  
MAINTAINER boboLiu <admin@boboweb.net>  
  
#Install ssh and others  
RUN mkdir -p /app/ghost /app/nginx-src /app/nginx /home/cache/temp
/home/cache/path /app/node  
RUN apt-get update -y && apt-get upgrade -y && apt-get -y install openssh-
server pwgen gcc make unzip supervisor wget git patch libpcre3 libpcre3-dev
zlib1g-dev zlib1g  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
#Get Ghost  
ENV GHOST_VERSION 0.7.8  
RUN wget https://ghost.org/zip/ghost-$GHOST_VERSION.zip -O
/app/ghost/ghost.zip  
RUN cd /app/ghost && unzip ghost.zip && rm -f ghost.zip  
  
#Get Nginx  
ENV NGINX_VERSION 1.9.12  
RUN wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -O /app/nginx-
src/nginx.tar.gz && \  
cd /app/nginx-src && \  
tar xf nginx.tar.gz && \  
mv nginx-$NGINX_VERSION/* ./ && \  
rm -f nginx.tar.gz  
  
#Get modules  
RUN cd /app/nginx-src && \  
git clone https://github.com/FRiCKLE/ngx_cache_purge.git && do=do && \  
git clone https://github.com/popu125/ngx_cache_status_module.git  
  
#Install Node  
ENV NODE_VERSION 4.4.1  
RUN cd /app/node && wget
http://nodejs.org/dist/latest-v4.x/node-v${NODE_VERSION}-linux-x64.tar.gz -O
node.tar.gz && tar xf node.tar.gz && mv node-v${NODE_VERSION}-linux-x64/* ./
&& rm -rf node.tar.gz node-v${NODE_VERSION}-linux-x64 && ln -s
/app/node/bin/node /usr/bin/node && ln -s /app/node/bin/npm /usr/bin/npm && ln
-s /app/node/lib/node_modules /usr/lib/node_modules  
RUN cd /app/ghost && npm install -g forever && npm install --production  
  
#Install OpenSSL (1.0.2g now)  
ENV OPENSSL_VERSION 1.0.2g  
RUN wget http://openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz -O
/app/openssl.tar.gz && \  
wget
https://github.com/cloudflare/sslconfig/raw/master/patches/openssl__chacha20_poly1305_draft_and_rfc_ossl102g.patch
-O /app/ssl.patch  
RUN cd /app && \  
apt-get remove openssl -y && \  
tar xf openssl.tar.gz && rm -f openssl.tar.gz && \  
mv openssl-* ssl && \  
cd ssl && \  
patch -p1 < ../ssl.patch  
RUN cd /app/ssl && ./config --prefix=/usr/local threads shared no-zlib no-comp
no-ssl2 no-ssl3 no-ssl3-method && \  
make depend && make && make install && \  
rm -f /usr/bin/openssl /usr/include/openssl && \  
ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl && ln -s
/usr/local/openssl/include/openssl /usr/include/openssl && \  
echo "/usr/local/openssl/lib" >> /etc/ld.so.conf && ldconfig -v  
  
#Install Nginx  
RUN cd /app/nginx-src && \  
./configure --prefix=/app/nginx --add-module=./ngx_cache_purge --add-
module=./ngx_cache_status_module --with-http_ssl_module --with-http_v2_module
&& \  
make && make install  
  
#Set Nginx  
ADD nginx.conf /app/nginx/conf/nginx.conf  
  
#Set Supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisor.conf /etc/supervisor/conf.d/supervisord.conf  
  
#Set Let's Encypt  
RUN mkdir /app/le && cd /app/le && \  
wget https://raw.githubusercontent.com/diafygi/acme-tiny/master/acme_tiny.py
&& \  
wget https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem -O
intermediate.pem  
ADD le.sh /app/le/le.sh  
  
#Add scripts to root dictory  
ADD passwd.sh /passwd.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
#Set ENV  
ENV DOMAIN bobiji.com  
ENV HSTS Y  
ENV LESSL Y  
ENV ROOT_PASS root  
  
#The End  
EXPOSE 22 80 443  
CMD ["/bin/bash","/run.sh"]  

