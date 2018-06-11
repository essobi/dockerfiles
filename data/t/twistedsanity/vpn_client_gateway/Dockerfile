FROM phusion/baseimage:latest  
MAINTAINER twistedsanity  
  
# Evironment variables  
ENV DEBIAN_FRONTEND=noninteractive  
# OPENVPN_USERNAME=**None** \  
# OPENVPN_PASSWORD=**None**  
# OPENVPN_PROVIDER=**None**  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Update packages and install software  
RUN \  
apt-get update && \  
apt-get install -y \  
apt-utils \  
dnsmasq \  
iptables \  
# iptables-persistent \  
openvpn \  
lighttpd \  
php-common \  
php-cgi php \  
php-curl \  
php-xml \  
wget \  
sudo \  
unzip \  
logrotate \  
traceroute \  
# Needed for testing  
whiptail \  
nano \  
iputils-ping \  
dnsutils \  
# End testing apps  
libterm-readline-gnu-perl && \  
apt-get clean && rm -rf /tmp/* /var/tmp/* && \  
# Get and install PIA files  
wget https://www.privateinternetaccess.com/openvpn/openvpn.zip && \  
unzip openvpn.zip -d ./openvpn && \  
cp openvpn/crl.rsa.2048.pem openvpn/ca.rsa.2048.crt /etc/openvpn && \  
  
# Create Password file  
touch /etc/openvpn/auth.txt && \  
echo $OPENVPN_USERNAME >> /etc/openvpn/auth.txt && \  
echo $OPENVPN_PASSWORD >> /etc/openvpn/auth.txt && \  
chmod 600 /etc/openvpn/auth.txt && \  
  
# Get and install vpn_client_gateway files  
wget https://github.com/twistedsanity/vpn_client_gateway/archive/master.zip &&
\  
unzip master.zip && \  
cp -rp vpn_client_gateway-master/www/* /var/www/html/ && \  
chown www-data:www-data /var/www/html/vpnmgmt && \  
  
sed -i \  
-e 's#daily#daily#g' \  
-e 's#rotate 4#rotate 4#g' \  
/etc/logrotate.conf && \  
  
echo "www-data ALL=(root) NOPASSWD: /usr/sbin/service"\ >>
/etc/sudoers.d/sudoers && \  
echo "www-data ALL=(root) NOPASSWD: /usr/sbin/update-rc.d"\ >>
/etc/sudoers.d/sudoers && \  
echo "www-data ALL=(root) NOPASSWD: /sbin/shutdown"\ >> /etc/sudoers.d/sudoers
&& \  
echo "www-data ALL=(root) NOPASSWD: /sbin/iptables"\ >> /etc/sudoers.d/sudoers
&& \  
echo "www-data ALL=(root) NOPASSWD: /sbin/iptables-save"\ >>
/etc/sudoers.d/sudoers && \  
echo "www-data ALL=(root) NOPASSWD: /bin/su" >> /etc/sudoers.d/sudoers && \  
# setup lighty  
usermod -a -G www-data root && \  
lighty-enable-mod fastcgi-php  
  
# Volumes  
VOLUME /etc/openvpn  
  
# Adding utils scripts to bin  
ADD bin/ /usr/local/bin/  
RUN \  
chmod +x /usr/local/bin/* && \  
# Copy over server.conf and set perms  
# cp -a /usr/local/bin/server.conf /etc/openvpn/server.conf && \  
# chown www-data:www-data /etc/openvpn/server.conf && \  
# Running scripts during container startup  
mkdir -p /etc/my_init.d && \  
#ln -s /usr/local/bin/vpn_gw-run.sh /etc/my_init.d/vpn_gw-run.sh && \  
cp -a /usr/local/bin/vpn_gw-run.sh /etc/my_init.d/vpn_gw-run.sh && \  
chmod +x /etc/my_init.d/* && \  
  
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf && \  
echo "net.ipv6.conf.all.disable_ipv6=1" >> /etc/sysctl.conf && \  
  
sysctl -p /etc/sysctl.conf  

