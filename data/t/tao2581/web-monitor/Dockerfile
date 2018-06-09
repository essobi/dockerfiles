FROM ubuntu:14.04  
MAINTAINER tao2581 <tao2581@126.com>  
  
ADD monitor.sh /home/monitor.sh  
  
ADD monitor.conf /home/monitor.conf  
  
ADD start.sh /home/start.sh  
  
RUN chmod +x /home/start.sh  
  
RUN apt-get update && apt-get -y install curl  
  
ENV DINTALK_TOKEN=null  
ENV SITES=null  
ENV CRON_ENTRY=3  
# Clean up  
USER root  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
RUN echo "start runing ... " >> /var/log/cron.log  
  
WORKDIR /home/  
  
CMD ["/home/start.sh"]

