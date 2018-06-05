FROM alpine:3.1  
RUN apk --update add haproxy  
  
ADD ambassadorize /  
  
WORKDIR /  
ENTRYPOINT ["./ambassadorize"]

