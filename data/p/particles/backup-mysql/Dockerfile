FROM debian  
MAINTAINER particles.io  
  
# Update  
RUN apt-get update && apt-get -y dist-upgrade && apt-get -y autoremove && apt-
get clean  
  
# Timezone  
# Set the time zone to the local time zone  
RUN echo "Europe/Rome" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
# Add MySQL tools packages  
RUN apt-get -y install mysql-client  
  
ADD init-backup.sh /init-backup.sh  
RUN chmod 0755 /init-backup.sh  
  
ENTRYPOINT ["/init-backup.sh"]  

