# Phusion baseimage comes with cron and a proper init:  
FROM phusion/baseimage:latest  
MAINTAINER Ryan McGuire <ryan@enigmacurry.com>  
  
RUN useradd -ms /bin/bash rss2email  
  
RUN apt-get update  
RUN apt-get install -y ssmtp python3-pip  
  
RUN echo "0 * * * * /usr/local/bin/r2e run" | crontab -u rss2email -  
RUN mkdir /home/rss2email/.config && \  
ln -s /home/rss2email/.rss2email/rss2email.cfg
/home/rss2email/.config/rss2email.cfg && \  
chown -R rss2email:rss2email /home/rss2email/.config  
  
RUN pip3 install feedparser html2text
https://github.com/wking/rss2email/archive/master.zip  
  
CMD "/sbin/my_init"  
VOLUME ["/home/rss2email/.rss2email", "/home/rss2email/.config", "/etc/ssmtp"]  

