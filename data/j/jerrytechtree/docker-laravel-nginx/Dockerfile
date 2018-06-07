FROM jerrytechtree/docker-laravel-base  
MAINTAINER Jerry Zhang "jerry_techtree@126.com"  
ENV REFRESHED_AT 2016-02-03  
ENV SOFTWARE_DIR /software  
ENV NGINX_VERSION 1.9.10  
ENV NGINX_TAR_FILENAME nginx-$NGINX_VERSION.tar.gz  
ENV NGINX_DOWNLOAD_URL http://nginx.org/download/$NGINX_TAR_FILENAME  
ENV NGINX_TAR_FILE $SOFTWARE_DIR/$NGINX_TAR_FILENAME  
ENV NGINX_SOURCE_DIR $SOFTWARE_DIR/nginx  
  
# install dependencies  
RUN apt-get update && apt-get install -y \  
gcc \  
g++ \  
make \  
curl \  
zlib1g-dev \  
libpcre3 \  
libpcre3-dev \  
libssl-dev  
  
# download nginx  
RUN echo $NGINX_DOWNLOAD_URL  
RUN mkdir -p $SOFTWARE_DIR && \  
curl -L $NGINX_DOWNLOAD_URL > $NGINX_TAR_FILE && \  
tar -zxvf $NGINX_TAR_FILE -C $SOFTWARE_DIR && \  
mv $SOFTWARE_DIR/nginx-$NGINX_VERSION $NGINX_SOURCE_DIR  
  
# add user & group  
RUN groupadd -r www && \  
useradd -M -s /sbin/nologin -r -g www www  
  
# install nginx  
RUN cd /software/nginx && \  
./configure --prefix=/usr/local/nginx \  
\--sbin-path=/usr/local/sbin \  
\--conf-path=/etc/nginx/nginx.conf \  
\--user=www --group=www \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--with-pcre \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--without-mail_pop3_module \  
\--without-mail_imap_module && \  
make && make install  
  
# copy configure  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/website.conf /etc/nginx/conf.d/  
  
RUN apt-get clean \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /software  
  
VOLUME ["/var/log/nginx"]  
  
EXPOSE 80  
ENTRYPOINT [ "nginx" ]  

