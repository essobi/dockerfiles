FROM debian:stretch  
MAINTAINER LWB  
  
ENV DB_USERNAME=ADMIN \  
DB_PASSWORD=ADMIN \  
DB_HOST=mariadb \  
FILE_BACKUP_USER=ADMIN \  
FILE_BACKUP_PASSWORD=ADMIN \  
FILE_BACKUP_PATH=/ \  
BACKUP_HOST=db \  
LOG_HOST=mariadb \  
LOG_USERNAME=ADMIN \  
LOG_PASSWORD=ADMIN  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y --force-yes --no-install-recommends bzip2 mysql-client
cifs-utils && \  
rm -rf /var/lib/apt/lists  
  
USER root  
  
ADD ./backup.sh /  
  
CMD ["/backup.sh"]  

