FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y dist-upgrade  
  
RUN apt-get -q -y install \  
cron \  
supervisor \  
postfix \  
munin \  
apache2 \  
apache2-utils  
  
RUN rm -f /etc/cron.d/munin-node /etc/cron.daily/* /etc/cron.weekly/*  
  
RUN mkdir /var/run/munin/ \  
&& chown -R munin:munin /var/run/munin/ /var/www/html/  
  
RUN apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
ADD etc/supervisor/ /etc/supervisor/  
ADD etc/apache2/sites-available /etc/apache2/sites-available  
ADD etc/munin/munin.conf /etc/munin/munin.conf  
  
ADD scripts/entrypoint.sh /entrypoint.sh  
  
RUN chmod 755 /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

