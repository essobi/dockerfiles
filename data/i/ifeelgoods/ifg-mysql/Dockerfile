from mysql:5.7  
ENV MYSQL_ROOT_PASSWORD password  
RUN sed -i '/bind-address/ c\bind-address= 0.0.0.0' /etc/mysql/my.cnf  
  
RUN conf_path=/etc/mysql/mysql.conf.d/mysqld.cnf && line=`cat $conf_path |
grep -n "\\[mysqld\\]" | cut -d ':' -f 1` \  
&& sed "$line a innodb_file_format = Barracuda" -i $conf_path \  
&& sed "$line a innodb_large_prefix" -i $conf_path \  
&& sed "$line a innodb_file_per_table=true" -i $conf_path \  
&& sed "$line a default-time-zone='+00:00'" -i $conf_path  
  

