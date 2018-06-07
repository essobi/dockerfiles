FROM ubuntu:14.04  
MAINTAINER ilpuccio.febo@gmail.com  
  
ENV MYSQL_USER=mysql \  
MYSQL_DATA_DIR=/var/lib/mysql \  
MYSQL_RUN_DIR=/run/mysqld \  
MYSQL_LOG_DIR=/var/log/mysql  
  
RUN apt-get update \  
&& apt-get install -y mysql-server \  
&& rm -rf ${MYSQL_DATA_DIR} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y rsync  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
# RUN addgroup --gid 10513 bioinfousers &&\  
# adduser --uid 11247 --gid 10513 bioinfo  
# USER bioinfo  
COPY download_ensembl.sh /sbin/  
RUN chmod 755 /sbin/download_ensembl.sh  
  
EXPOSE 5306/tcp  
VOLUME ["${MYSQL_DATA_DIR}", "${MYSQL_RUN_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["/usr/bin/mysqld_safe"]  

