FROM ubuntu:14.04  
MAINTAINER "Alin Voinea" <alin.voinea@eaudeweb.ro>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
cron \  
gawk \  
rsync && \  
rm -rf /var/lib/apt/lists/*  
  
ADD backup.sh /bin/backup.sh  
ADD run.sh /bin/run.sh  
RUN chmod -v +x /bin/backup.sh /bin/run.sh  
  
CMD ["/bin/run.sh"]  

