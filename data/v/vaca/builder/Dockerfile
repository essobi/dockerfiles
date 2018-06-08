FROM alpine:3.3  
RUN apk --no-cache add tzdata  
COPY mkrootfs /usr/local/sbin/mkrootfs  
  
ENTRYPOINT ["mkrootfs"]  

