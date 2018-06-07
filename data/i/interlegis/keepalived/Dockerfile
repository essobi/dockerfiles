FROM alpine:3.6  
RUN apk --update -t add --no-cache keepalived iproute2 grep bash tcpdump sed
&& \  
rm -f /var/cache/apk/* /tmp/*  
  
COPY keepalived.sh /usr/bin/keepalived.sh  
COPY keepalived.conf /etc/keepalived/keepalived.conf  
  
RUN chmod +x /usr/bin/keepalived.sh  
  
ENTRYPOINT ["/usr/bin/keepalived.sh"]  

