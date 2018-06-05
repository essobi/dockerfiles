FROM alpine:edge  
  
RUN apk add bird --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/  
  
COPY run.sh /root/  
RUN chmod +x /root/run.sh && \  
rm -rf /etc/bird.conf  
  
VOLUME ["/etc/bird.conf"]  
  
CMD ["/root/run.sh"]  

