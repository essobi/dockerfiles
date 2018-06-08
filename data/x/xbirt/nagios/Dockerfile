FROM jasonrivers/nagios  
RUN apt-get update && apt-get install -y \  
smbclient \  
ipmitool \  
&& \  
sed -i 's/syslog = 0/#syslog = 0/g' /etc/samba/smb.conf \  
&& \  
echo "docker:x:1101:nagios" >> /etc/group \  
&& \  
apt-get clean && rm -Rf /var/lib/apt/lists/*  

