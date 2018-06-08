FROM debian:jessie  
  
# Labels  
LABEL maintainer="Paulino Padial <github.com/ppadial>"  
  
# Environment variables (with default values)  
ENV CRON_LOG_LEVEL 8  
ENV CRON_SCHEDULE 0 * * * *  
  
# Packages installation  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install --no-install-recommends --no-install-suggests -y ssmtp
mailutils mysql-client pigz pbzip2 cron && \  
apt-get purge -y --auto-remove && \  
rm -rf /var/lib/apt/lists/*  
  
# Copy and configure app files  
ADD automysqlbackup /etc/automysqlbackup  
RUN chmod +x /etc/automysqlbackup/automysqlbackup && \  
ln -s /etc/automysqlbackup/automysqlbackup /usr/bin/automysqlbackup  
  
# Configure entrypoint  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
VOLUME [ "/backup" ]  
WORKDIR /backup  
  
# Start the container process  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

