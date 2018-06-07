FROM alpine:edge  
  
ENV DOCKERIZE_VERSION=0.4.0 \  
POSTFIX_MYDESTINATION=localhost \  
POSTFIX_MYDOMAIN=localhost.local \  
POSTFIX_MYHOSTNAME=localhost.local \  
POSTFIX_RELAY="" \  
POSTFIX_RELAY_AUTH="" \  
POSTFIX_INET_INTERFACES=loopback-only  
  
RUN set -ex \  
&& apk add --no-cache \  
postfix \  
supervisor \  
rsyslog \  
&& apk add --no-cache --virtual .build-deps \  
ca-certificates \  
curl \  
&& mkdir -p /usr/local/bin/ \  
&& curl -SL
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
| tar xzC /usr/local/bin \  
&& apk del .build-deps  
  
EXPOSE 25  
  
COPY ./supervisord.conf /etc/supervisor/supervisord.conf  
COPY ./docker_entrypoint.sh /docker_entrypoint.sh  
COPY ./main.tmpl /main.tmpl  
  
ENTRYPOINT ["/bin/sh", "docker_entrypoint.sh"]  
  
CMD dockerize -stdout /var/log/maillog -template
/main.tmpl:/etc/postfix/main.cf /usr/bin/supervisord -c
/etc/supervisor/supervisord.conf  

