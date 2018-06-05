FROM nginx  
  
MAINTAINER blackbarn@gmail.com  
  
# Use bash instead of sh  
RUN rm -rf /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install dependencies  
RUN apt-get -q update && \  
apt-get install -qy --force-yes cron python-pip build-essential python-dev
libffi-dev libssl-dev git  
  
# Clone PlexEmail  
RUN git clone https://github.com/jakewaldron/PlexEmail.git /PlexEmail  
  
# Cleanup  
RUN apt-get autoremove &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/*  
  
# Define the config volume  
VOLUME ["/config"]  
  
# Add the nginx default.conf  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
# Add start.sh and ensure it can be executed  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Add the default crontab and set permissions  
ADD crontab /etc/cron.d/plexemail  
RUN chmod 0644 /etc/cron.d/plexemail  
  
# Expose port  
EXPOSE 80  
# Start command, run start.sh to run additional run-time startup logic  
CMD ["/start.sh"]  

