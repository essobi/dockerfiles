FROM ubuntu:xenial  
  
EXPOSE 1883  
EXPOSE 9883  
ENV MOSQUITTO_VERSION=v1.4.15  
RUN useradd mosquitto  
  
RUN buildDeps="git build-essential libpq-dev uuid-dev libcurl4-openssl-dev
libwebsockets-dev wget libssl-dev"; \  
apt update && \  
apt install -y $buildDeps libwebsockets7 libpq5 libcurl3&& \  
cd /tmp && \  
wget https://github.com/eclipse/mosquitto/archive/v1.4.15.tar.gz && \  
mkdir mosquitto && \  
tar -xf v1.4.15.tar.gz -C mosquitto --strip-components=1 && \  
cd mosquitto && \  
make WITH_DOCS=no WITH_SRV=no WITH_WEBSOCKETS=yes && \  
make install WITH_DOCS=no && \  
git clone git://github.com/jpmens/mosquitto-auth-plug.git && \  
cd mosquitto-auth-plug && \  
cp config.mk.in config.mk && \  
sed -i "s/BACKEND_POSTGRES ?= no/BACKEND_POSTGRES ?= yes/" config.mk && \  
sed -i "s/BACKEND_HTTP ?= no/BACKEND_HTTP ?= yes/" config.mk && \  
sed -i "s/BACKEND_FILES ?= no/BACKEND_FILES ?= yes/" config.mk && \  
sed -i "s/BACKEND_MYSQL ?= yes/BACKEND_MYSQL ?= no/" config.mk && \  
sed -i "s/MOSQUITTO_SRC =/MOSQUITTO_SRC = ..\//" config.mk && \  
sed -i "s/CFG_CFLAGS =/CFG_CFLAGS = -DRAW_SALT/" config.mk && \  
make && \  
cp auth-plug.so /usr/local/lib/ && \  
cp np /usr/local/bin/ && \  
apt remove -y --purge $buildDeps && apt autoremove -y && rm -rf
/var/cache/apt/* && rm -rf /tmp/*  
  
ADD etc/mosquitto/mosquitto.conf /etc/mosquitto/mosquitto.conf  
  
RUN mkdir -p /etc/mosquitto/mosquitto-auth-plug/ && \  
touch /etc/mosquitto/mosquitto-auth-plug/passwords && \  
touch /etc/mosquitto/mosquitto-auth-plug/acls && \  
chown -R mosquitto /etc/mosquitto/mosquitto-auth-plug  
  
CMD ["mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]  

