#This dockerfile uses the centos image  
#Author: mygithublab@126.com  
#Nagios core with Nagiosgraph  
#Basic image  
FROM centos:6.8  
#Maintainer information  
MAINTAINER mygithublab (mygithublab@126.com)  
#Setup environment  
ENV NAGIOSADMIN_USER nagiosadmin  
ENV NAGIOSADMIN_PASS nagios  
  
#Prerequisites Software  
RUN yum install -y \  
#Prerequisties software for NagiosCore  
gcc \  
glibc \  
php-cli \  
glibc-common \  
wget \  
unzip \  
httpd \  
php \  
gd \  
gd-devel \  
perl \  
#Prerequisties software for NagiosPlugin  
make \  
gettext \  
automake \  
autoconf \  
openssl-devel \  
net-snmp \  
net-snmp-utils \  
epel-release \  
##perl-Net-SNMP \  
#Prerequisties software for SSH Git  
openssh-server \  
git \  
#Prerequisties softeare for NagiosGraph  
perl-rrdtool \  
perl-GD \  
perl-CPAN \  
perl-CGI \  
perl-Time-HiRes \  
#Prerequisties software for SnmpPrinter  
php-snmp \  
bc \  
#Prerequisties software for HPilo2health  
perl-XML-Simple \  
perl-IO-Socket-SSL \  
#Prerequisties software for HPEProLiantServer  
nmap \  
procmail \  
curl \  
libtdb \  
##perl-Nagios-Plugin  
&& yum install -y \  
perl-Net-SNMP \  
perl-Nagios-Plugin \  
#Prerequisties software for DellEMCOpenManage  
perl-Socket6 \  
libwsman1 \  
openwsman-perl \  
net-snmp-perl \  
snmptt \  
#Edit snmptt.ini for DellEMCOpenManage  
&& sed -i 's/dns_enable = 0/dns_enable = 1/g' /etc/snmp/snmptt.ini \  
&& sed -i 's/net_snmp_perl_enable = 0/net_snmp_perl_enable = 1/g'
/etc/snmp/snmptt.ini \  
&& sed -i 's/translate_log_trap_oid = 0/translate_log_trap_oid = 1/g'
/etc/snmp/snmptt.ini \  
&& sed -i 's/stdout_enable = 0/stdout_enable = 1/g' /etc/snmp/snmptt.ini \  
&& sed -i 's/log_system_enable = 0/log_system_enable = 1/g'
/etc/snmp/snmptt.ini \  
&& sed -i 's/unknown_trap_log_enable = 0/unknown_trap_log_enable = 1/g'
/etc/snmp/snmptt.ini \  
&& sed -i 's/DEBUGGING = 0/DEBUGGING = 1/g' /etc/snmp/snmptt.ini \  
&& sed -i 's/DEBUGGING_FILE = /DEBUGGING_FILE = \/var\/log\/snmptt.debugg/g'
/etc/snmp/snmptt.ini \  
&& sed -i 's/DEBUGGING_FILE_HANDLER = /DEBUGGING_FILE_HANDLER =
\/var\/log\/snmptt\/snmptthandler.debug/g' /etc/snmp/snmptt.ini \  
&& sed -i '$a traphandle default \/usr\/sbin\/snmptthandler'
/etc/snmp/snmptrapd.conf \  
&& sed -i '$a disableAuthorization yes' /etc/snmp/snmptrapd.conf \  
#Configure snmptt snmptrapd services to start on OS boot  
&& chkconfig snmptrapd on && chkconfig snmptt on && service snmptt start &&
service snmptrapd start \  
#Install and setup Nagios::Config perl module  
&& wget http://xrl.us/cpanm -O /usr/bin/cpanm && chmod +x /usr/bin/cpanm &&
cpanm Nagios::Config \  
#Prerequisties software for TCPTraffice  
&& cpanm Carp English File::Basename Monitoring::Plugin
Monitoring::Plugin::Getopt Monitoring::Plugin::Threshold
Monitoring::Plugin::Range Readonly version \  
#Prerequisties software for DellEMCOpenManage - Perl Net-IP Module  
&& cd /tmp \  
&& wget http://search.cpan.org/CPAN/authors/id/M/MA/MANU/Net-IP-1.26.tar.gz \  
&& tar -zxvf Net-IP-1.26.tar.gz && cd Net-IP-1.26 \  
&& perl Makefile.PL && make && make all && make install \  
#Prerequisties software for DellEMCOpenManage - Perl Net-SNMP Module  
&& cd /tmp \  
&& wget http://search.cpan.org/CPAN/authors/id/D/DT/DTOWN/Net-
SNMP-v6.0.1.tar.gz \  
&& tar -zxvf Net-SNMP-v6.0.1.tar.gz && cd Net-SNMP-v6.0.1 \  
&& perl Makefile.PL && make && make all && make install \  
#Prerequisties software for DellEMCOpenManage - DellRACADM  
&& cd /tmp \  
&& wget -q -O- http://linux.dell.com/repo/hardware/latest/bootstrap.cgi | bash
\  
&& yum install -y \  
srvadmin-idrac7 \  
java-1.8.0-openjdk \  
java-1.8.0-openjdk-devel \  
#Clean repo cache  
&& yum clean all  
  
  
#Download to Install Nagios Core 4.3.4 and plugin  
#Add HPEProLiantServer ILO Agentless Management RPM package  
#Add DellEMCOpenManage package  
ADD plugins/nagios-plugins-hpeilo-1.5.1-156.9.rhel6.x86_64.rpm /tmp  
ADD plugins/Dell_EMC_OpenManage_Plugin_v2.1_Nagios_Core_A00.tar.gz /tmp  
#Create User And Group  
RUN useradd nagios && groupadd nagcmd && usermod -a -G nagcmd nagios &&
usermod -a -G nagcmd apache && usermod -a -G nagios apache && cd /tmp \  
#Downloading NagiosCore  
&& wget \--no-check-certificate -O nagioscore.tar.gz
https://github.com/NagiosEnterprises/nagioscore/archive/nagios-4.3.4.tar.gz \  
#Extract NagiosCore  
&& tar xzvf nagioscore.tar.gz && cd /tmp/nagioscore-nagios-4.3.4/ \  
#Compile NagiosCore  
&& ./configure && make all \  
#Install NagiosCore  
&& make install \  
#Install NagiosCore Service Daemon  
&& make install-init && chkconfig \--add nagios && chkconfig \--level 2345
httpd on \  
#Install NagiosCore Command Mode  
&& make install-commandmode \  
#Install NagiosCore Configuration  
&& make install-config \  
#Install NagiosCore ApacheConfig  
&& make install-webconf \  
#Configure Firewall for NagiosCore  
#&& iptables -I INPUT -p tcp --destination-port 80 -j ACCEPT && service
iptables save \  
#&& ip6tables -I INPUT -p tcp --destination-port 80 -j ACCEPT && service
ip6tables save \  
#Create Nagiosadmin User Account  
&& htpasswd -bcs /usr/local/nagios/etc/htpasswd.users "${NAGIOSADMIN_USER}"
"${NAGIOSADMIN_PASS}" \  
  
#Downloading NagiosPlugin  
&& cd /tmp && wget \--no-check-certificate -O nagios-plugins.tar.gz
https://github.com/nagios-plugins/nagios-plugins/archive/release-2.2.1.tar.gz
\  
#Extract NagiosPlugin  
&& tar zxvf nagios-plugins.tar.gz && cd /tmp/nagios-plugins-release-2.2.1/ \  
#Compile + Install for NagiosPlugin  
&& ./tools/setup && ./configure && make && make install \  
  
#Downloading NagiosNRPE  
&& cd /tmp && wget \--no-check-certificate -O nrpe.tar.gz
https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-3.2.1/nrpe-3.2.1.tar.gz
\  
#Install NagiosNRPE  
&& tar zxvf nrpe.tar.gz && cd /tmp/nrpe-3.2.1 \  
&& ./configure && make check_nrpe && make install-plugin \  
  
#Downloading NagiosGraph  
&& cd /tmp && wget \--no-check-certificate -O nagiosgraph.tar.gz
https://nchc.dl.sourceforge.net/project/nagiosgraph/nagiosgraph/1.5.2/nagiosgraph-1.5.2.tar.gz
\  
#Install NagiosGraph  
&& tar zxvf nagiosgraph.tar.gz && cd /tmp/nagiosgraph-1.5.2 \  
&& ./install.pl \--install \  
\--prefix /usr/local/nagiosgraph \  
\--etc-dir /usr/local/nagiosgraph/etc \  
\--var-dir /usr/local/nagiosgraph/var \  
\--log-dir /usr/local/nagiosgraph/var/log \  
\--doc-dir /usr/local/nagiosgraph/doc \  
\--nagios-cgi-url /nagiosgraph/cgi-bin \  
\--nagios-perfdata-file /tmp/perfdata.log \  
\--nagios-user nagios \  
\--www-user apache \  
# --prefix /opt/nagiosgraph \  
# --nagios-user nagios \  
# --www-user apache \  
# --nagios-perfdata-file /tmp/perfdata.log \  
# --nagios-cgi-url /nagiosgraph/cgi-bin && \  
&& cp share/nagiosgraph.ssi /usr/local/nagios/share/ssi/common-header.ssi \  
#Install HPEProLiantServer  
&& cd /tmp && chmod 755 /tmp/nagios-plugins-
hpeilo-1.5.1-156.9.rhel6.x86_64.rpm \  
&& rpm -ivh nagios-plugins-hpeilo-1.5.1-156.9.rhel6.x86_64.rpm \  
#Install DellEMCOpenManage  
&& cd /tmp/Dell_OpenManage_Plugin/Install \  
&& ./install.sh \  
#Check and server NagiosCore  
&& /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg \  
#Create index.html file and setup Shanghai timezone  
&& touch /var/www/html/index.html && cat /usr/share/zoneinfo/Asia/Shanghai >
/etc/localtime \  
&& rm -rf /tmp/*  
  
#Add startup service script  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh && mkdir -p /root/.ssh  
COPY authorized_keys /root/.ssh  
RUN chmod 700 /root/.ssh && chmod 600 /root/.ssh/authorized_keys  
#Add configure file to NagiosCore  
ADD cfg/httpd/httpd.conf /etc/httpd/conf/httpd.conf  
ADD cfg/nagiosgraph/etc/nagiosgraph-apache.conf
/usr/local/nagiosgraph/etc/nagiosgraph-apache.conf  
ADD cfg/nagiosgraph/etc/nagiosgraph.conf
/usr/local/nagiosgraph/etc/nagiosgraph.conf  
ADD cfg/nagios/etc/cgi.cfg /usr/local/nagios/etc/cgi.cfg  
ADD cfg/nagios/etc/nagios.cfg /usr/local/nagios/etc/nagios.cfg  
ADD cfg/nagios/objects/commands.cfg /usr/local/nagios/etc/objects/commands.cfg  
ADD cfg/nagios/objects/templates.cfg
/usr/local/nagios/etc/objects/templates.cfg  
ADD cfg/nagios/objects/test.cfg /usr/local/nagios/etc/objects/test.cfg  
#Add plugin to NagiosCore  
ADD plugins/check_ilo2_health.pl
/usr/local/nagios/libexec/check_ilo2_health.pl  
ADD plugins/check_snmp_printer /usr/local/nagios/libexec/check_snmp_printer  
ADD plugins/check_mem.pl /usr/local/nagios/libexec/check_mem.pl  
ADD plugins/check_tcptraffic /usr/local/nagios/libexec/check_tcptraffic  
#Change above file permission  
  
RUN chmod 755 /usr/local/nagios/libexec/check_ilo2_health.pl \  
&& chmod 755 /usr/local/nagios/libexec/check_snmp_printer \  
&& chmod 755 /usr/local/nagios/libexec/check_mem.pl \  
&& chmod 755 /usr/local/nagios/libexec/check_tcptraffic \  
&& chown nagios.nagios /usr/local/nagios/etc/cgi.cfg \  
/usr/local/nagios/etc/nagios.cfg \  
/usr/local/nagios/etc/objects/commands.cfg \  
/usr/local/nagios/etc/objects/templates.cfg \  
&& chmod 664 /usr/local/nagios/etc/cgi.cfg \  
/usr/local/nagios/etc/nagios.cfg \  
/usr/local/nagios/etc/objects/commands.cfg \  
/usr/local/nagios/etc/objects/templates.cfg \  
/usr/local/nagios/etc/objects/test.cfg \  
&& /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg  
#Export service ports  
EXPOSE 80 22  
  
#Export container folder  
VOLUME "/mnt"  
#ENTRYPOINT ["executable","/run.sh"]  
CMD ["/run.sh"]  

