FROM alpine:3.5  
MAINTAINER Johannes 'fish' Ziemke <docker@freigeist.org>  
  
VOLUME [ "/dumps" ]  
RUN apk add --update tcpdump  
  
ENTRYPOINT [ "/usr/sbin/tcpdump" ]  
CMD [ "-C", "1000", "-W", "100", \  
"-v", "-w", "/dumps/dump" ]  

