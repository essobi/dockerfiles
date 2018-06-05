FROM asterios/mysql  
  
# Replication Master  
RUN echo [mysqld] > /etc/mysql/conf.d/rep-master.cnf \  
&& echo slave_compressed_protocol = 1 >> /etc/mysql/conf.d/rep-master.cnf \  
&& echo sync_master_info = 0 >> /etc/mysql/conf.d/rep-master.cnf \  
&& echo sync_relay_log = 0 >> /etc/mysql/conf.d/rep-master.cnf \  
&& echo sync_relay_log_info = 0 >> /etc/mysql/conf.d/rep-master.cnf \  
&& echo binlog_format = MIXED >> /etc/mysql/conf.d/rep-master.cnf \  
&& echo server-id = 1 >> /etc/mysql/conf.d/rep-master.cnf \  
&& echo log_bin = /var/log/mysql/mysql-bin.log >> /etc/mysql/conf.d/rep-
master.cnf \  
&& echo expire_logs_days = 7 >> /etc/mysql/conf.d/rep-master.cnf \  
&& echo max_binlog_size = 256M >> /etc/mysql/conf.d/rep-master.cnf  

