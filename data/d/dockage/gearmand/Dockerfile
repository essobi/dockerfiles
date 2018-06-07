FROM dockage/alpine:3.5  
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>  
  
ENV GEARMAND_VERSION=1.1.15 \  
GEARMAN_USER=gearman \  
GEARMAN_GROUP=gearman \  
DOCKAGE_ETC_DIR=/etc/dockage  
  
ENV GEARMAN_HOME=/var/lib/${GEARMAN_USER}  
  
ADD
https://github.com/gearman/gearmand/releases/download/${GEARMAND_VERSION}/gearmand-${GEARMAND_VERSION}.tar.gz
/  
ADD ./assets ${DOCKAGE_ETC_DIR}  
  
RUN apk update \  
&& apk --no-cache add g++ libc-dev boost-dev gperf libevent-dev util-linux-dev
hiredis-dev libressl-dev sqlite-dev libmemcached-dev \  
&& ${DOCKAGE_ETC_DIR}/buildtime/install \  
&& mv ${DOCKAGE_ETC_DIR}/sbin/* /sbin \  
&& rm -rf /var/cache/apk/* ${DOCKAGE_ETC_DIR}/sbin
${DOCKAGE_ETC_DIR}/buildtime  
  
EXPOSE 4730/tcp  
  
ENTRYPOINT ["/sbin/entrypoint"]  
CMD ["gearmand:start"]  

