FROM mysql:5.7  
LABEL NAME=mysql  
LABEL VERSION=5.7  
  
ENV LOGFILES="/var/log/mysql/error.log"  
COPY . /  
  
RUN rm $LOGFILES || :  
  
EXPOSE 3306  
ENTRYPOINT ["/usr/local/bin/logged-stdout", "/usr/local/bin/docker-
entrypoint.sh"]  
CMD ["mysqld"]  

