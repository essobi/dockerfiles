FROM alpine:latest AS build  
  
ARG FLIF_VERSION=0.3  
ENV FLIF_VERSION=$FLIF_VERSION  
  
RUN set -e \  
&& cd /tmp \  
&& mkdir -p /tmp/build \  
&& wget https://github.com/FLIF-hub/FLIF/archive/v${FLIF_VERSION}.tar.gz \  
&& tar xzf v${FLIF_VERSION}.tar.gz -C /tmp/build \--strip-components=1 \  
&& apk add \--update build-base libpng-dev \  
&& cd /tmp/build \  
&& make \  
&& make install \  
&& mkdir -p /flif/bin /flif/data \  
&& mv /usr/local/bin/* /flif/bin  
  
FROM alpine:latest  
  
COPY \--from=build /flif /flif  
  
RUN set -e \  
&& apk add \--no-cache libpng \  
&& addgroup -g 1000 -S flif \  
&& adduser -u 1000 -S flif -G flif \  
&& ln -s /flif/bin/* /usr/local/bin/ \  
&& chown -R flif:flif /flif  
  
USER flif  
  
WORKDIR /flif/data

