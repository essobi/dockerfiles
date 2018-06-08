FROM alpine:3.5  
# useful things..  
RUN apk --no-cache add ca-certificates openssl su-exec  
  
# add dumb-init (https://github.com/Yelp/dumb-init)  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /bin/dumb-init  
RUN chmod +x /bin/dumb-init  
  
ENV REFRESHED=20170221  
RUN apk --no-cache upgrade  
  

