FROM alpine  
MAINTAINER "Tiny Docker Images" <tini2mini@gmail.com>  
  
RUN apk add --no-cache tini su-exec  
COPY tini-entrypoint.sh docker-entrypoint.sh /  
  
ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]  
CMD ["sh"]  

