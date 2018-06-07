FROM lsiobase/alpine  
MAINTAINER tynor88 <tynor@hotmail.com>  
  
#Adding Custom files  
COPY init/ /etc/my_init.d/  
COPY cron/ /etc/cron.d/  
COPY app/script/ /app/script/  
RUN chmod -v +x /etc/my_init.d/*.sh /app/script/*.sh  

