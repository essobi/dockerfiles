FROM telegraf:1.3.5  
  
MAINTAINER sebastien.helbert@gmail.com  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
RUN mv /etc/telegraf/telegraf.conf /etc/telegraf/telegraf.conf.initial  
  
COPY telegraf.conf /etc/telegraf/telegraf.conf

