FROM bringnow/haproxy-letsencrypt  
  
RUN apt-get update && \  
apt-get install --yes inotify-tools dnsmasq && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

