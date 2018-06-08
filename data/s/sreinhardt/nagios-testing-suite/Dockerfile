#NCPA  
#start with my cent build  
FROM sreinhardt/centos-6-x86_64:latest  
  
MAINTAINER Spenser Reinhardt  
  
ENV nagios_user nagios  
ENV nagios_group nagios  
ENV plugins_version 2.0.3  
# deps  
RUN yum install -y wget httpd php gcc glibc glibc-common gd gd-devel make net-
snmp automake autoconf \  
openssl-devel mysql-devel fping perl-Net-SNMP openssh-devel net-snmp-utils
bind-utils samba-client gettext  
  
#copy and build  
WORKDIR /tmp  
RUN curl
"http://assets.nagios.com/downloads/ncpa/download.php?type=rpm&arch=x86_64&os=el6"
-o /tmp/ncpa.rpm  
RUN yum localinstall --nogpgcheck ncpa.rpm -y  
  
# users and groups  
RUN groupadd ${nagios_group}  
RUN usermod -a -G ${nagios_group} nagios  
  
#Add config  
ADD ncpa.cfg /usr/local/ncpa/etc/ncpa.cfg  
  
#add and untar plugins  
WORKDIR /tmp/  
ADD https://github.com/nagios-plugins/nagios-
plugins/archive/release-${plugins_version}.tar.gz /tmp/nagios-
plugins-${plugins_version}.tar.gz  
RUN tar xzvf nagios-plugins-${plugins_version}.tar.gz  
  
# change per version  
WORKDIR nagios-plugins-release-2.0.3/  
  
# build and install plugins  
RUN ./tools/setup  
RUN ./configure --with-nagios-user=${nagios_user} \--with-nagios-
group=${nagios_group} \--prefix=/usr/local/ncpa
--libexecdir=/usr/local/ncpa/plugins  
RUN make  
RUN make install  
  
#Post-build docker info  
EXPOSE 5693  
WORKDIR /usr/local/ncpa/  
ENTRYPOINT ["/usr/local/ncpa/ncpa_posix_listener"]  
CMD ["--start", "--nodaemon"]  

