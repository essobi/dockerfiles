FROM alpine:latest  
  
RUN apk add --no-cache bash tzdata  
  
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/US/Eastern
/etc/localtime  
RUN echo "US/Eastern" > /etc/timezone  
  
ADD hrs /usr/bin/hrs  
  
ENTRYPOINT ["/usr/bin/hrs"]  

