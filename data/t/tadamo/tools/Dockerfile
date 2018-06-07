FROM alpine:latest  
RUN apk update && \  
apk add --no-cache \  
bash \  
ca-certificates \  
openssl \  
curl \  
bind-tools \  
netcat-openbsd \  
jq \  
coreutils \  
openldap-clients \  
httpie \  
apache2-utils && \  
mkdir -p /.httpie && \  
chgrp -R 0 /.httpie && \  
chmod -R g=u /.httpie  
COPY ./bin/ /usr/local/bin  

