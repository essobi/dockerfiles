FROM ruby:2.2-slim  
MAINTAINER Ryan Winograd <ryan@thewinograds.com>  
  
RUN set -ex && \  
buildDeps=' \  
build-essential \  
libsqlite3-dev \  
sqlite3 \  
' && \  
apt-get update && \  
apt-get install -y --no-install-recommends $buildDeps && \  
gem install mailcatcher --no-rdoc --no-ri && \  
apt-get purge -y --auto-remove build-essential libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 1025 1080  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]  

