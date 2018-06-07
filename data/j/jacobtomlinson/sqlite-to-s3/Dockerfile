FROM alpine:3.4  
MAINTAINER Jacob Tomlinson <jacob@tom.linson.uk>  
  
# Install system dependancies  
RUN apk add --no-cache bash py-pip && rm -rf /var/cache/apk/*  
  
# Install sqlite  
RUN apk add --no-cache sqlite && rm -rf /var/cache/apk/*  
  
# Install aws cli  
RUN pip --no-cache-dir install awscli  
  
COPY sqlite-to-s3.sh /usr/bin/sqlite-to-s3  
  
ENTRYPOINT ["/usr/bin/sqlite-to-s3"]  
CMD ["cron", "0 1 * * *"]  

