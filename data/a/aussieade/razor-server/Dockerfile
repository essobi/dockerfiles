# docker-razor  
FROM centos:centos6.6  
MAINTAINER aussieade  
  
COPY install.pp /root/install.pp  
COPY start.sh /root/start.sh  
  
RUN yum -y update && \  
rpm -ivh https://yum.puppetlabs.com/el/6/products/x86_64/puppetlabs-
release-6-11.noarch.rpm && \  
yum install -y puppet tar razor-server ipmitool && \  
puppet module install puppetlabs/postgresql && \  
yum clean all && \  
chmod 750 /root/start.sh  
  
ENV HOSTNAME razor-server  
ENV TORQUEBOX_HOME /opt/razor-torquebox  
ENV JBOSS_HOME $TORQUEBOX_HOME/jboss  
ENV JRUBY_HOME $TORQUEBOX_HOME/jruby  
ENV PATH $JRUBY_HOME/bin:$PATH  
  
EXPOSE 8080  
CMD ["/root/start.sh"]  

