FROM mariadb:10.1  
LABEL maintainer="daniel.baragan@eaudeweb.ro" \  
name="maria"  
  
RUN apt-get update && apt-get -y --no-install-recommends install \  
vim \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ARG EDW_BUILD_maria_innodb_log_file_size=300M  
  
RUN sed -i -e"s/^#innodb_log_file_size.*=.*[0-9]\\+M/innodb_log_file_size =
${EDW_BUILD_maria_innodb_log_file_size}/" /etc/mysql/my.cnf  
  
ADD /container-scripts/entrypoint.sh \  
/usr/local/bin/  
  
ENTRYPOINT ["entrypoint.sh"]  
# mariadb own entrypoint, docker-entrypoint.sh will prepend mysqld if it finds
that the command is a bunch of options  
# our entrypoint, entrypoint.sh will pass those to docker-entrypoint.sh  
CMD ["--character-set-server=utf8mb4", "--collation-
server=utf8mb4_unicode_ci"]  

