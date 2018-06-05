FROM ubuntu:18.04  
MAINTAINER Fabian Köster <mail@fabian-koester.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bacula-sd \  
inotify-tools \  
openssl \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /etc/bacula  
VOLUME /var/lib/bacula  
VOLUME /etc/dhparam  
  
COPY create_dhparam.sh entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT /usr/local/bin/entrypoint.sh  
  
EXPOSE 9103  

