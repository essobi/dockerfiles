FROM alpine:latest  
RUN apk add --update curl coreutils && rm -rf /var/cache/apk/*  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["curl"]  

