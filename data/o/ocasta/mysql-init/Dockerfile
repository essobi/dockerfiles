FROM alpine:edge  
RUN apk add --no-cache bash mysql-client  
ADD ./init.sh /init.sh  
CMD ["/init.sh"]  

