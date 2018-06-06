FROM ubuntu:16.04  
LABEL \  
maintainer="mickare"  
  
ENV \  
TURN_REALM=localhost  
  
RUN apt-get update -qq  
  
# Build environment  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
wget git \  
build-essential \  
cmake \  
python \  
ca-certificates \  
gettext-base  
  
# Dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
sqlite3 libsqlite3-dev \  
libssl-dev \  
libpq-dev \  
libmysqlclient-dev \  
libmongoc-dev libmongoc-1.0-0 \  
libbson-1.0-0 libbson-dev \  
libhiredis-dev \  
libevent-dev libevent-2.0-5  
  
WORKDIR /root  
  
RUN git clone https://github.com/coturn/coturn.git /root/coturn  
  
ADD *.sh /root/  
RUN chmod +x /root/*.sh  
RUN sh /root/setup.sh  
  
ADD turnserver.conf /etc/  
  
EXPOSE 3478  
CMD sh /root/start.sh

