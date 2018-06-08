FROM alpine:latest  
MAINTAINER Kenneth Tan <github@way-of-the-blade.com>  
  
RUN apk -U add mariadb  
  
# RUN wget -nv https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/mysqltuner.pl -O /usr/local/bin/mysqltuner.pl  
# RUN wget -nv https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/basic_passwords.txt -O /usr/local/bin/basic_passwords.txt  
COPY docker_init.sh /usr/local/bin/  
# RUN chmod +x /usr/local/bin/mysqltuner.pl  
RUN chmod +x /usr/local/bin/docker_init.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/usr/local/bin/docker_init.sh"]  

