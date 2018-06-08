FROM alpine:latest  
  
RUN set -xe \  
&& apk update --no-cache && apk upgrade --no-cache \  
&& apk add --update --no-cache dhcrelay \  
&& rm -rf /var/cache/apk/*  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT [ "/entrypoint.sh" ]  

