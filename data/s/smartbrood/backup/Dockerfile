FROM alpine:3.6  
LABEL maintainer "Andrey N. Petrov <andreynpetrov@gmail.com>"  
  
RUN apk add --no-cache mariadb-client bash  
  
VOLUME ["/efs"]  
  
WORKDIR /efs  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["mariadb", "wordpress"]  

