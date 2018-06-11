FROM alpine:3.6  
RUN \  
apk add --no-cache --virtual .build-deps ca-certificates curl \  
&& curl -fSL https://github.com/phuslu/goproxy-
ci/releases/download/r1547/goproxy-vps_linux_amd64-r254.tar.xz | tar xJ \  
&& rm -rf goproxy-vps_linux_amd64-r254.tar.xz  
  
ENV CONFIG_FILE_URL = https://pastbin/raw/....  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
  
EXPOSE 8443  

