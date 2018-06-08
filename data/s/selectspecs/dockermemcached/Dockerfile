FROM alpine:latest  
RUN apk add --no-cache memcached  
EXPOSE 11211  
CMD ["memcached", "-m", "512", "-u", "memcached"]  

