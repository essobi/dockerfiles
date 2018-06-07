FROM ubuntu:12.04  
RUN apt-get update \  
&& apt-get install -y curl build-essential libpcre3-dev zlib1g-dev
liblua5.1-dev  
  
RUN curl
http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-1.4.35.tar.gz -o
/usr/src/lighttpd-1.4.35.tar.gz && \  
cd /usr/src && \  
tar -zxvf lighttpd-1.4.35.tar.gz  
  
RUN curl https://www.openssl.org/source/old/1.0.1/openssl-1.0.1i.tar.gz -o
/usr/src/openssl-1.0.1i.tar.gz && \  
cd /usr/src && \  
tar -zxvf openssl-1.0.1i.tar.gz  
  
WORKDIR /usr/src/openssl-1.0.1i  
  
RUN CFLAGS=-fPIC ./config shared --prefix=/usr/local/openssl \  
&& make install  
  
WORKDIR /usr/src/lighttpd-1.4.35  
  
RUN ./configure --prefix=/usr/local/lighttpd --with-zlib --without-bzip2
--with-openssl=/usr/local/openssl --with-pcre --with-lua \  
&& make install  
  
RUN apt-get remove -y build-essential libpcre3-dev zlib1g-dev liblua5.1-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN /bin/bash -c "mkdir -p /var/www/{logs,var} && chown www-data:www-data
/var/www/{logs,var}"  
  
ENTRYPOINT ["/usr/local/lighttpd/sbin/lighttpd", "-f",
"/etc/lighttpd/lighttpd.conf", "-D"]  

