##  
##Dockerfile  
##  
FROM centos:6  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
  
##  
## copy configuration of my.cnf  
##  
COPY ./docker/install/* /root/install/  
RUN chmod -R 755 /root/install/  
  
##  
## facilities  
##  
RUN yum install -y memcached ntp postfix && \  
chkconfig memcached on && \  
chkconfig ntpd on && \  
chkconfig postfix on && \  
sed -i 's@^inet_protocols = all@inet_protocol = ipv4@g' /etc/postfix/main.cf
&& \  
service memcached start && \  
service postfix start && \  
service ntpd start  
  
##  
## Kaltura  
##  
RUN rpm -ihv http://installrepo.kaltura.org/releases/kaltura-
release.noarch.rpm && \  
sed -i 's@installrepo.kaltura.org@installrepo.origin.kaltura.org@g'
/etc/yum.repos.d/kaltura.repo && \  
sed -i 's@^tsflags=nodocs@#tsflags=nodocs@g' /etc/yum.conf && \  
yum install -y kaltura-postinst kaltura-base && \  
yum install -y vim dos2unix  
  
EXPOSE 80 443 1935 88 8443  
# start services  
CMD ["/sbin/init"]

