FROM alpine:3.7  
ENV VERSION 1.6.1  
RUN set -ex \  
&& apk add --no-cache ca-certificates  
  
RUN set -ex \  
&& apk add --no-cache --virtual .phraseapp-build \  
curl \  
&& curl -fSL -o /usr/local/bin/phraseapp "https://github.com/phrase/phraseapp-
client/releases/download/${VERSION}/phraseapp_linux_amd64" \  
&& chmod +x /usr/local/bin/phraseapp \  
&& apk del .phraseapp-build  
  
ENTRYPOINT [ "/usr/local/bin/phraseapp" ]  

