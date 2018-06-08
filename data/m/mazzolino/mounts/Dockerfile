FROM alpine  
  
RUN apk add --update --no-cache bash \  
&& rm /var/cache/apk/*  
  
COPY entrypoint /entrypoint  
  
ENTRYPOINT ["/entrypoint"]  

