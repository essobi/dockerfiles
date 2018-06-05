FROM rickyb/centos70-systemd-httpd  
RUN yum -y install cacti rrdtool php-pecl-rrd net-snmp; yum clean all;
systemctl enable httpd.service  
RUN yum -y install iperf iperf3 mtr nmap nmap-ncat; yum clean all;  
EXPOSE 80 22  
CMD ["/usr/sbin/init"]  

