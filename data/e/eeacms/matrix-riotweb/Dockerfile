FROM nginx:1.13.12-alpine  
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"  
  
ARG RIOT_WEB_VERSION="0.15.1"  
RUN set -ex \  
&& apk add --no-cache \  
ca-certificates \  
openssl \  
bash \  
&& update-ca-certificates \  
&& cd /tmp \  
&& wget https://github.com/vector-im/riot-
web/releases/download/v${RIOT_WEB_VERSION}/riot-v${RIOT_WEB_VERSION}.tar.gz \  
&& tar -xzvf riot-v${RIOT_WEB_VERSION}.tar.gz \  
&& mkdir -p /var/www \  
&& mv riot-v${RIOT_WEB_VERSION} /var/www/riot \  
&& apk del ca-certificates openssl \  
&& rm -rf /tmp/*  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 80  
STOPSIGNAL SIGTERM  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

