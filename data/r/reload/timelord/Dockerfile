FROM phusion/baseimage:0.9.17  
# Need git for cloning.  
RUN apt-get update && \  
apt-get install -y apache2 php5 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV TIMELORD_SITE_NAME Time Lord  
ENV TIMELORD_BASE /  
ENV TIMELORD_HARVESTER_URL http://harvester  
ENV TIMELORD_HARVESTER_API_PATH /api/v1/  
ENV TIMELORD_SALT_STRING ChangeMe  
  
RUN rm -rf /var/www/html  
COPY ./ /var/www/html  
  
# Script for setting up harvester.  
COPY docker/timelord.sh /etc/my_init.d/99-timelord  
  
# Make runit start apache.  
COPY docker/apache2.service /etc/service/apache2/run  

