FROM alpine  
LABEL maintainer="contact-docker@mo-mar.de"  
  
RUN apk add --no-cache mariadb-client postgresql-client mongodb-tools  
  
ADD backup /bin/backup  
ADD restore /bin/restore  
  
CMD ["/bin/backup"]  

