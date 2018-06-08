FROM alpine:edge  
  
RUN apk update && apk add tzdata  
RUN cp -r -f /usr/share/zoneinfo/Hongkong /etc/localtime  
ADD frps /usr/local/bin/  
RUN chmod +x /usr/local/bin/frps  
  
CMD ["frps", "-c", "/etc/frp/frps.ini"]  

