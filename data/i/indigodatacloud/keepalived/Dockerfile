FROM alpine:latest  
  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && apk --update -t add keepalived iproute2 grep bash
tcpdump sed perl && rm -f /var/cache/apk/* /tmp/*  
  
COPY run.sh /run.sh  
COPY keepalived.conf /etc/keepalived/keepalived.conf  
  
ENTRYPOINT [ "/run.sh" ]  

