FROM haugene/transmission-openvpn  
  
MAINTAINER Carsten Stender  
  
RUN apt-get update \  
&& apt-get install -y make ruby ruby-dev supervisor\  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN gem install transmission-rss  
  
ENV "XDG_CONFIG_HOME=/data/"  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY transmission-rss.conf /etc/transmission-rss.conf  
COPY init.sh /  
  
CMD ["/usr/bin/supervisord"]  

