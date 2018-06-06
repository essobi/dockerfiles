FROM alpine:3.1  
RUN apk add --update mysql-client && rm -rf /var/cache/apk/*  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
COPY entrypoint.sh /  
  
CMD ["/entrypoint.sh"]

