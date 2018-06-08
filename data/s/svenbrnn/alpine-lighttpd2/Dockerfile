FROM alpine:3.7  
RUN apk add --no-cache --update gcc g++ glib glib-dev make libtool automake
autoconf libev libev-dev lua-dev ragel glib lua zlib zlib-dev libbz2 libssl1.0
openssl-dev && \  
wget
http://git.lighttpd.net/lighttpd/lighttpd2.git/snapshot/lighttpd2-master.tar.gz
&& \  
tar xfvz lighttpd2-master.tar.gz && \  
cd lighttpd2-master && \  
./autogen.sh && \  
./configure --with-lua --with-openssl --with-kerberos5 --with-zlib --with-
bzip2 --includedir=/usr/include/lighttpd-2.0.0 && \  
make && \  
make install && \  
cd .. && rm -rf lighttpd2-master* && \  
apk del gcc g++ glib-dev make libtool automake autoconf libev-dev lua-dev
zlib-dev openssl-dev && \  
adduser -D www-data  
  
COPY ./conf /etc/lighttpd2  
  
VOLUME ["/etc/lighttpd2"]  
VOLUME ["/var/www"]  
  
WORKDIR /var/www  
  
EXPOSE 80  
ENTRYPOINT ["lighttpd2", "-c", "/etc/lighttpd2/angel.conf"]  

