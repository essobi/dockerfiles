FROM centos:7  
MAINTAINER Marc Richter <mail@marc-richter.info>  
  
# Update system  
RUN yum -y update  
  
# Install and enable chronyd  
RUN yum -y install chrony \  
&& systemctl enable chronyd  
  
# Add Puppetlabs repo  
RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm  
# Add EPEL repo  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
  
# Install monit  
RUN yum -y install monit \  
&& mkdir -p /var/monit/events \  
&& mkdir -p /etc/monit.d  
ADD files/monit/monitrc /etc/monitrc  
ADD files/monit/monit_main.template /etc/monit.d/00_monit_main.conf  
ADD files/monit/monit_puppetmaster.conf
/etc/monit.d/01_monit_puppetmaster.conf  
RUN if [ ! -e /var/monit/events ]; then mkdir -p /var/monit/events; fi  
RUN if [ ! -e /etc/monit.d ]; then mkdir -p /etc/monit.d; fi  
RUN chmod 600 /etc/monitrc /etc/monit.d/00_monit_main.conf
/etc/monit.d/01_monit_puppetmaster.conf \  
&& chmod 700 /etc/monit.d /var/monit/events  
  
# Install Puppet master  
RUN yum -y install puppet-server  
  
ADD files/init.sh /init  
RUN chmod +x /init  
  
VOLUME /etc/puppet  
VOLUME /etc/httpd  
VOLUME /etc/monit.d  
  
EXPOSE 8140  
CMD /init  

