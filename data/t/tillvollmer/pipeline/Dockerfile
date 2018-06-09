FROM ruby:2.2.5  
MAINTAINER Till Vollmer <till@meisterlabs.com>  
ENV MYSQL_USER=mysql \  
MYSQL_DATA_DIR=/var/lib/mysql \  
MYSQL_RUN_DIR=/run/mysqld \  
MYSQL_LOG_DIR=/var/log/mysql  
  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server default-jre
nodejs libssl1.0.0 openssl  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY phantomjs /usr/bin/  
  
CMD ["/usr/bin/mysqld_safe"]  
# just a test  

