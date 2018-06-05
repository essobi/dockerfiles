FROM barkingiguana/base  
  
MAINTAINER Craig R Webster <craig@barkingiguana.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq apache2 nagios3  
  
RUN usermod -a -G nagios www-data  
RUN chmod -R g+x /var/lib/nagios3/  
RUN sed -i 's/check_external_commands=0/check_external_commands=1/g'
/etc/nagios3/nagios.cfg  
  
ADD ./nagios.cfg /etc/nagios3/nagios.cfg  
ADD ./cgi.cfg /etc/nagios3/cgi.cfg  
ADD ./htpasswd /etc/nagios3/htpasswd.users  
ADD ./apache2.envvars /etc/apache2/envvars  
ADD ./start-app.sh /usr/local/sbin/start-app.sh  
RUN chmod +x /usr/local/sbin/start-app.sh  
CMD [ "/usr/local/sbin/start-app.sh" ]  
EXPOSE 80  
RUN rm -rf /etc/nagios3/conf.d/* /etc/nagios3/commands.cfg  
ADD ./conf.d /etc/nagios3/conf.d/000_base  
ONBUILD ADD ./conf.d /etc/nagios3/conf.d/001_local  

