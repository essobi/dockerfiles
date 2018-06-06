FROM ubuntu-debootstrap:14.04  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV LIBRARIES_VERSION 8.0.1  
ENV SCANNER_VERSION 5.0.1  
ENV MANAGER_VERSION 6.0.1  
ENV ASSISTANT_VERSION 6.0.1  
  
RUN apt-get update && apt-get dist-upgrade -yq && \  
apt-get install -yq rsync libhiredis-dev build-essential devscripts dpatch
libassuan-dev \  
libglib2.0-dev libgpgme11-dev libpcre3-dev libpth-dev libwrap0-dev libgmp-dev
libgmp3-dev \  
libgpgme11-dev libopenvas2 libpcre3-dev libpth-dev quilt cmake pkg-config \  
libssh-dev libglib2.0-dev libpcap-dev libgpgme11-dev uuid-dev bison libksba-
dev \  
doxygen sqlfairy xmltoman sqlite3 libsqlite3-dev wamerican rsyslog redis-
server \  
libmicrohttpd-dev libxml2-dev libxslt1-dev xsltproc libssh2-1-dev libldap2-dev
autoconf nmap libgnutls-dev supervisor && \  
apt-get clean && \  
export CMAKE_OPT="-DCMAKE_INSTALL_PREFIX=/usr -DLOCALSTATEDIR=/var" && \  
mkdir -p /usr/src/build/libraries && cd /usr/src/build/libraries && \  
curl http://wald.intevation.org/frs/download.php/2015/openvas-
libraries-${LIBRARIES_VERSION}.tar.gz | tar zxv \--strip-components=1 && \  
mkdir -p build && cd build && cmake ${CMAKE_OPT} .. && make install && \  
mkdir -p /usr/src/build/scanner && cd /usr/src/build/scanner && \  
curl http://wald.intevation.org/frs/download.php/2016/openvas-
scanner-${SCANNER_VERSION}.tar.gz | tar zxv \--strip-components=1 && \  
mkdir -p build && cd build && cmake ${CMAKE_OPT} .. && make install && \  
mkdir -p /usr/src/build/manager && cd /usr/src/build/manager && \  
curl http://wald.intevation.org/frs/download.php/2017/openvas-
manager-${MANAGER_VERSION}.tar.gz | tar zxv \--strip-components=1 && \  
mkdir -p build && cd build && cmake ${CMAKE_OPT} .. && make install && \  
mkdir -p /usr/src/build/assistant && cd /usr/src/build/assistant && \  
curl http://wald.intevation.org/frs/download.php/1018/greenbone-security-
assistant-${ASSISTANT_VERSION}.tar.gz | tar zxv \--strip-components=1 && \  
mkdir -p build && cd build && cmake ${CMAKE_OPT} .. && make install && \  
echo "unixsocket /tmp/redis.sock" >> /etc/redis/redis.conf && \  
sed -i 's#daemonize yes#daemonize no#g' /etc/redis/redis.conf  
  
ADD resources/supervisord.conf /etc/supervisor/supervisord.conf  
ADD bin/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
RUN /usr/local/bin/setup.sh  
# UI + Scanner ports  
EXPOSE 443 9390 9391  
  
CMD ["/usr/local/bin/run"]  

