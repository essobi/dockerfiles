FROM odaniait/docker-base:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
RUN apt-get update  
RUN apt-get install -y sqlite3 libsqlite3-dev  
  
RUN gem install mailcatcher --no-ri --no-rdoc  
  
# setup mailcatcher service  
RUN mkdir -p /etc/service/mailcatcher  
COPY runit/mailcatcher.sh /etc/service/mailcatcher/run  
  
EXPOSE 2525 1080  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

