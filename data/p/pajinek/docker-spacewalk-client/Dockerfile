FROM fedora:24  
MAINTAINER "Pavel Studenik" <pstudeni@redhat.com>  
  
# download and install spacewalk nightly client repository  
RUN URL_SW=http://yum.spacewalkproject.org/2.6-client/Fedora/24/x86_64/ && \  
rpm -Uvh $URL_SW/$( curl --silent $URL_SW | grep spacewalk-client-repo-[0-9] |
grep -Po '(?<=href=")[^"]*' )  
  
RUN dnf install rhn-client-tools rhn-check rhn-setup rhnsd hwdata python3-dbus
m2crypto wget osad -y  
  
ADD bin/register.sh /root/register.sh  
ADD bin/osad.sh /root/osad.sh  
  
RUN chmod a+x /root/{register.sh,osad.sh}  
  
CMD /root/osad.sh  
  

