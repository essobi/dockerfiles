FROM hence/base:3.4-onbuild  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ENV HENCE_APP_NAME=nginx \  
HENCE_APP_USER=hence \  
HENCE_APP_VERSION=3.4  
ENV HENCE_APP_DIR=$HENCE_PREFIX/$HENCE_APP_NAME \  
HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME  
  
ENV PATH=$HENCE_APP_DIR/sbin:$HENCE_PREFIX/common/bin:$PATH  
  
RUN apk add --update \  
openssl \  
nginx && \  
rm -rf /var/cache/apk/* && \  
rm -rf /etc/nginx/* && \  
chown -R $HENCE_APP_USER:$HENCE_APP_USER /var/lib/nginx && \  
chsh -s /bin/bash $HENCE_APP_USER  
  
COPY rootfs /  
  
RUN sh $HENCE_PREFIX/install.sh && \  
s6-rmrf /etc/s6/services/s6-fdholderd/down  
  
EXPOSE 80 443  
VOLUME ["/etc/nginx/custom.d", "/app", "$HENCE_APP_VOL_PREFIX/conf",
"$HENCE_APP_VOL_PREFIX/logs/nginx-access-logs",
"$HENCE_APP_VOL_PREFIX/logs/nginx-error-logs"]  
  
WORKDIR /app  

