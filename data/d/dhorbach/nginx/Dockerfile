FROM dhorbach/base  
  
MAINTAINER Dzmitry Horbach  
  
ENV NGINX_VERSION 1.7.8  
ENV STICKY_VERSION 1.2.5  
WORKDIR /opt  
  
RUN wget -nv -O - http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz | tar
zx  
RUN wget -nv -O - https://bitbucket.org/nginx-goodies/nginx-sticky-module-
ng/get/$STICKY_VERSION.tar.gz | tar zx  
RUN mv nginx-goodies* nginx-goodies-$STICKY_VERSION  
RUN apt-get update && \  
apt-get install -y build-essential zlib1g-dev libpcre3-dev libssl-dev
libxslt1-dev libxml2-dev libgd2-xpm-dev libgeoip-dev libperl-dev  
  
WORKDIR /opt/nginx-$NGINX_VERSION  
  
RUN ./configure --prefix=/usr/local/nginx --sbin-path=/usr/local/sbin/nginx
--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log --http-log-
path=/var/log/nginx/access.log --pid-path=/run/nginx.pid --lock-
path=/run/lock/subsys/nginx \  
\--user=nginx --group=nginx --add-module=/opt/nginx-goodies-$STICKY_VERSION \  
\--with-http_gzip_static_module --with-http_stub_status_module --with-
http_ssl_module \  
\--with-pcre --with-file-aio --with-http_realip_module --without-
http_scgi_module --without-http_uwsgi_module  
RUN make  
RUN make install  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /etc/nginx/conf.d  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
WORKDIR /etc/nginx  
  
RUN useradd -r nginx  
  
CMD ["nginx"]  
  
EXPOSE 80  
EXPOSE 443  

