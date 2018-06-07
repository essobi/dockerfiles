FROM alpine  
  
RUN apk update && apk add ca-certificates wget \  
&& wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 \  
&& apk del wget && rm -rf /var/cache/apk/*  
  
RUN chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  

