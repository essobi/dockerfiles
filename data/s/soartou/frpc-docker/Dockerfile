FROM alpine:edge  
  
RUN apk update && apk add tzdata  
RUN cp -r -f /usr/share/zoneinfo/Hongkong /etc/localtime  
ADD frpc /usr/local/bin/  
RUN chmod +x /usr/local/bin/frpc  
ADD frpc.ini /etc/frp/  
  
CMD ["frpc", "-c", "/etc/frp/frpc.ini"]  

