FROM mariadb:10.0.28  
MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>  
  
# Remove log_bin from config file  
RUN sed -ri 's/^(log_bin\t*=\\.*)/#\1/' /etc/mysql/my.cnf \  
&& sed -ri 's/^(expire_logs_days\t*=.*)/#\1/' /etc/mysql/my.cnf  

