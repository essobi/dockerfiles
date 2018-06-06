FROM alpine  
  
ARG CONVOY_VERSION=v0.5.0  
WORKDIR /usr/local/bin  
  
COPY entrypoint.sh .  
  
RUN chmod +x entrypoint.sh && \  
apk add --no-cache openssl && \  
wget -qO-
https://github.com/rancher/convoy/releases/download/$CONVOY_VERSION/convoy.tar.gz
\  
| gunzip -c \  
| tar xv --strip-components=1 convoy/convoy-pdata_tools convoy/convoy  
  
ENTRYPOINT ["entrypoint.sh"]  

