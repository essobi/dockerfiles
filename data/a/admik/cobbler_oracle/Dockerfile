FROM oraclelinux:6  
#ENV ftp_proxy http://IP.AD.DR.ES:3128  
#ENV http_proxy http://IP.AD.DR.ES:3128  
#ENV https_proxy http://IP.AD.DR.ES:3128  
#ENV no_proxy IP.AD.DR.ES  
#RUN curl https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm -o /root/epel-release-6-8.noarch.rpm && yum
localinstall -y /root/epel-release-6-8.noarch.rpm && rm -f /root/epel-
release-6-8.noarch.rpm  
#RUN curl https://downloads.dell.com/FOLDER04161783M/1/OM-MgmtStat-Dell-Web-
LX-8.5.0-2372_A00.tar.gz -o /root/OM-MgmtStat-Dell-Web-
LX-8.5.0-2372_A00.tar.gz  
#RUN curl http://yum.oracle.com/public-yum-ol6.repo - o /root/public-yum-
ol6.repo  
RUN curl https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm -o epel-release-6-8.noarch.rpm && yum localinstall -y
epel-release-6-8.noarch.rpm && rm -f epel-release-6-8.noarch.rpm  
#RUN curl http://yum.oracle.com/public-yum-ol6.repo -o public-yum-ol6.repo  
#RUN rm -f /etc/yum.repos.d/*.repo  
#RUN mv public-yum-ol6.repo /etc/yum.repos.d  
#ADD epel6.repo /etc/yum.repos.d  
ADD setup.sh /root/  
#ADD OM-MgmtStat-Dell-Web-LX-8.5.0-2372_A00.tar.gz /root  
ADD script.sh /root/script.sh  
  
RUN yum -y install cobbler tftp-server httpd dhcp dnsmasq dnsmasq-utils telnet
git wget make automake tcpdump nmap screen mc tar  
RUN mkdir /tftpboot  
RUN sed -i 's/manage_dhcp: 0/manage_dhcp: 1/g' /etc/cobbler/settings  
RUN sed -i 's/manage_dns: 1/manage_dns: 0/g' /etc/cobbler/settings  
RUN sed -i 's/pxe_just_once: 0/pxe_just_once: 1/g' /etc/cobbler/settings  
RUN sed -i '10 i log-facility local7;' /etc/cobbler/dhcp.template  
RUN echo "*.debug,local6.none,local7.none /var/log/syslog" >>
/etc/rsyslog.conf  
RUN echo "local7.debug /var/log/dhcp/dhcpd.log" >> /etc/rsyslog.conf  
RUN curl https://downloads.dell.com/FOLDER04161783M/1/OM-MgmtStat-Dell-Web-
LX-8.5.0-2372_A00.tar.gz -o OM-MgmtStat-Dell-Web-LX-8.5.0-2372_A00.tar.gz  
RUN mv OM-MgmtStat-Dell-Web-LX-8.5.0-2372_A00.tar.gz /root/OM-MgmtStat-Dell-
Web-LX-8.5.0-2372_A00.tar.gz && cd /root && tar -xzf OM-MgmtStat-Dell-Web-
LX-8.5.0-2372_A00.tar.gz  
RUN cd /root/linux/rac/RHEL6/x86_64 && yum -y localinstall *.rpm && rm -rf
/root/linux /root/docs  
  
VOLUME [ " /var/lib/cobbler " ]  
VOLUME [ " /var/lib/cobbler/api_cobbler " ]  
VOLUME [ " /var/www/cobbler " ]  
VOLUME [ " /etc/cobbler " ]  
VOLUME [ " /etc/dhcp " ]  
VOLUME [ " /var/log " ]  
  
RUN cp -pr /var/lib/cobbler /var/lib/cobbler-default  
RUN cp -pr /var/www/cobbler /var/www/cobbler-default  
RUN cp -pr /etc/cobbler /etc/cobbler-default  
RUN cp -pr /etc/dhcp /etc/dhcp-default  
RUN echo "if [ -f /root/script.sh ]; then bash /root/script.sh; fi" >
/root/run_script.sh && chmod 755 /root/run_script.sh && chown root:root
/root/run_script.sh  
  
CMD /root/setup.sh && while true; do /root/run_script.sh; sleep 10; done  

