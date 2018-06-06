FROM ubuntu:14.04  
MAINTAINER DEFENSATIVE Docker Mantainers "docker-maint@defensative.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV OpenVPN-Client 1.0  
RUN apt-get update && \  
apt-get install -y openvpn sqlite3 rdnssd openssh-server python2.7 && \  
\  
echo "" >> /etc/network/interfaces && \  
echo "allow-hotplug tap0" >> /etc/network/interfaces && \  
echo "iface tap0 inet manual" >> /etc/network/interfaces && \  
echo "iface tap0 inet6 dhcp" >> /etc/network/interfaces && \  
echo " autoconf 1" >> /etc/network/interfaces && \  
echo " accept_ra 2" >> /etc/network/interfaces && \  
echo "send fqdn.fqdn = gethostname();" >> /etc/dhcp/dhclient.conf && \  
echo "send fqdn.encoded on;" >> /etc/dhcp/dhclient.conf && \  
echo "send fqdn.server-update off;" >> /etc/dhcp/dhclient.conf && \  
echo "also request fqdn, dhcp6.fqdn;" >> /etc/dhcp/dhclient.conf && \  
mkdir -p /root/.ssh && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDaEffssajs/mit5aLygUetlTyl5PnxDfuqwII9VgePi4+rugOkdDfTvBHGsm8kml/G+PVAxAgeC0uMONEe1wteecMk3PYxnk2XREeKvZKeuwIHWhwi8Ejg2dHfvJycag07SomzbHRRnpYihnl0XWVm+tsfnbaJe3Fi78zCMXQrV+ENXMzukGPhilGHsO8PMiQfYqLY3vIwAvyvb7qzHDM5jbJbW2rzmg5QJubMW0Dzala0KjL9+d6iQ19XlygjuZUyCm4V8cF2Kz1GH0eDdlxRBMXgSeHw5On39Z4tMEPsUt3WDZ5uKhTwOvLOAaAr+H1hx7OckSA3LomfwqRmweed
root@debian-router" > /root/.ssh/authorized_keys && \  
\  
apt-get purge -y man && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
(dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg -P || true) && \  
rm -Rf /tmp/* && \  
rm -Rf /var/lib/apt/lists/*.gz && \  
rm -Rf /var/lib/cache/* && \  
rm -Rf /var/lib/log/* && \  
rm -Rf /var/log/* && \  
rm -Rf /var/cache/*  
  
ADD up /etc/openvpn/up  
ADD run.sh /sbin/run.sh  
ADD down /etc/openvpn/down  
#ADD smoke_test.py /usr/sbin/smoke_test.py  
ENTRYPOINT ["/sbin/run.sh"]  
CMD ["--status", "/var/run/openvpn.client.status", "10", "--cd",
"/etc/openvpn", \  
"--config", "/etc/openvpn/client.conf", "--fragment", "1300", "--connect-
retry-max", "0"]  

