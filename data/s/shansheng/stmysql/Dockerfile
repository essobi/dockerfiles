FROM mysql:5.7  
  
LABEL maintainer="shanshengsheng@gmail.com" \  
provider="SSS, Ltd."  
# ENV LANG="en_US.UTF-8" \  
# LANGUAGE="en_US:en" \  
# LC_ALL="en_US.UTF-8"  
  
# Default value for entrypoint  
ENV MYSQL_ROOT_PASSWORD=root \  
MYSQL_DEVOPS_DATABASE=devops \  
MYSQL_DEVOPS_USER=devops \  
MYSQL_DEVOPS_PASSWORD=devops \  
MYSQL_SONAR_DATABASE=sonar \  
MYSQL_SONAR_USER=sonar \  
MYSQL_SONAR_PASSWORD=sonar \  
MYSQL_JIRA_DATABASE=jira \  
MYSQL_JIRA_USER=jira \  
MYSQL_JIRA_PASSWORD=jira \  
DEVOPS_DOWNLOAD_URL="ftp://product:primeton@192.168.1.12/DevOps51/dist/devops-
dist/devops/files/devops.war"  
  
# Do not use alias cp  
RUN \cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# ADD resources/my.cnf /etc/mysql/my.cnf  
# RUN echo "character-set-server=utf8" >> /etc/mysql/conf.d/mysql.cnf \  
RUN echo "character-set-server=utf8" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "collation-server=utf8_bin" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "default-storage-engine=Innodb" >> /etc/mysql/mysql.conf.d/mysqld.cnf
\  
&& echo "max_allowed_packet=256M" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "innodb_log_file_size=2GB" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "explicit_defaults_for_timestamp=true" >>
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "max_connections=3600" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "lower_case_table_names=1" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "innodb_large_prefix=ON" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "innodb_file_format=Barracuda" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "innodb_file_format_check=ON" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "innodb_file_format_max=Barracuda" >>
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "innodb_file_per_table=ON" >> /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo "sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES" >>
/etc/mysql/mysql.conf.d/mysqld.cnf  
  
# ADD resources/devops/*.sql /tmp/devops/5.0/  
#RUN apt-get update && apt-get install -y \--no-install-recommends ca-
certificates wget \  
# && wget -t 3 -O /tmp/sql.tar.gz ${DEVOPS_DOWNLOAD_URL} \  
# && mkdir -p /tmp/devops/5.0/ \  
# && tar -zvxf /tmp/sql.tar.gz -C /tmp/devops/5.0/ \  
# && apt-get purge -y \--auto-remove ca-certificates wget  
  
ADD resources/entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]  
  
CMD [ "mysqld" ]  
#EXPOSE 3306  

