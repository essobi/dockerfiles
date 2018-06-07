FROM alpine:3.6  
LABEL maintainer="gmblar+github@gmail.com"  
  
ENV MYSQL_HOST=mysql  
ENV MYSQL_BACKUP_COMPRESS=yes  
  
COPY content /  
RUN mysql-setup  
  
ENTRYPOINT ["mysql-entrypoint"]  

