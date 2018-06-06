FROM registry:2  
ENV REGISTRY_CREDS registry_user registry_pass  
ENV REGISTRY_CERT_SUBJ "/C=AU/ST=Some-
State/O=OpenSource/CN=Registry/emailAddress=registry@example.com"  
ENV REGISTRY_CERT_DAYS 1825  
ENV REGISTRY_AUTH htpasswd  
ENV REGISTRY_AUTH_HTPASSWD_REALM Registry Realm  
ENV REGISTRY_AUTH_HTPASSWD_PATH /auth/htpasswd  
ENV REGISTRY_HTTP_TLS_CERTIFICATE /certs/domain.crt  
ENV REGISTRY_HTTP_TLS_KEY /certs/domain.key  
  
RUN apk add --update --no-cache openssl && rm -rf /var/cache/apk/* && mkdir -p
certs auth  
  
COPY docker-entrypoint.sh /entrypoint.sh  

