FROM debian:7.9  
MAINTAINER Akel <Akel@domain.tld>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update  
RUN apt-get -y install build-essential ffmpeg gcc libpcre3-dev libssl-dev wget
nano mc  
  
WORKDIR /usr/local/src  
  
RUN wget -O /usr/local/src/nginx.tar.gz
http://nginx.org/download/nginx-1.9.9.tar.gz  
RUN wget --no-check-certificate -O /usr/local/src/nginx-rtmp-module.zip
https://github.com/arut/nginx-rtmp-module/archive/master.zip  
  
RUN tar -xzvf /usr/local/src/nginx.tar.gz  
RUN unzip /usr/local/src/nginx-rtmp-module.zip  
  
WORKDIR /usr/local/src/nginx-1.9.9  
  
RUN ./configure \  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--user=root \  
--group=root \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_mp4_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-file-aio \  
--add-module=/usr/local/src/nginx-rtmp-module-master \  
--with-ipv6  
RUN make -j4 && make install  
  
COPY templates/nginx.conf /etc/nginx/nginx.conf  
COPY start.sh /root/start.sh  
  
RUN chmod +x /root/start.sh  
  
ENV HOME /root  
  
WORKDIR /root  
  
EXPOSE 80 1935  
  
ENTRYPOINT ["/root/start.sh"]  

