FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y wget  
  
RUN wget -O /bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-1.6.0  
RUN chmod +x /bin/docker  
  
VOLUME /data/builder-gc  
  
COPY files /  
  
RUN crontab /tmp/crontab  
RUN rm /tmp/crontab  
  
CMD ["/bin/sh", "-c", "cron && tail --retry --follow=name /data/builder-
gc/builder_gc.log"]  

