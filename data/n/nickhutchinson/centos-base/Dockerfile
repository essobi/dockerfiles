FROM centos:centos7  
MAINTAINER Nick Hutchinson <nick.hutchinson@thefoundry.co.uk>  
  
COPY scripts/install_runit.sh /tmp/install_runit.sh  
RUN yum -y install gcc glibc-static make && \  
/tmp/install_runit.sh && \  
rm /tmp/install_runit.sh && \  
yum -y remove gcc glibc-static make && \  
yum clean all  
  
RUN useradd -r -s /sbin/nologin -c "svlogd" -d /var/log/svlogd svlogd  
  
COPY sbin/ /sbin  
COPY etc/ /etc  
RUN ln -s /etc/service.d /service  
COPY var/log/svlogd /var/log/svlogd  
RUN chown -R svlogd:svlogd /var/log/svlogd  
  
VOLUME /var/log/svlogd  
  
CMD ["/sbin/my_init"]  

