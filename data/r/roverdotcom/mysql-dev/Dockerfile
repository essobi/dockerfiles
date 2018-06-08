FROM mysql:5.6  
  
RUN apt-get update && apt-get install -y \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MYSQLD_ARGS --max_allowed_packet=1024M --innodb_file_per_table
--net_read_timeout=240 \--net_write_timeout=480 \--skip-host-cache --skip-
name-resolve  
  
ADD rover.cnf /etc/mysql/conf.d/rover.cnf  

