FROM alpine  
  
RUN apk add -U ca-certificates  
  
VOLUME /data  
VOLUME /etc/aria2  
EXPOSE 6800  
EXPOSE 25236  
COPY aria2c /bin/aria2c  
  
RUN touch /etc/aria2/aria2.conf  
  
CMD ["aria2c", "--dir=/data", "--conf-path=/etc/aria2/aria2.conf", "--enable-
rpc", "--rpc-listen-all=true", "--rpc-allow-origin-all"]  

