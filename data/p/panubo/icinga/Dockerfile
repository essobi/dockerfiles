FROM centos:5  
# Provide Entrypoint that Docker won't override  
RUN cp -a /sbin/init /sbin/init.real  
  
ADD *.txt /tmp/  
  
RUN rpm --import /tmp/RPM-GPG-KEY-CentOS-5.txt && \  
rpm --import /tmp/RPM-GPG-KEY-EPEL.txt && \  
rpm --import /tmp/RPM-GPG-KEY.dag.txt && \  
rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-latest-5.noarch.rpm
&& \  
rpm -Uvh http://apt.sw.be/redhat/el5/en/x86_64/rpmforge/RPMS/rpmforge-
release-0.5.3-1.el5.rf.x86_64.rpm  
  
# Add our customised repo priorities / config  
ADD rpmforge.repo /etc/yum.repos.d/  
# Install required packages  
RUN yum -y install \  
exim \  
git \  
icinga \  
icinga-doc \  
icinga-gui \  
lighttpd \  
nagios \  
nagios-common \  
nagios-nsca \  
nagios-nsca-client \  
nagios-plugins \  
nagios-plugins-dns \  
nagios-plugins-dummy \  
nagios-plugins-http \  
nagios-plugins-nrpe \  
nagios-plugins-ping \  
nagios-plugins-smtp \  
nagios-plugins-ssh \  
nagios-plugins-tcp && \  
yum update -y  
  
# Allow unified config independent of architecture  
RUN ln -s /usr/lib64/icinga /usr/lib/icinga && \  
# Allow icinga commands from web  
usermod -a -G icingacmd lighttpd  
  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network && \  
# Do not launch *getty on tty devices - they are not accessible  
sed -i -e '/getty/d' /etc/inittab && \  
# Disable Udev  
sed -i -e 's@^/sbin/start_udev@@' /etc/rc.sysinit && \  
# disable unnecessary services  
for SERVICE in iscsi iscsid lvm2-monitor mcstrans netconsole netfs network
rawdevices xinetd; do chkconfig $SERVICE off; done && \  
# enable necessary services  
for SERVICE in icinga lighttpd exim nsca; do chkconfig $SERVICE on; done && \  
# cache spool dir  
cp -a /var/spool/icinga /var/spool/icinga.cache  
  
# Copy in config  
ADD etc/lighttpd /etc/lighttpd/  
  
ADD entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  
  
EXPOSE 80  

