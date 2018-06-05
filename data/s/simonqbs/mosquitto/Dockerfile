FROM debian:jessie  
  
ENV MOSQUITTO_VERSION=1.4.5  
RUN \  
set -x; \  
apt-get update && apt-get install -y --no-install-recommends \  
libc-ares-dev git libmysqlclient-dev libssl-dev uuid-dev build-essential wget
ca-certificates \  
&& cd /tmp \  
&& wget http://mosquitto.org/files/source/mosquitto-$MOSQUITTO_VERSION.tar.gz
-O mosquitto.tar.gz \  
&& wget
http://mosquitto.org/files/source/mosquitto-$MOSQUITTO_VERSION.tar.gz.asc -O
mosquitto.tar.gz.asc \  
&& gpg --keyserver pgp.mit.edu --recv B3E717B7 \  
&& gpg --verify mosquitto.tar.gz.asc \  
&& mkdir mosquitto-src && tar xfz mosquitto.tar.gz --strip-components=1 -C
mosquitto-src \  
&& cd mosquitto-src && make && make install && ldconfig \  
&& git clone https://github.com/jpmens/mosquitto-auth-plug.git \  
&& cd mosquitto-auth-plug \  
&& cp config.mk.in config.mk \  
&& echo "MOSQUITTO_SRC = /tmp/mosquitto-src" >> config.mk \  
&& make \  
&& cp np /usr/bin/np \  
&& mkdir /mqtt && cp auth-plug.so /mqtt/ \  
&& useradd -r mosquitto \  
&& apt-get purge -y build-essential git wget ca-certificates \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
VOLUME ["/var/lib/mosquitto"]  
  
EXPOSE 1883 9001  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["mosquitto"]  

