FROM alpine:3.5  
RUN apk -U add --update curl jq && rm -rf /var/cache/apk/*  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

