FROM alpine:3.4  
MAINTAINER Matt Graham <gadgetmg@gmail.com>  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN apk --no-cache add ca-certificates wget openvpn && \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
apk --no-cache del wget  
  
COPY client.tmpl /etc/openvpn/client.tmpl  
COPY auth.tmpl /etc/openvpn/auth.tmpl  
  
ENTRYPOINT ["dockerize", \  
"-template", "/etc/openvpn/client.tmpl:/etc/openvpn/client.conf", \  
"-template", "/etc/openvpn/auth.tmpl:/etc/openvpn/auth.txt", \  
"openvpn", \  
"--config", "/etc/openvpn/client.conf"]  

