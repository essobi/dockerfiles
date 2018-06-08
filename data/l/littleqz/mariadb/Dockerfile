FROM alpine  
MAINTAINER littleqz@gmail.com  
LABEL description="A lightweight mariadb image based on alpine linux."  
  
ENV TERM xterm  
ENV ENV_FILE /var/lib/mysql/db.env  
ENV MYSQL_DATA_DIR /var/lib/mysql  
ENV MYSQL_ROOT_PASSWORD ""  
ENV MYSQL_USER ""  
ENV MYSQL_PASSWORD ""  
ENV MYSQL_DATABASE ""  
RUN apk update && apk add bash mariadb mariadb-client && \  
sed -ri "s/^(bind-address|skip-networking|log-bin)/# \1/" /etc/mysql/my.cnf  
  
COPY run.sh install-db.sh /  
RUN chmod a+x /*.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/run.sh"]  
CMD ["mysqld_safe"]  

