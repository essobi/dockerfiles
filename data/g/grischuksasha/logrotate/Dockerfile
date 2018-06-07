FROM alpine:3.7  
RUN apk update && apk add logrotate  
  
RUN mkdir /logrotate  
  
COPY logrotate.conf /etc/logrotate.conf  
  
WORKDIR /logrotate  
  
CMD ["crond", "-f"]

