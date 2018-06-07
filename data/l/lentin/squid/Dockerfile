FROM alpine  
MAINTAINER lentin <docker@lte.pw>  
  
ADD squid.conf /etc/squid/squid.conf  
ADD entrypoint.sh /entrypoint.sh  
  
RUN apk add --no-cache squid curl && \  
chmod +x /entrypoint.sh && \  
squid -zF  
  
EXPOSE 443  
ENTRYPOINT ["/entrypoint.sh"]  

