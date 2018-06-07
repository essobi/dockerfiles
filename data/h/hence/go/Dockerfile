FROM hence/base:3.2-onbuild  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ENV HENCE_APP_NAME=go \  
HENCE_APP_USER=hence \  
HENCE_APP_VERSION=3.2  
ENV HENCE_APP_DIR=$HENCE_PREFIX/$HENCE_APP_NAME \  
HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME  
  
RUN apk --update add \  
go \  
bzr \  
git && \  
rm -rf /var/cache/apk/*  
  
COPY rootfs /  
  
ENV GOPATH=/go \  
PATH=$GOPATH/bin:/usr/src/go/bin:$PATH  
  
RUN sh $HENCE_PREFIX/install.sh && \  
s6-rmrf /etc/s6/services/s6-fdholderd/down  
  
EXPOSE 8000  
VOLUME [/app, "$HENCE_APP_VOL_PREFIX/logs/go-general-logs",
"$HENCE_APP_VOL_PREFIX/logs/go-error-logs"]  
  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  

