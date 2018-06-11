FROM alpine:3.7  
ARG VARNISH_VERSION=5.2.1-r0  
ARG MODULE_VERSION=0.13.0  
LABEL maintainer="Peter Golm <golm.peter@gmail.com>" \  
varnish.version=$VARNISH_VERSION \  
varnish_module.version=$MODULE_VERSION  
  
# install Varnish  
RUN \  
apk update && \  
apk upgrade && \  
apk add --update ca-certificates openssl && \  
update-ca-certificates && \  
apk add \  
\--no-cache \  
varnish=${VARNISH_VERSION} \  
varnish-dev=${VARNISH_VERSION} \  
varnish-libs=${VARNISH_VERSION}  
  
# build & install & cleanup varnish modules  
RUN \  
cd /tmp && \  
apk add \  
\--no-cache \  
varnish-dev=${VARNISH_VERSION} && \  
apk add \  
\--no-cache \  
autoconf automake libtool make py-docutils python && \  
wget -O varnish_modules.tar.gz https://download.varnish-software.com/varnish-
modules/varnish-modules-${MODULE_VERSION}.tar.gz && \  
tar -zxf varnish_modules.tar.gz && \  
cd varnish-modules-${MODULE_VERSION} && ./configure && make && make install &&
\  
cd .. && rm -fr varnish-modules-${MODULE_VERSION} && \  
apk del varnish-dev autoconf automake make libtool python py-docutils  
  
WORKDIR /  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["-?"]  

