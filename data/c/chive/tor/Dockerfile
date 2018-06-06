FROM alpine:3.2  
MAINTAINER Chive <kim@smuzey.ch>  
  
ENV TOR_VERSION tor-0.2.6.10  
RUN apk --update add --virtual build-dependencies curl make gcc musl-dev
openssl-dev libevent-dev \  
&& curl https://dist.torproject.org/${TOR_VERSION}.tar.gz | tar xz -C /tmp \  
&& cd /tmp/${TOR_VERSION} \  
&& ./configure \  
&& make \  
&& make install \  
&& cd /tmp \  
&& rm -rf /tmp/${TOR_VERSION} \  
&& apk del build-dependencies \  
&& apk add libevent \  
&& ntpd -d -q -n -p pool.ntp.org  
  
ADD ./torrc /etc/torrc  
  
EXPOSE 9150  
CMD /usr/local/bin/tor -f /etc/torrc  

