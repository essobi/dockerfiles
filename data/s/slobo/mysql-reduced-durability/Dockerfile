FROM azukiapp/ubuntu  
MAINTAINER Azuki <support@azukiapp.com>  
  
ENV MYSQL_VERSION 5.6  
# Install packages  
# Remove pre-installed database  
# Remove syslog configuration  
RUN apt-get update \  
&& apt-get -yq install mysql-server-$MYSQL_VERSION pwgen \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mysql/* \  
&& rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf  
  
# Add MySQL configuration  
ADD etc /etc  
  
# Add MySQL scripts  
ADD import_sql.sh /import_sql.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Exposed ENV  
ENV MYSQL_USER admin  
ENV MYSQL_PASS **Random**  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/run.sh"]  

