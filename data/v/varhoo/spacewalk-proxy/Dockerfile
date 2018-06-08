FROM fedora:24  
MAINTAINER "Pavel Studenik" <pstudeni@redhat.com>  
  
RUN URL_SW=http://yum.spacewalkproject.org/nightly/Fedora/24/x86_64/ && \  
rpm -Uvh $URL_SW/$( curl --silent $URL_SW | grep spacewalk-repo-[0-9] | grep
-Po '(?<=href=")[^"]*' )  
RUN sed s/enabled=0/enabled=1/g /etc/yum.repos.d/spacewalk-nightly.repo -i &&
\  
sed s/enabled=1/enabled=0/g /etc/yum.repos.d/spacewalk.repo -i  
  
RUN dnf update -y && \  
dnf install spacewalk-proxy-selinux spacewalk-proxy-installer spacewalk-proxy-
management \  
rhn-client-tools rhn-check rhn-setup rhnsd hwdata python3-dbus m2crypto wget
which -y && \  
dnf clean all  
  
RUN wget
https://raw.githubusercontent.com/spacewalkproject/spacewalk/master/proxy/installer/get_system_id.xslt
-O /usr/share/rhn/get_system_id.xslt  
  
ADD proxyanswers.txt /root/proxyanswers.txt  
ADD bin/rhnclient.py /root/rhnclient.py  
ADD bin/configure.sh /root/configure.sh  
ADD bin/docker-entrypoint.sh /root/docker-entrypoint.sh  
  
# system needs to be to registered to Spacewalk  
RUN chmod a+x /root/docker-entrypoint.sh  
RUN chown -R squid. /var/spool/squid  
RUN chown -R apache. /var/spool/rhn-proxy/  
  
EXPOSE 80 443 5222 5269 5280  
CMD /root/docker-entrypoint.sh  

