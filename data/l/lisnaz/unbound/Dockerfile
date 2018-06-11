#  
# Dockerfile for unbound  
#  
FROM alpine  
MAINTAINER Vincent.Gu <g@v-io.co>  
  
ENV APP_DIR /srv/unbound  
ENV INTERFACE 0.0.0.0  
ENV PORT 53  
ENV SSL_PORT 853  
ENV REMOTE_CONTROL_INTERFACE 127.0.0.1  
ENV REMOTE_CONTROL_PORT 8953  
ENV VERBOSITY 1  
ENV CACHE_MIN_TTL 900  
ENV CACHE_MAX_TTL 172800  
ENV CACHE_MAX_NEGATIVE_TTL 0  
ENV INFRA_HOST_TTL 0  
ENV PREFETCH no  
  
ENV DEFAULT_FORWARD_ADDRS ""  
ENV FORWARDS ""  
EXPOSE $PORT/udp  
EXPOSE $PORT/tcp  
EXPOSE $SSL_PORT/tcp  
EXPOSE $REMOTE_CONTROL_PORT/tcp  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
# build software stack  
ENV DEP unbound  
RUN set -ex \  
&& apk --update --no-cache add $DEP \  
&& rm -rf /var/cache/apk/* \  
&& ln -s /etc/unbound "$APP_DIR"  
WORKDIR $APP_DIR  

