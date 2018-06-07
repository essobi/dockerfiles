from frolvlad/alpine-glibc:alpine-3.4  
# install dumb-init, a simple process supervisor and init system  
ENV DUMB_INIT_VERSION 1.1.3  
RUN set -ex \  
&& apk add --no-cache curl build-base bash \  
&& curl -Lo dumb-init.tgz "https://github.com/Yelp/dumb-
init/archive/v${DUMB_INIT_VERSION}.tar.gz" \  
&& tar xzf dumb-init.tgz \  
&& cd dumb-init-${DUMB_INIT_VERSION} \  
&& make \  
&& cp dumb-init /usr/bin \  
&& cd .. \  
&& rm -rf dumb-init* \  
&& apk del curl build-base bash  
  
ENV SIGIL_VERSION 0.4.0  
RUN set -ex \  
&& apk add --no-cache curl \  
&& curl -Lo sigil.tgz
"https://github.com/gliderlabs/sigil/releases/download/v${SIGIL_VERSION}/sigil_${SIGIL_VERSION}_Linux_x86_64.tgz"
\  
&& tar xzf sigil.tgz -C /usr/local/bin \  
&& rm sigil.tgz \  
&& apk del curl  
  
ENV FILEBEAT_VERSION=1.3.1 \  
FILEBEAT_SHA1=693c04e2251498e73436cfc2b36a3a0aec920a2d  
RUN set -ex \  
&& apk add --no-cache curl \  
&& curl -Lo filebeat.tgz
"https://download.elastic.co/beats/filebeat/filebeat-${FILEBEAT_VERSION}-x86_64.tar.gz"
\  
&& echo "${FILEBEAT_SHA1} filebeat.tgz" | sha1sum -c - \  
&& tar xzf filebeat.tgz \  
&& cp filebeat-*/filebeat /usr/local/bin \  
&& rm -rf filebeat* \  
&& apk del curl  
  
COPY docker-entrypoint.sh filebeat.yml.tmpl /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD [ "filebeat", "-e" ]  

