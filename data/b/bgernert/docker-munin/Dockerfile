# Use official Ubuntu release  
FROM ubuntu:latest  
  
# Maintainer  
LABEL maintainer="Björn Gernert <mail@bjoern-gernert.de>"  
  
# Update Ubuntu image  
RUN apt-get -qq update && apt-get -qq upgrade  
  
# Install Munin  
RUN apt-get -qq install --no-install-recommends munin cron rsyslog logrotate
iputils-ping telnet  
  
# Clean up updates/install  
RUN apt-get -qq autoclean && apt-get -qq autoremove && apt-get -qq clean  
  
# Create munin run dir  
RUN mkdir /var/run/munin && chown munin:munin /var/run/munin  
  
# Change some default Munin configuration settings  
RUN sed -i 's|^#dbdir\t/var/lib/munin|dbdir /docker/dbdir|g'
/etc/munin/munin.conf  
RUN sed -i 's|^#htmldir /var/cache/munin/www|htmldir /docker/www|g'
/etc/munin/munin.conf  
RUN sed -i 's|^#logdir /var/log/munin|logdir /docker/log|g'
/etc/munin/munin.conf  
RUN sed -i 's|^#tmpldir\t/etc/munin/templates|tmpldir /docker/etc/templates|g'
/etc/munin/munin.conf  
RUN sed -i 's|^#staticdir /etc/munin/static|staticdir /docker/etc/static|g'
/etc/munin/munin.conf  
RUN sed -i 's|^includedir /etc/munin/munin-conf.d|includedir
/docker/etc/munin-conf.d|g' /etc/munin/munin.conf  
RUN sed -i 's|^\\[localhost\\.localdomain\\]|#\\[localhost\\.localdomain\\]|g'
/etc/munin/munin.conf  
RUN sed -i 's|^ address 127.0.0.1|# address 127.0.0.1|g' /etc/munin/munin.conf  
RUN sed -i 's|^ use_node_name yes|# use_node_name yes|g' /etc/munin/munin.conf  
  
# Change logrotate configuration for Munin  
RUN sed -i 's|^/var/log/munin/|/docker/log/|g' /etc/logrotate.d/munin  
  
# Change config file for munin  
RUN sed -i 's|then /usr/bin/munin-cron|then /usr/bin/munin-cron --config
/docker/etc/munin.conf|g' /etc/cron.d/munin  
RUN sed -i 's|then /usr/share/munin/munin-limits|then /usr/share/munin/munin-
limits --config /docker/etc/munin.conf|g' /etc/cron.d/munin  
  
# Export volumes  
VOLUME /docker  
  
# Copy scripts and configurations files into container  
ADD start_munin /root/start_munin  
  
# Allow execution of start script  
RUN chmod u+x /root/start_munin  
  
# Start cups  
CMD ["/root/start_munin"]  

