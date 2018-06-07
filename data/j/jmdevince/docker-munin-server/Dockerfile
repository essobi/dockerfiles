FROM debian:stable-slim  
  
MAINTAINER James DeVincentis <james.d@hexhost.net>  
  
RUN apt-get update -qq && RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -qq cron munin munin-node nginx apache2-utils wget
heirloom-mailx patch spawn-fcgi  
RUN rm /etc/nginx/sites-enabled/default  
RUN rm -f /etc/munin/plugins/*  
RUN ln -s /usr/share/munin/plugins/munin_stats /etc/munin/plugins/munin_stats  
  
VOLUME /var/lib/munin  
VOLUME /var/log/munin  
  
ADD ./munin.conf /etc/munin/munin.conf  
ADD ./nginx-munin /etc/nginx/sites-enabled/munin  
  
ADD ./launch-munin.sh /launch-munin.sh  
  
EXPOSE 8080  
CMD ["/bin/bash", "/launch-munin.sh"]  

