FROM gliderlabs/alpine:3.4  
MAINTAINER Will Salt <williamejsalt@gmail.com>  
  
ENV
OAUTH2_RELEASE_URL=https://github.com/bitly/oauth2_proxy/releases/download/v2.1/oauth2_proxy-2.1.linux-
amd64.go1.6.tar.gz  
  
RUN apk --update add tar ca-certificates  
  
RUN adduser -S oauth2proxy  
  
ADD "$OAUTH2_RELEASE_URL" /tmp  
  
RUN tar -xf /tmp/oauth2_proxy-2.1.linux-amd64.go1.6.tar.gz -C ./bin --strip-
components=1 && rm /tmp/*.tar.gz  
  
USER oauth2proxy  
  
ENTRYPOINT ["oauth2_proxy"]  

