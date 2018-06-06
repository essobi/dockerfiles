FROM alpine:latest  
RUN apk update && apk add \--virtual .build-deps curl jq && \  
curl -Ls `curl -s https://api.github.com/repos/Cube-Earth/tools-coreos-
ct/releases/latest | jq -r '.assets[].browser_download_url'` | gunzip -c - >
/usr/bin/ct && \  
chmod +x /usr/bin/ct && \  
apk del .build-deps && rm -rf /var/cache/apk  
  
ENTRYPOINT ["/usr/bin/ct"]  

