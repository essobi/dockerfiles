FROM alpine:3.5  
ADD https://github.com/emailbob/docker-registry-
cleaner/releases/download/latest-linux/docker-registry-cleaner /docker-
registry-cleaner  
  
RUN apk add --update ca-certificates && \  
rm -rf /var/cache/apk/* && \  
chmod +x /docker-registry-cleaner  
  
CMD ["/docker-registry-cleaner"]

