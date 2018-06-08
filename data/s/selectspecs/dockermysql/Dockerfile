FROM alpine:latest  
  
WORKDIR /app  
VOLUME /app  
  
RUN apk --update add mysql mysql-client && rm -f /var/cache/apk/*  
COPY my.cnf /etc/mysql/my.cnf  
COPY startup.sh /startup.sh  
EXPOSE 3306  
CMD ["/startup.sh"]  

