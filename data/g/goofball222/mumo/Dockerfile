FROM python:2-alpine3.7  
MAINTAINER The Goofball "goofball222@gmail.com"  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL \  
org.label-schema.vendor=goofball222 \  
org.label-schema.url="https://github.com/goofball222/mumo" \  
org.label-schema.name="Mumble/Murmur Server Mumo Script" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url="https://github.com/goofball222/mumo.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.schema-version="1.0"  
  
ENV \  
DEBUG=false \  
MUMO_OPTS= \  
PGID=999 \  
PUID=999 \  
RUNAS_UID0=false  
  
WORKDIR /opt/mumo  
  
COPY root /  
  
RUN set -x \  
&& delgroup ping \  
&& addgroup -g $PGID mumo \  
&& adduser -D -G mumo -u $PUID mumo \  
&& apk add --no-cache bash libstdc++ openssl shadow su-exec \  
&& apk add --no-cache --virtual .build-deps bzip2-dev g++ git openssl-dev \  
&& pip install --global-option=build_ext --global-option="-D__USE_UNIX98"
zeroc-ice \  
&& git clone https://github.com/mumble-voip/mumo.git . \  
&& apk del .build-deps \  
&& bash -c 'mkdir -p {config,log}' \  
&& mv /opt/mumo/mumo.ini /opt/mumo/mumo.ini-default \  
&& chown -R mumo:mumo /opt/mumo \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' +;  
  
VOLUME ["/opt/mumo/config","/opt/mumo/log"]  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["mumo"]  

