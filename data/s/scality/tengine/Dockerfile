FROM scality/ironman-base:latest  
ENV HOME=/home/ironman  
  
#------------------------------  
# INSTALL NGINX  
#------------------------------  
  
ENV NGINX_VERSION tengine-2.1.0  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /usr/src/  
  
ADD https://github.com/alibaba/tengine/archive/${NGINX_VERSION}.tar.gz
tengine.tar.gz  
  
RUN sudo apt-get update && \  
sudo apt-get -y install libssl-dev \  
libpcre3-dev \  
zlib1g-dev \  
libgeoip-dev \  
libxslt1-dev \  
libgd2-dev \  
build-essential \  
libc6 \  
libexpat1 \  
libgd2-xpm-dev \  
libgeoip1 \  
libgeoip-dev \  
libpam0g \  
libssl1.0.0 \  
libxml2 \  
libxslt1.1 \  
zlib1g \  
openssl \  
liblua5.1-0-dev \  
lua5.1 \  
libgd2-xpm-dev \  
libgeoip-dev \  
libxslt1-dev \  
libpcre++0 \  
libpcre++-dev \  
libperl-dev \  
wget \  
curl && \  
sudo tar -zxvf tengine.tar.gz && \  
cd tengine-${NGINX_VERSION} && \  
sudo ./configure \  
--enable-mods-static=all \  
--user=ironman \  
--group=ironman \  
--prefix=/home/ironman/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--lock-path=/home/ironman/nginx.lock \  
--pid-path=/home/ironman/nginx.pid \  
--http-client-body-temp-path=/home/ironman/body \  
--http-fastcgi-temp-path=/home/ironman/fastcgi \  
--http-proxy-temp-path=/home/ironman/proxy \  
--http-scgi-temp-path=/home/ironman/scgi \  
--http-uwsgi-temp-path=/home/ironman/uwsgi \  
--with-http_ssl_module \  
--with-http_gzip_static_module \  
--with-http_gunzip_module \  
--with-md5=/usr/include/openssl \  
--with-sha1-asm \  
--with-md5-asm \  
--with-http_auth_request_module \  
--with-http_image_filter_module \  
--with-http_addition_module \  
--with-http_dav_module \  
--with-http_realip_module \  
--with-http_spdy_module \  
--with-http_ssl_module \  
--with-http_stub_status_module \  
--with-http_sub_module \  
--with-http_xslt_module \  
--with-http_upstream_ip_hash_module=shared \  
--with-http_upstream_least_conn_module=shared \  
--with-http_upstream_session_sticky_module=shared \  
--with-http_map_module=shared \  
--with-http_user_agent_module=shared \  
--with-http_mp4_module \  
--with-http_split_clients_module=shared \  
--with-http_access_module=shared \  
--with-http_user_agent_module=shared \  
--with-http_degradation_module \  
--with-http_upstream_check_module \  
--with-http_upstream_consistent_hash_module \  
--with-ipv6 \  
--with-file-aio \  
--with-mail \  
--with-mail_ssl_module \  
--with-pcre \  
--with-pcre-jit \  
--prefix=/etc/nginx \  
--with-debug \  
--http-log-path=/home/ironman/log/access.log \  
--error-log-path=/home/ironman/log/error.log \  
--sbin-path=/usr/sbin/nginx && \  
sudo make && \  
sudo make install && \  
sudo mkdir /etc/nginx/conf.d && \  
sudo mkdir -p /etc/nginx/sites-available && \  
sudo mkdir -p /etc/nginx/sites-enabled && \  
sudo mkdir -p /home/ironman/body && \  
sudo chown -R ironman:ironman /home/ironman/log && \  
sudo chown -R ironman:ironman /etc/nginx/sites-available && \  
sudo chown -R ironman:ironman /etc/nginx/sites-enabled && \  
sudo chown -R ironman:ironman /home/ironman/body && \  
sudo apt-get -y remove build-essential && \  
sudo dpkg --get-selections | awk '{print $1}'|cut -d: -f1|grep -- '-dev$' |
xargs sudo apt-get remove -y && \  
sudo rm -rf /usr/src && \  
sudo apt-get clean all && \  
sudo rm -rf /tmp/*  
  
ADD ./deployment/nginx.conf /etc/nginx/nginx.conf  
ADD ./deployment/fastcgi_params /etc/nginx/fastcgi_params  
VOLUME ["/var/log/nginx"]  
VOLUME ["/var/cache/nginx"]  
WORKDIR $HOME  
EXPOSE 8181  
  
#------------------------------  
# CONFIGURE SUPERVISOR  
#------------------------------  
# see http://supervisord.org/configuration.html  
USER ironman  
COPY ./deployment/supervisord.conf ${HOME}/supervisord.conf  
  
#-------------------------------------  
# DOCKER 1.9  
#-------------------------------------  
# Avoids the message  
# Error response from daemon: client is newer  
# than server (client API version: 1.22, server API version: 1.21)  
# we solve the problem by having the same docker binary  
# in CI and within the docker container  
RUN sudo curl -L -o /usr/bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-1.9.1  
  
  
#-------------------------------------  
# DOCKER STARTUP  
#-------------------------------------  
COPY ./deployment/startDocker.bash ${HOME}/startDocker.bash  
CMD sudo ${HOME}/startDocker.bash  

