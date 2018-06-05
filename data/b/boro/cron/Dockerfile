FROM ubuntu:latest  
MAINTAINER Boro <docker@bo.ro>  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/container-cron  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/container-cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
#Install Cron  
RUN apt-get update  
RUN apt-get -y install cron nano  
  
# Fix: "TERM environment variable not set." error when entering the container
with bash  
RUN echo "export TERM=xterm" >> /etc/bash.bashrc  
  
# Run the command on container startup  
CMD cron && tail -f /var/log/cron.log

