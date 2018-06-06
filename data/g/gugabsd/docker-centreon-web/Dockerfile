FROM centos:7  
# Install dependences package  
RUN yum install --nogpgcheck -y \  
http://yum.centreon.com/standard/3.4/el7/stable/noarch/RPMS/centreon-
release-3.4-4.el7.centos.noarch.rpm \  
&& yum install -y epel-release \  
&& yum install -y --skip-broken \  
centreon \  
centreon-engine \  
centreon-license-manager \  
centreon-pp-manager \  
centreon-widget-* \  
centreon-plugin-Hardware-Printers-Generic-Snmp \  
centreon-plugin-Applications-* \  
centreon-plugin-Operatingsystems-Linux-Snmp \  
centreon-plugin-Operatingsystems-Windows-Snmp \  
centreon-plugin-Network-Cisco-Standard-Snmp \  
centreon-nrpe-plugin \  
nagios-plugins-snmp \  
nagios-plugins-perl \  
nagios-plugins-ping \  
nagios-plugins-icmp \  
nagios-plugins-nrpe \  
nrpe-plugin \  
openssh-clients \  
wget \  
sudo \  
postfix \  
rsyslog \  
python-devel \  
&& yum clean all  
  
# Install supervisor and requests by pip and configure  
RUN wget -O - https://bootstrap.pypa.io/get-pip.py | python - \  
&& pip install supervisor requests \  
&& echo_supervisord_conf > /etc/supervisord.conf \  
&& mkdir /etc/supervisor.d \  
&& echo '[include]' >> /etc/supervisord.conf \  
&& echo 'files = /etc/supervisor.d/*.conf' >> /etc/supervisord.conf  
  
# Add postfix-wrapper  
# From: https://www.snip2code.com/Snippet/309436/postfix-wrapper-sh-for-
supervisord-in-do  
COPY ./files/supervisord/postfix-wrapper.sh /usr/local/sbin/  
RUN chmod +x /usr/local/sbin/postfix-wrapper.sh  
  
# Copy supervisor configuration services  
COPY ./files/supervisord/cbd.conf /etc/supervisor.d/  
COPY ./files/supervisord/centcore.conf /etc/supervisor.d/  
COPY ./files/supervisord/centengine.conf /etc/supervisor.d/  
COPY ./files/supervisord/crond.conf /etc/supervisor.d/  
COPY ./files/supervisord/httpd.conf /etc/supervisor.d/  
COPY ./files/supervisord/postfix.conf /etc/supervisor.d/  
COPY ./files/supervisord/rsyslog.conf /etc/supervisor.d/  
  
# Add fake init scripts (used by centreon web)  
COPY ./files/init-fake/centengine /etc/init.d/centengine  
COPY ./files/init-fake/centcore /etc/init.d/centcore  
COPY ./files/init-fake/cbd /etc/init.d/cbd  
RUN chmod +x \  
/etc/init.d/centengine \  
/etc/init.d/centcore \  
/etc/init.d/cbd  
  
# Set the ssh keys to user centreon (necessary to communication with engine)  
RUN mkdir -p /var/spool/centreon/.ssh \  
&& ssh-keygen -t rsa -N '' -f /var/spool/centreon/.ssh/id_rsa \  
&& touch /var/spool/centreon/.ssh/known_hosts \  
&& chmod -R 700 /var/spool/centreon/.ssh \  
&& chown -R centreon:centreon /var/spool/centreon/.ssh \  
&& echo -e "\tStrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  
# Centreon config  
COPY ./files/central-broker.xml /etc/centreon/  
COPY ./files/central-rrd.xml /etc/centreon/  
COPY ./files/poller-module.xml /etc/centreon/  
COPY ./files/watchdog.xml /etc/centreon/  
COPY ./files/conf.pm /etc/centreon/  
COPY ./files/centreon.conf.php /etc/centreon/  
  
# Install custom plugins  
COPY ./files/plugins/check_rbl.py /usr/lib/nagios/plugins/  
COPY ./files/plugins/send_sms.py /usr/lib/nagios/plugins/  
# Add compatibility path of check's nagios  
RUN ln -s /usr/lib64/nagios/plugins/check_ping
/usr/lib/nagios/plugins/check_ping \  
&& ln -s /usr/lib64/nagios/plugins/check_snmp
/usr/lib/nagios/plugins/check_snmp \  
&& ln -s /usr/lib64/nagios/plugins/check_icmp
/usr/lib/nagios/plugins/check_icmp \  
&& chmod u+s /usr/bin/ping  
  
EXPOSE 80  
EXPOSE 5669  
COPY ./files/start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Start default container command  
CMD ["/start.sh"]  

