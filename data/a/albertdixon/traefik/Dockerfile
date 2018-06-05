FROM alpine:3.2  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
ENV GOSU_VER=1.7 \  
T2_VER=v2.2.1 \  
TRAEFIK_VER=v1.0.alpha.358  
ADD
https://github.com/albertrdixon/tmplnator/releases/download/${T2_VER}/t2-linux.tgz
/t2.tgz  
ADD https://github.com/tianon/gosu/releases/download/${GOSU_VER}/gosu-amd64
/bin/gosu  
ADD
https://github.com/emilevauge/traefik/releases/download/${TRAEFIK_VER}/traefik
/bin/  
  
COPY *.tmpl /templates/  
COPY docker-* /sbin/  
RUN apk add --update --repository
http://dl-1.alpinelinux.org/alpine/edge/testing/ tini \  
&& tar xvzf /t2.tgz -C /bin && rm -f /t2.tgz \  
&& chmod +x /sbin/* /bin/*  
  
ENTRYPOINT ["tini", "-g", "--", "docker-entry"]  
CMD ["docker-start"]  
EXPOSE 1090 8888  
ENV ETCD=enabled \  
PORT=1090 \  
LOG_LEVEL=ERROR \  
WEB=enabled \  
WEB_PORT=8888 \  
WEB_READ_ONLY=true

