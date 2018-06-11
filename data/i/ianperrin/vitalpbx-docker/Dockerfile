FROM centos/systemd  
  
ENV HOME /root  
WORKDIR $HOME  
  
#Install wget command  
RUN \  
yum install wget -y;  
  
#Clean Yum Cache  
RUN \  
yum clean all;\  
rm -rf /var/cache/yum;  
  
#Download the beta repo of VitalPBX  
RUN \  
wget -P /etc/yum.repos.d/
https://raw.githubusercontent.com/VitalPBX/VPS/master/resources/vitalpbx.repo;  
  
#Install SSH Welcome Banner  
RUN \  
rm -rf /etc/profile.d/vitalwelcome.sh;\  
wget -P /etc/profile.d/
https://raw.githubusercontent.com/VitalPBX/VPS/master/resources/vitalwelcome.sh;\  
chmod 644 /etc/profile.d/vitalwelcome.sh;  
  
#Intall other required dependencies  
RUN \  
yum -y install epel-release php-5.4.16-42.el7;  
  
# Update the system & Clean Cache Again  
RUN \  
yum clean all;\  
rm -rf /var/cache/yum;\  
yum -y update;  
  
# Install VitalPBX pre-requisites  
RUN \  
wget
https://raw.githubusercontent.com/VitalPBX/VPS/master/resources/pack_list;\  
yum -y install $(cat pack_list);  
  
# Install VitalPBX  
RUN \  
mkdir -p /etc/ombutel;\  
mkdir -p /etc/asterisk/ombutel;\  
yum -y install vitalpbx vitalpbx-asterisk-configs vitalpbx-fail2ban-config
vitalpbx-sounds vitalpbx-themes dahdi-linux dahdi-tools dahdi-tools-doc kmod-
dahdi-linux fxload;  
  
# Speed up the localhost name resolving  
RUN \  
sed -i 's/^hosts.*$/hosts: myhostname files dns/' /etc/nsswitch.conf;  
  
# Set permissions  
RUN \  
chown -R apache:root /etc/asterisk/ombutel;  
  
# Restart httpd  
#RUN \  
# systemctl restart httpd;  
#Start ombutel-dbsetup  
#RUN \  
# systemctl start ombutel-dbsetup.service;  
# Enable the http access:  
#RUN \  
# firewall-cmd --add-service=http;\  
# firewall-cmd --reload;  
EXPOSE 3000/tcp 3005/tcp  
  
CMD ["/usr/sbin/init"]  

