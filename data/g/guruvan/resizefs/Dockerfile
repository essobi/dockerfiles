FROM alpine:latest  
  
COPY growpart /  
COPY grow.sh /  
  
RUN apk --update add sfdisk parted  
RUN apk add --update e2fsprogs=1.42.8-r2 -X
http://dl-3.alpinelinux.org/alpine/v2.7/main && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/grow.sh"]  

