FROM alpine:latest  
MAINTAINER Fabian Sabau "fabian.sabau+docker@gmail.com"  
ENV SIEGE_VERSION=3.1.4  
RUN set -xe; \  
apk add --no-cache --virtual .build-deps curl g++ make \  
&& curl http://download.joedog.org/siege/siege-${SIEGE_VERSION}.tar.gz >
siege-${SIEGE_VERSION}.tar.gz \  
&& tar -xf siege-${SIEGE_VERSION}.tar.gz \  
&& cd siege-${SIEGE_VERSION} \  
&& ./configure \  
&& make install \  
&& apk del .build-deps  
  
ENTRYPOINT ["siege"]  
CMD ["--help"]  

