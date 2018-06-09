FROM ubuntu:14.04.3  
  
MAINTAINER SimPhoNy Team  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends supervisor \  
openssh-server pwgen sudo vim-tiny \  
net-tools \  
lxde x11vnc xvfb \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
wget \  
python-pip python-dev build-essential \  
mesa-utils libgl1-mesa-dri \  
gettext \  
\  
# packages needed for building nginx  
libpcre++-dev libpcre++0 libxml2 libxml2-dev \  
libxslt1-dev libxslt1.1 libgd-dev libgd2-xpm-dev \  
libgeoip-dev libgeoip1 libperl-dev libssl-dev \  
gxmessage \  
\  
&& apt-get autoclean \  
&& apt-get autoremove  
  
# In order to have auth_request support, we need nginx >= 1.5.4  
# But the nginx from the ubuntu prebuilt is 1.4.6  
# So we need to build it from source  
RUN wget http://nginx.org/download/nginx-1.10.0.tar.gz \  
&& tar xfz nginx-1.10.0.tar.gz \  
&& cd nginx-1.10.0 \  
&& ./configure \  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--with-debug \  
--with-pcre-jit \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_mp4_module \  
--with-http_geoip_module \  
--with-http_image_filter_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_xslt_module \  
--with-http_auth_request_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-file-aio \  
--with-ipv6 \  
&& make \  
&& make install \  
&& cd ../ \  
&& rm -rf nginx-1.10.0*  
  
# Make directories needed for nginx  
RUN mkdir -p /var/cache/nginx/uwsgi_temp \  
/var/cache/nginx/fastcgi_temp \  
/var/cache/nginx/proxy_temp \  
/var/cache/nginx/client_temp \  
/etc/nginx/sites-enabled/  
  
LABEL eu.simphony-project.docker.type="webapp" \  
eu.simphony-project.docker.env.user="" \  
eu.simphony-project.docker.env.jpy-user="" \  
eu.simphony-project.docker.env.jpy-base-user-url="" \  
eu.simphony-project.docker.env.url-id=""  
  
COPY container-files/ /  
  
WORKDIR /root  
  
# These are required for the remote access to the docker container  
EXPOSE 8888  
ENTRYPOINT ["/startup.sh"]  

