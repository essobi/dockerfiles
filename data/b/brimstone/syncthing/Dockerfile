FROM alpine  
  
ENTRYPOINT ["/opt/syncthing", "-gui-address", "http://0.0.0.0:8080"]  
  
EXPOSE 8080  
ENV SYNCTHING_VERSION=0.14.47 \  
HOME=/home  
  
RUN chmod 777 /home  
  
RUN apk add --no-cache --virtual .build-deps \  
curl \  
ca-certificates \  
&& mkdir /opt \  
&& cd /opt \  
&& curl -L
https://github.com/syncthing/syncthing/releases/download/v${SYNCTHING_VERSION}/syncthing-
linux-amd64-v${SYNCTHING_VERSION}.tar.gz \  
| tar zx syncthing-linux-amd64-v${SYNCTHING_VERSION}/syncthing \  
&& apk del .build-deps \  
&& mv syncthing-linux-amd64-v${SYNCTHING_VERSION}/syncthing /opt \  
&& rmdir syncthing-linux-amd64-v${SYNCTHING_VERSION}  

