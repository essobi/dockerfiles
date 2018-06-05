FROM nginx:1.12.1-alpine-perl  
COPY alpine-patches/*.patch /tmp/  
RUN apk add --no-cache \  
build-base \  
ca-certificates \  
fcgiwrap \  
make \  
openssl \  
perl-carp \  
perl-cgi \  
perl-net-dns \  
perl-uri \  
spawn-fcgi \  
tini \  
wget \  
&& update-ca-certificates \  
&& wget
https://github.com/pacparser/pacparser/releases/download/1.3.7/pacparser-1.3.7.tar.gz
-O pacparser-1.3.7.tar.gz \  
&& sh -c 'tar xzf pacparser-1.3.7.tar.gz && \  
cd pacparser* && \  
cat /tmp/*.patch | patch -p1 && \  
cd src && \  
make && \  
make install' \  
&& apk del --purge \  
build-base \  
ca-certificates \  
make \  
openssl \  
wget \  
&& rm -rf pacparser* /tmp/*.patch  
ENTRYPOINT ["/sbin/tini", "--"]  
COPY nginx-conf/*.conf /etc/nginx/conf.d/  
COPY pactester.cgi /usr/lib/cgi-bin/pactester-cgi/pactester.cgi  
  
CMD ["/bin/sh", "-c", "spawn-fcgi -s /run/fcgiwrap.socket -U nginx -u nginx
/usr/bin/fcgiwrap && exec nginx -g 'daemon off;'"]  
  

