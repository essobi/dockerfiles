FROM gliderlabs/alpine:3.3  
MAINTAINER dominic.kim@navercorp.com  
  
## Install prerequisites  
RUN apk-install gcc g++ make perl binutils tar  
  
WORKDIR /root  
  
## Download stable version of squid source  
RUN wget http://www.squid-cache.org/Versions/v3/3.5/squid-3.5.26.tar.gz; \  
tar xvf squid-3.5.26.tar.gz; \  
rm -rf squid-3.5.26.tar.gz  
  
WORKDIR /root/squid-3.5.26  
  
## Add retry-delay on connection error  
RUN sed -i 's/#include <cerrno>/#include <cerrno>\n#include <unistd.h>/g'
src/comm/ConnOpener.cc  
RUN sed -i 's/debugs(5, 5, HERE << conn_ << "\: \\* - try again");/debugs(5,
5, HERE << conn_ << ": * - try again");\n sleep(7);/g' src/comm/ConnOpener.cc  
  
RUN ./configure \  
\--prefix=/usr \  
\--includedir=/usr/include \  
\--datadir=/usr/share \  
\--bindir=/usr/sbin \  
\--libexecdir=/usr/lib/squid \  
\--localstatedir=/var \  
\--sysconfdir=/etc/squid \  
\--with-default-user=proxy \  
&& make \  
&& make install  
  
ENV SQUID_USER=proxy \  
SQUID_CACHE_DIR=/var/spool/squid \  
SQUID_RUN_DIR=/var/run \  
SQUID_CACHE_LOG_DIR=/var/logs \  
SQUID_ACCESS_LOG_DIR=/var/log/squid \  
SQUID_SWAP_DIR=/var/cache/squid  
  
RUN addgroup -S ${SQUID_USER} && adduser -S -g ${SQUID_USER} ${SQUID_USER}  
  
COPY squid.conf /etc/squid/squid.conf  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
RUN mkdir -p ${SQUID_ACCESS_LOG_DIR} \  
&& mkdir -p ${SQUID_CACHE_DIR} \  
&& mkdir -p ${SQUID_SWAP_DIR} \  
&& chown -R ${SQUID_USER}:${SQUID_USER} ${SQUID_ACCESS_LOG_DIR} \  
&& chown -R ${SQUID_USER}:${SQUID_USER} ${SQUID_CACHE_LOG_DIR} \  
&& chown -R ${SQUID_USER}:${SQUID_USER} ${SQUID_CACHE_DIR} \  
&& chown -R ${SQUID_USER}:${SQUID_USER} ${SQUID_SWAP_DIR} \  
&& chown -R ${SQUID_USER}:${SQUID_USER} ${SQUID_RUN_DIR}  
  
USER $SQUID_USER  
EXPOSE 3128/tcp  
CMD ["/sbin/entrypoint.sh"]  

