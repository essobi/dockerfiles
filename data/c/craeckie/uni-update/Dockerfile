#FROM ubuntu  
#FROM phusion/baseimage:0.9.16  
FROM craeckie/uni-base  
  
MAINTAINER Josia <josia-login@rosskopfs.de>  
  
# Install required packages  
RUN apt-get install -y curl wget recode nano  
  
# Set environment variables  
ENV updatelog $logdir/update.log  
ENV cronpath /etc/cron.d/update-cron  
  
# Cron job  
ADD cron $cronpath  
RUN chmod 0744 $cronpath  
  
# Scripts run by cron  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
ADD run-refresh.sh /root/run-refresh.sh  
RUN chmod +x /root/run-refresh.sh  
  
RUN touch $updatelog  
  
# Clean up  
RUN apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm
-rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

