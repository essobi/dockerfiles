FROM phusion/baseimage  
  
MAINTAINER Dimitris Bozelos <dbozelos@gmail.com>  
  
# Update.  
RUN apt-get update  
  
# Install.  
RUN apt-get -y install gearman-job-server  
  
# Clean up.  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4730  
# @todo: Fix problem with entrypoint  
ENTRYPOINT ["gearmand"]  

