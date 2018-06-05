FROM centos:7  
MAINTAINER "romracer" <romracer@gmail.com>  
ENV BACULA_VERSION "7.4.3"  
LABEL com.baculasystems.bacula.version="${BACULA_VERSION}" \  
com.redcoolbeans.image.version="1.0.1"  
  
ENV BACULA_COMPONENTS "bacula-libs bacula-common bacula-libs-sql bacula-
storage"  
# Install customer's repository information  
RUN mkdir -p /tmp/bacula  
ADD bacula-common/configs/ /tmp/bacula  
  
RUN yum -q -y update && \  
yum -q -y install sudo  
RUN for b in ${BACULA_COMPONENTS}; do yum -y --nogpgcheck localinstall
/tmp/bacula/$b-${BACULA_VERSION}*.rpm; done  
  
RUN sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
  
# Cleanup caches and repository information  
RUN yum clean all; rm -rf /tmp/bacula  
  
ADD bacula-sd/scripts/run.sh /  
RUN chmod +x /run.sh  
  
# Volume(s):  
# /backups: Default disk-based backup point. Can be a host-volume or a
separate  
# container if needed.  
VOLUME ["/backups"]  
  
ENTRYPOINT ["/run.sh"]  
  
EXPOSE 9103  

