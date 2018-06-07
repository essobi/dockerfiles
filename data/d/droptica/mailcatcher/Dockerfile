FROM debian:jessie  
  
RUN apt-get update && apt-get install -y ruby ruby-dev build-essential sqlite3
libsqlite3-dev  
  
RUN gem install mailcatcher --no-ri --no-rdoc  
  
RUN apt-get remove --purge -y build-essential ruby-dev libsqlite3-dev && apt-
get autoclean && apt-get clean  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# smtp port  
EXPOSE 1025  
# webserver port  
EXPOSE 80  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0", "--http-port", "80"]

