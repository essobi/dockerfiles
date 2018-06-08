FROM shift/ubuntu:15.04  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
WORKDIR /usr/local/src  
RUN apt-get update \  
&& apt-get install --no-install-recommends --yes build-essential curl git-core
libssl-dev libpcre3-dev python-pip \  
&& pip install elasticsearch \  
&& curl -L -O http://nginx.org/download/nginx-1.8.0.tar.gz \  
&& curl -L -O https://github.com/nbs-system/naxsi/archive/0.54rc3.tar.gz \  
&& tar xfvz nginx-1.8.0.tar.gz \  
&& tar xfvz 0.54rc3.tar.gz \  
&& cd nginx-1.8.0 \  
&& ./configure --prefix=/usr --add-module=../naxsi-0.54rc3/naxsi_src/ \--conf-
path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-
client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-
path=/var/lib/nginx/fastcgi --http-log-path=/var/log/nginx/access.log --http-
proxy-temp-path=/var/lib/nginx/proxy --lock-path=/var/lock/nginx.lock --pid-
path=/var/run/nginx.pid --with-http_ssl_module --without-mail_pop3_module
--without-mail_smtp_module --without-mail_imap_module --without-
http_uwsgi_module --without-http_scgi_module --with-ipv6 --with-
http_spdy_module --with-http_gunzip_module --with-http_gzip_static_module
--with-http_auth_request_module \  
&& make \  
&& make install \  
&& cd .. \  
&& cd naxsi-0.54rc3/nxapi \  
&& python setup.py install \  
&& cd .. \  
&& rm -rf nginx-1.8.0 nginx-1.8.0.tar.gz 0.54rc3.tar.gz \  
&& apt-get remove --yes build-essential \  
&& apt-get autoremove --yes \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /etc/nginx  
VOLUME /var/log/nginx  
VOLUME /var/lock  
VOLUME /var/run  
VOLUME /var/lib/nginx/fastcgi  
  
EXPOSE 80/tcp  
EXPOSE 443/tcp  

