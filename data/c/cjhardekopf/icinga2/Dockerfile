FROM cjhardekopf/confd  
MAINTAINER Chris Hardekopf <cjh@ygdrasill.com>  
  
# Install software-properties-common and msmtp, add the icinga ppa, and
install  
# everything  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
msmtp msmtp-mta && \  
add-apt-repository -y ppa:formorer/icinga && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y icinga2 icinga2-ido-mysql icinga-web \  
nagios-plugins nagios-plugins-contrib nagios-plugins-extra \  
nagios-nrpe-plugin && \  
rm -rf /var/lib/apt/lists/*  
  
# The icinga 2 ido-mysql module should be configured dynamically and the  
# server needs to be started. Icinga 2 configuration is pretty involved and  
# and needs to be configured by the end user and should therefore by in a  
# /data directory. On start with an empty /data directory the configuration  
# will be copied from /etc/icinga2 before changing /etc/icinga2 into a soft  
# like to the configuration directory in /data.  
ADD icinga2-mysql.conf.tmpl /etc/confd/templates/  
ADD icinga2.toml /etc/confd/conf.d/  
ADD icinga2-command /opt/  
ADD icinga2.conf /etc/supervisor/conf.d/  
  
# We need to configure ixinga-web and start the web server (apache).  
ADD databases.xml.tmpl /etc/confd/templates/  
ADD icinga-web.toml /etc/confd/conf.d/  
ADD icinga-web-command /opt/  
ADD icinga-web.conf /etc/supervisor/conf.d/  
  
# We need to dynamically configure msmtp so that we can send mail  
# (there is no server to start or restart)  
ADD msmtprc.tmpl /etc/confd/templates/  
ADD msmtp.toml /etc/confd/conf.d/  
  
# Expose port 80 for icinga-web  
EXPOSE 80  
CMD [ "/opt/start" ]  
  

