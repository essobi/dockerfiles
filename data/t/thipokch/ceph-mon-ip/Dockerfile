FROM alpine  
  
# Relies on curl to get public ip address  
RUN apk --no-cache add curl  
COPY entrypoint.sh /  
WORKDIR /ceph-mon-ip  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]

