FROM alpine:3.5  
RUN \  
apk add --no-cache --virtual .build-deps ca-certificates curl \  
&& mkdir -p /opt/goproxy \  
&& cd /opt/goproxy \  
&& curl -fSL https://github.com/phuslu/goproxy-
ci/releases/download/r1309/goproxy-vps_linux_amd64-r163.tar.xz | tar xJ  
  
ENV CONFIG_FILE_URL = https://pastbin/raw/....  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT sh /entrypoint.sh  
  
EXPOSE 8443  

