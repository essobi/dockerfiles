FROM hence/base:3.2-onbuild  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ENV HENCE_APP_NAME=memcached \  
HENCE_APP_USER=hence \  
HENCE_APP_VERSION=3.2  
ENV HENCE_APP_DIR=$HENCE_PREFIX/$HENCE_APP_NAME \  
HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME  
  
RUN apk add --update \  
memcached \  
libmemcached && \  
rm -rf /var/cache/apk/*  
  
COPY rootfs /  
  
RUN sh $HENCE_PREFIX/install.sh && \  
s6-rmrf /etc/s6/services/s6-fdholderd/down  
  
EXPOSE 11211  
VOLUME ["$HENCE_APP_VOL_PREFIX/data", "$HENCE_APP_VOL_PREFIX/logs/memcached-
general-logs", "$HENCE_APP_VOL_PREFIX/logs/memcached-error-logs"]  

