FROM mysql:latest  
  
# Make mysql user uid/gid 1000 since this is the uid that boot2docker  
# will use for mounted directories.  
RUN usermod -u 1000 mysql && \  
groupmod -g 1000 mysql && \  
## The previous mysql uid was 999, so chown any 999 files to mysql.  
find / -uid 999 2>/dev/null | xargs chown mysql:mysql  
  
ADD my.cnf /etc/mysql/my.cnf  
ENV MYSQL_ALLOW_EMPTY_PASSWORD 1  
EXPOSE 3306  

