FROM nginx:stable  
  
ENV MUNKI_ROOT="" \  
SUS_ROOT="" \  
UPSTREAM_SERVER="" \  
MAX_SIZE=100g \  
EXPIRE_PKGS=30d \  
EXPIRE_ICONS=14d \  
EXPIRE_SUS=14d \  
EXPIRE_OTHER=10m \  
PORT=8080 \  
AVAHI_DOMAIN=local  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y avahi-daemon \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
COPY run /usr/local/bin/run  
  
RUN chmod +x /usr/local/bin/run  
  
VOLUME ["/cache"]  
  
CMD ["/usr/local/bin/run"]  

