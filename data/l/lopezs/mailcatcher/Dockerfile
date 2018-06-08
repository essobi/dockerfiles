FROM debian:wheezy  
  
# Install ruby  
RUN apt-get update && \  
apt-get install -y \  
ruby \  
ruby-dev \  
build-essential \  
sqlite3 \  
libsqlite3-dev  
  
# Install mailcatcher  
RUN gem install mailcatcher --no-ri --no-rdoc  
  
# Cleanup  
RUN apt-get remove --purge -y build-essential ruby-dev libsqlite3-dev && \  
apt-get autoclean && \  
apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# SMTP port  
EXPOSE 1025  
# web port  
EXPOSE 1080  
CMD ["mailcatcher", "--foreground", "--ip=0.0.0.0"]

