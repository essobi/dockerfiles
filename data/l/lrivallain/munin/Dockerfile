FROM ubuntu:14.04  
MAINTAINER lrivallain (https://github.com/lrivallain) - based on Arcus
("http://arcus.io") work  
  
# install and configure munin  
RUN apt-get update -qq && RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -qq cron munin munin-node nginx apache2 wget  
RUN (cp /etc/munin/apache.conf /etc/apache2/sites-available/000-default.conf)  
RUN (sed -i 's/^Alias.*/Alias \/ \/var\/cache\/munin\/www\//g'
/etc/apache2/sites-available/000-default.conf)  
RUN (sed -i 's/Allow from .*/Satisfy Any/g' /etc/apache2/sites-
available/000-default.conf)  
RUN (sed -i 's/Order allow,deny.*/Allow from all/g' /etc/apache2/sites-
available/000-default.conf)  
RUN (mkdir -p /var/run/munin && chown -R munin:munin /var/run/munin)  
  
# copy launcher  
ADD run.sh /usr/local/bin/run  
  
# persist  
VOLUME /var/lib/munin  
VOLUME /var/log/munin  
VOLUME /var/cache/munin  
  
EXPOSE 80  
# launcher  
CMD ["/usr/local/bin/run"]  

