FROM alpine:3.6  
RUN apk add --update --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" > /etc/timezone && apk del tzdata  
  
RUN apk add --update --no-cache tinc iptables  
  
VOLUME ["/etc/tinc"]  
  
ENTRYPOINT ["/usr/sbin/tincd"]  

