FROM centos:centos7  
MAINTAINER mike@whatsmycut.com  
# undocumented requirement for docker containers  
ENV container=docker  
# systemd init variables  
ENV init /lib/systemd/systemd  
ENV SYSTEMD_IGNORE_CHROOT=true  
# yum package update for latest systemd  
RUN yum -y distribution-synchronization  
RUN yum -y update  
  
## additional yum packages  
### named (dns server) service  
RUN yum install -y sh wget sudo bind bind-utils  
RUN yum -y install epel-release # for nginx  
RUN yum -y install initscripts # for old "service"  
# Remove problematic files for systemd to run in docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# extra systemd settings.  
RUN systemctl set-default multi-user.target  
  
# myserver test  
COPY someserver /etc/init.d/  
RUN find / -name *update*; \  
chkconfig --add someserver; \  
sysctl -p;  
  
  
## INSTALL JAVA 8u151-b12  
# Prepare environment  
ENV JAVA_HOME /opt/java  
  
# Install Oracle Java8  
ENV JAVA_VERSION 8u151  
ENV JAVA_BUILD 8u151-b12  
ENV JAVA_DL_HASH e758a0de34e24606bca991d704f6dcbf  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_BUILD}/${JAVA_DL_HASH}/jre-${JAVA_VERSION}-linux-x64.rpm
&& \  
yum localinstall -y jre-${JAVA_VERSION}-linux-x64.rpm \  
rm jre*.rpm \  
mv jre* ${JAVA_HOME}  
  
# Enable services  
RUN systemctl enable named.service  
RUN systemctl enable network.service  
RUN systemctl list-unit-files;  
#RUN systemctl --system  
# set required volumes for cgroup and docker (/run and /tmp may not be
necessary)  
# Entrypoint  
#ENTRYPOINT ["/usr/lib/systemd/systemd", "--system"]  
#ENTRYPOINT [ "/usr/sbin/init" ]  
# print out some info  
# RUN systemctl start named.service  
#RUN find / -name *network*  
#RUN ls -al /etc/init.d/  
RUN java -version  
#RUN [ "/etc/rc.d/init.d/network", "start"]  
RUN chkconfig --level 2345 network on; \  
chkconfig --list;  
#old stuff  
#/sbin/chkconfig network on  
VOLUME /sys/fs/cgroup  
# start systemd  
#CMD ["sysctl", "--system"]  
ENTRYPOINT [ "/usr/sbin/init" ]  
CMD ["/bin/bash"]  
  
  
  
  
# Copy run script  
#COPY run.sh /  
#ENTRYPOINT ["/bin/bash"]  

