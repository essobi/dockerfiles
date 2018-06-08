FROM library/alpine:latest  
  
RUN apk add --update --no-cache bash pigz  
  
COPY files/bin/ /usr/bin/  
  
ENTRYPOINT ["/usr/bin/entrypoint"]  

