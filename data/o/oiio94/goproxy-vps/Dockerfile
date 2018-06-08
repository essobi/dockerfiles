FROM alpine:3.6  
RUN \  
apk add --no-cache --virtual .build-deps ca-certificates curl \  
&& curl -fSL https://github.com/phuslu/goproxy-
ci/releases/download/r1555/goproxy-vps_linux_amd64-r256.tar.xz | tar xJ \  
&& rm -rf goproxy-vps_linux_amd64-r254.tar.xz \  
&& chmod -R 777 /goproxy-vps  
  
ENV CONFIG_FILE_URL = https://pastbin/raw/....  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
  
EXPOSE 8443  

