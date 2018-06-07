FROM ubuntu:18.04  
MAINTAINER Hermann Mayer "hermann.mayer92@gmail.com"  
# You can change this environment variable on run's with -e  
ENV \  
DEBIAN_FRONTEND="noninteractive" \  
MDNS_HOSTNAME="ejabberd.local"  
# Install system packages  
RUN apt-get update -yqqq && \  
apt-get install -y \  
avahi-daemon avahi-discover avahi-utils \  
libnss-mdns haproxy supervisor \  
ejabberd ejabberd-contrib ejabberd-contrib \  
erlang-p1-mysql erlang-p1-pgsql erlang-p1-sqlite3  
  
# Copy avahi.sh  
COPY config/avahi.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/avahi.sh  
  
# Copy ejabberd.sh  
COPY config/ejabberd.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/ejabberd.sh  
  
# Configure haproxy  
COPY config/haproxy.conf /etc/haproxy/haproxy.cfg  
  
# Configure supervisord  
COPY config/supervisor/* /etc/supervisor/conf.d/  
  
# Configure ejabberd  
COPY config/ejabberd.yml /etc/ejabberd/ejabberd.yml  
  
# Define the command to run per default  
CMD /usr/bin/supervisord -nc /etc/supervisor/supervisord.conf  

