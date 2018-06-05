FROM centos:7  
ENV MAXSCALE_VERSION=2.2.5  
COPY entrypoint.sh /entrypoint.sh  
  
RUN yum install -y
https://downloads.mariadb.com/MaxScale/${MAXSCALE_VERSION}/centos/7/x86_64/maxscale-${MAXSCALE_VERSION}-1.centos.7.x86_64.rpm
&& \  
yum clean all -y && \  
chmod g=u /etc/passwd && \  
chmod +x entrypoint.sh && \  
chmod -R g=u /var/{lib,run}/maxscale && \  
chgrp -R 0 /var/{lib,run}/maxscale  
  
COPY maxscale.cnf /etc/maxscale.cnf  
  
USER 1001  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["maxscale", "--nodaemon", "--log=stdout"]  
  
EXPOSE 6603 3306 3307  
ENV THREADS=2 \  
SERVICE_USER=maxscale \  
READ_WRITE_LISTEN_ADDRESS=127.0.0.1 \  
READ_WRITE_PORT=3307 \  
READ_WRITE_PROTOCOL=MariaDBClient \  
MASTER_ONLY_LISTEN_ADDRESS=127.0.0.1 \  
MASTER_ONLY_PORT=3306 \  
MASTER_ONLY_PROTOCOL=MariaDBClient \  
MONITOR_USER=maxscale \  
DB1_PORT=3306 \  
DB2_PORT=3306 \  
DB3_PORT=3306 \  
DB1_PRIO=1 \  
DB2_PRIO=2 \  
DB3_PRIO=3  

