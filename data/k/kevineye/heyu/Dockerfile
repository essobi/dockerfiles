FROM alpine  
MAINTAINER Kevin Eye <kevineye@gmail.com>  
  
RUN apk -U add curl build-base \  
&& mkdir /build \  
&& cd /build \  
&& curl -LsSO
http://github.com/msoap/shell2http/releases/download/1.4/shell2http-1.4.amd64.linux.zip
\  
&& echo 'd0c00a5a0e6ecf664ad865f2e949cf1d8ca2b4b7
*shell2http-1.4.amd64.linux.zip' | sha1sum -c - \  
&& unzip shell2http-1.4.amd64.linux.zip shell2http \  
&& mv shell2http /usr/local/bin \  
&& curl -LsSO http://www.heyu.org/download/heyu-2.11-rc1.tar.gz \  
&& echo 'f02fa53b866343f05d57a2ac87c7f7b39c786295 *heyu-2.11-rc1.tar.gz' |
sha1sum -c - \  
&& tar xzf heyu-2.11-rc1.tar.gz \  
&& cd heyu-2.11-rc1 \  
&& ./configure --sysconfdir=/etc \  
&& make \  
&& make install \  
&& cd / \  
&& apk --purge del curl build-base \  
&& rm -rf /build /etc/ssl /var/cache/apk/* /lib/apk/db/*  
  
RUN cp -r /etc/heyu /etc/heyu.default \  
&& mkdir -p /usr/local/var/tmp/heyu \  
&& mkdir -p /usr/local/var/lock \  
&& chmod 777 /usr/local/var/tmp/heyu \  
&& chmod 777 /usr/local/var/lock  
  
VOLUME /etc/heyu  
EXPOSE 80  
COPY heyu-run.sh /usr/local/bin/heyu-run  
CMD heyu-run  

