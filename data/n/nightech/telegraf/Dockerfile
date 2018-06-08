FROM telegraf  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
sysstat && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
COPY ./overlay/ /  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["telegraf", "--config", "/etc/telegraf/telegraf.conf", "--config-
directory", "/etc/telegraf/conf.d/"]  

