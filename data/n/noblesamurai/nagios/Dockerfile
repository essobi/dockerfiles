FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NAGIOSADMIN_USER nagiosadmin  
ENV NAGIOSADMIN_PASS nagios  
ENV NAGIOS_USER_CONF_DIR /opt/nagios/userconf  
  
# Use closest ubuntu mirrors (prepend necessary lines to sources.list)  
ADD ubuntu-mirrors /tmp/ubuntu-mirrors  
RUN cat /tmp/ubuntu-mirrors /etc/apt/sources.list > /tmp/sources.list && mv
/tmp/sources.list /etc/apt/sources.list  
  
# Install reqd deps  
RUN apt-get update  
RUN apt-get install -y \  
nagios3 \  
nagios-plugins \  
nagios-nrpe-plugin \  
supervisor \  
curl  
  
# Configure apache and the nagios daemon to start on boot  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Set the username/password  
RUN mkdir -p /etc/my_init.d  
ADD htpasswd.sh /etc/my_init.d/htpasswd.sh  
RUN chmod u+x /etc/my_init.d/htpasswd.sh  
  
# Enable external commands  
RUN sed -i "s,check_external_commands=0,check_external_commands=1,"
/etc/nagios3/nagios.cfg  
# Allow www-data to write to the command file.  
RUN usermod -a -G nagios www-data  
# Hack around weird things that were meaning no permission.  
RUN rm -rf /var/lib/nagios3/rw  
RUN mkdir /var/lib/nagios3/rw && chown nagios:www-data /var/lib/nagios3/rw &&
chmod 750 /var/lib/nagios3/rw  
RUN mkfifo /var/lib/nagios3/rw/nagios.cmd && chown nagios:nagios
/var/lib/nagios3/rw/nagios.cmd && chmod 660 /var/lib/nagios3/rw/nagios.cmd  
  
# Create user config dir in case nothing is mounted there  
RUN mkdir -p $NAGIOS_USER_CONF_DIR  
# Enable user config to be mounted into /opt/nagios/userconf  
RUN echo "cfg_dir=${NAGIOS_USER_CONF_DIR}" >> /etc/nagios3/nagios.cfg  
  
# Clean up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

