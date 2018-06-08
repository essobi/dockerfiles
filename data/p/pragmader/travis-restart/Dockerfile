FROM ubuntu:latest  
MAINTAINER Denis Rechkunov <denis.rechkunov@gmail.com>  
  
ADD run.sh /travis-restart/run.sh  
ADD register_job.sh /travis-restart/register_job.sh  
  
RUN chmod +x /travis-restart/register_job.sh  
RUN chmod +x /travis-restart/run.sh  
  
RUN apt-get update  
RUN yes | apt-get install cron jq curl  
  
# Create the log file to be able to run tail  
RUN touch /var/log/last-travis-restart.log  
  
CMD /travis-restart/register_job.sh && tail -f /var/log/last-travis-
restart.log  

