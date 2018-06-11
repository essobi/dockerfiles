FROM alpine:edge  
  
MAINTAINER The Atlantic Programmers <programmers@theatlantic.com>  
  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REV  
ARG UNISON_VERSION=2.51.2  
ENV VCS_URL git@github.com:theatlantic/ollie-docker-containers.git  
  
LABEL org.label-schema.name="ollie-unison" \  
org.label-schema.description="Ollie Unison container" \  
org.label-schema.vendor="The Atlantic" \  
org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.version="$VERSION" \  
org.label-schema.vcs-url="$VCS_URL" \  
org.label-schema.vcs-rev="$VCS_REV" \  
org.label-schema.license="BSD-2" \  
org.label-schema.schema-version="1.2"  
  
RUN apk add --no-cache build-base curl bash supervisor \  
&& apk add --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ ocaml \  
&& curl -L
https://github.com/bcpierce00/unison/archive/v$UNISON_VERSION.tar.gz | tar zxv
-C /tmp \  
&& cd /tmp/unison-${UNISON_VERSION} \  
&& sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/'
src/fsmonitor/linux/inotify_stubs.c \  
&& make UISTYLE=text NATIVE=true STATIC=true \  
&& cp src/unison src/unison-fsmonitor /usr/local/bin \  
&& apk del curl build-base ocaml \  
&& apk add --no-cache libgcc libstdc++ \  
&& rm -rf /tmp/unison-${UNISON_VERSION} \  
&& apk add --no-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ shadow \  
&& apk add --no-cache tzdata  
  
ENV TZ="America/New_York" \  
LANG="C.UTF-8" \  
UNISON_DIR="/data" \  
HOME="/root"  
COPY entrypoint.sh /entrypoint.sh  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN mkdir -p /docker-entrypoint.d \  
&& chmod +x /entrypoint.sh \  
&& mkdir -p /etc/supervisor.conf.d  
  
COPY supervisor.unison.conf /etc/supervisor.conf.d/supervisor.unison.conf  
  
ENV DOCKERIZE_VERSION 0.3.0  
ENV DOCKERIZE_URL
"https://github.com/jwilder/dockerize/releases/download/v$DOCKERIZE_VERSION/"\  
"dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz"  
RUN apk add --no-cache curl openssl \  
&& curl -SL "$DOCKERIZE_URL" | tar -xvzC /usr/bin \  
&& apk del curl  
  
RUN mkdir -p /www/logs/unison \  
&& mkdir -p /home/deploy/.unison \  
&& groupadd -g 509 deploy \  
&& useradd -Md /home/deploy -u 508 -g 509 -G deploy deploy \  
&& chown -R deploy:deploy /www \  
&& chown -R deploy:deploy /home/deploy  
COPY entrypoint_custom.sh /docker-entrypoint.d/entrypoint_custom.sh  
  
VOLUME ["/home/deploy/.unison"]  
  
ENV UNISONLOCALHOSTNAME ollie_unison  
  
EXPOSE 5000  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["supervisord"]  

