# Shinken Docker installation using pip (latest)  
FROM debian:wheezy  
MAINTAINER Sergey Kozlov  
  
# Install Shinken, Nagios plugins, nginx and supervisord  
RUN apt-get update && apt-get install -y python-pip \  
python-pycurl \  
python-cherrypy3 \  
python-zmq \  
python-pika \  
nagios-plugins \  
libsys-statistics-linux-perl \  
nginx \  
supervisor && \  
apt-get -y autoremove && \  
apt-get clean  
RUN useradd --create-home shinken && \  
pip install shinken==2.0.3 && \  
pip install pymongo && \  
update-rc.d -f shinken remove  
  
# Install shinken modules from shinken.io  
RUN su - shinken -c 'shinken --init' && \  
su - shinken -c 'shinken install webui' && \  
su - shinken -c 'shinken install auth-htpasswd' && \  
su - shinken -c 'shinken install sqlitedb' && \  
su - shinken -c 'shinken install retention-mongodb' && \  
su - shinken -c 'shinken install pickle-retention-file-scheduler' && \  
su - shinken -c 'shinken install booster-nrpe'  
  
# Configure nginx  
ADD shinken/shinken_nginx.conf /etc/nginx/sites-available/shinken_nginx.conf  
RUN mkdir -p /var/log/nginx && \  
rm -f /etc/nginx/sites-enabled/default && \  
ln -sf /etc/nginx/sites-available/shinken_nginx.conf /etc/nginx/sites-
enabled/shinken_nginx.conf && \  
update-rc.d -f nginx remove && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Configure Shinken modules  
ADD shinken/shinken.cfg /etc/shinken/shinken.cfg  
ADD shinken/broker-master.cfg /etc/shinken/brokers/broker-master.cfg  
ADD shinken/poller-master.cfg /etc/shinken/pollers/poller-master.cfg  
ADD shinken/scheduler-master.cfg /etc/shinken/schedulers/scheduler-master.cfg  
ADD shinken/webui.cfg /etc/shinken/modules/webui.cfg  
RUN mkdir -p /etc/shinken/custom_configs /usr/local/custom_plugins && \  
ln -sf /etc/shinken/custom_configs/htpasswd.users /etc/shinken/htpasswd.users  
  
# Configure monitorian mongodb arbiter module  
ADD monitorian/import-monitorian /var/lib/shinken/modules/import-monitorian  
ADD monitorian/import-monitorian.cfg /etc/shinken/modules/import-
monitorian.cfg  
  
RUN rm /etc/shinken/arbiters/arbiter-master.cfg  
ADD monitorian/arbiter-master.cfg /etc/shinken/arbiters/arbiter-master.cfg  
  
# Configure monitorian zmq notifier command  
ADD monitorian/notify-ce.cfg /etc/shinken/commands/notify-ce.cfg  
ADD monitorian/notify-ce /usr/local/bin/notify-ce  
  
# Configure mongodb retention  
ADD shinken/retention-mongodb.cfg /etc/shinken/modules/retention-mongodb.cfg  
  
# Copy extra NRPE plugins and fix permissions  
ADD extra_plugins/* /usr/lib/nagios/plugins/  
RUN cd /usr/lib/nagios/plugins/ && \  
chmod a+x * && \  
chmod u+s check_apt restart_service check_ping check_icmp check_fping
apt_update  
  
# Define mountable directories  
VOLUME ["/etc/shinken/custom_configs", "/usr/local/custom_plugins"]  
  
# configure supervisor  
ADD supervisor/conf.d/* /etc/supervisor/conf.d/  
  
# Add runner script  
#ADD monitorian/run.sh /run.sh  
#CMD chmod +x /run.sh  
# Expost port 80 (nginx)  
EXPOSE 80  
# Default docker process  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  
#CMD ["/run.sh"]  

