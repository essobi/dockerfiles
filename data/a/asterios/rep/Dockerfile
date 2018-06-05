FROM mysql:5.5.58  
  
# Update & upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y locales mc htop ifstat  
  
# Configure timezone and locale  
ENV LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 TERM=xterm  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen \  
&& dpkg-reconfigure -f noninteractive locales \  
&& echo "Europe/Moscow" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
# Defaults  
#skip-external-locking  
#memlock  
RUN echo [mysqld] > /etc/mysql/conf.d/customs.cnf \  
&& echo skip-name-resolve >> /etc/mysql/conf.d/customs.cnf \  
&& echo key_buffer_size = 16M >> /etc/mysql/conf.d/customs.cnf \  
&& echo max_allowed_packet = 16M >> /etc/mysql/conf.d/customs.cnf \  
&& echo thread_stack = 256K >> /etc/mysql/conf.d/customs.cnf \  
&& echo thread_cache_size = 64 >> /etc/mysql/conf.d/customs.cnf \  
&& echo myisam-recover-options = OFF >> /etc/mysql/conf.d/customs.cnf \  
&& echo max_connections = 1000 >> /etc/mysql/conf.d/customs.cnf \  
&& echo table_cache = 256 >> /etc/mysql/conf.d/customs.cnf \  
&& echo query_cache_limit = 32M >> /etc/mysql/conf.d/customs.cnf \  
&& echo query_cache_size = 32M >> /etc/mysql/conf.d/customs.cnf \  
&& echo max_heap_table_size = 1G >> /etc/mysql/conf.d/customs.cnf \  
&& echo tmp_table_size = 1G >> /etc/mysql/conf.d/customs.cnf  
  
# Use MyISAM Only  
RUN echo [mysqld] > /etc/mysql/conf.d/myisam.cnf \  
&& echo default-storage-engine = myisam >> /etc/mysql/conf.d/myisam.cnf \  
&& echo skip-innodb >> /etc/mysql/conf.d/myisam.cnf  
  
# Replication Slave  
RUN echo [mysqld] > /etc/mysql/conf.d/rep-slave.cnf \  
&& echo slave_compressed_protocol = 1 >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo sync_master_info = 0 >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo sync_relay_log = 0 >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo sync_relay_log_info = 0 >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo master-retry-count = 86400 >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo server-id = 2 >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo relay-log = /var/log/mysql/relay >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo relay-log-index = /var/log/mysql/relay.index >> /etc/mysql/conf.d/rep-
slave.cnf \  
&& echo relay-log-space-limit = 128M >> /etc/mysql/conf.d/rep-slave.cnf \  
&& echo max-relay-log-size = 32M >> /etc/mysql/conf.d/rep-slave.cnf  
  
# Clean relay info  
RUN sed -i '/\\#\\!\/bin\/bash/a[ ! -d /var/log/mysql ] && mkdir -p
/var/log/mysql\nchmod 1777 /var/log/mysql\nfind /var/log/mysql -type f -iname
"relay.*" -delete\n[ -f /var/lib/mysql/relay-log.info ] && rm
/var/lib/mysql/relay-log.info\n' /usr/local/bin/docker-entrypoint.sh

