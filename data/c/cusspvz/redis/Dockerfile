FROM debian:wheezy  
MAINTAINER José Moreira <jose.moreira@findhit.com>  
  
LABEL version=0.0.1  
LABEL service=redis  
LABEL description="redis cluster image"  
  
ADD https://www.dotdeb.org/dotdeb.gpg /tmp/dotdeb.gpg  
RUN echo "deb http://packages.dotdeb.org wheezy all" >> /etc/apt/sources.list
&& \  
echo "deb-src http://packages.dotdeb.org wheezy all" >> /etc/apt/sources.list
&& \  
apt-key add /tmp/dotdeb.gpg && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
ruby \  
redis-server \  
redis-sentinel \  
redis-tools \  
&& \  
gem install redis && \  
rm -rf /var/lib/apt/lists/*  
  
# /cmd dir  
RUN mkdir /cmd  
WORKDIR /cmd  
  
# Startup script  
ADD startup.sh /cmd/startup  
ADD http://download.redis.io/redis-stable/src/redis-trib.rb /cmd/setup  
  
# Permissions  
RUN chmod +x -R /cmd  
  
# Volumes  
VOLUME /var/lib/redis  
  
# Exposures  
# Redis  
EXPOSE 6379  
# Redis Sentinel  
EXPOSE 26379  
CMD [ "/cmd/startup" ]  

