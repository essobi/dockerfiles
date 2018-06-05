FROM centos:7  
MAINTAINER Kostaintyn Bokhan <konstboh@gmail.com>  
  
# Add image description and version  
ENV IMAGE_DESCRIPTION aurora  
ENV IMAGE_VERSION 0.1  
ENV AURORA_VERSION 0.16.0  
ENV MESOS_VERSION 1.0.1  
RUN yum update -y && \  
yum install -y wget python2.7  
RUN wget --no-cookies --no-check-certificate
http://repos.mesosphere.com/el/7/x86_64/RPMS/mesos-1.0.1-2.0.93.centos701406.x86_64.rpm
&& \  
yum localinstall -y /mesos-1.0.1-2.0.93.centos701406.x86_64.rpm && \  
rm -f /mesos-1.0.1-2.0.93.centos701406.x86_64.rpm  
RUN wget -c https://apache.bintray.com/aurora/centos-7/aurora-
executor-${AURORA_VERSION}-1.el7.centos.aurora.x86_64.rpm && \  
yum localinstall -y /aurora-
executor-${AURORA_VERSION}-1.el7.centos.aurora.x86_64.rpm && \  
rm -f /aurora-executor-${AURORA_VERSION}-1.el7.centos.aurora.x86_64.rpm && \  
yum clean all  
  
# Defaults for Aurora executor startup  
ENV AURORA_HOME /var/lib/aurora  
ENV MESOS_ROOT /var/lib/mesos  
ENV OBSERVER_PORT 1338  
COPY docker-entrypoint.sh /  
RUN chmod a+x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE $OBSERVER_PORT  
  
CMD ["thermos_observer"]  

