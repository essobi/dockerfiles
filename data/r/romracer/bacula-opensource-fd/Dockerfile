FROM centos:7  
MAINTAINER "romracer" <romracer@gmail.com>  
ENV BACULA_VERSION "7.4.3"  
LABEL com.baculasystems.bacula.version="${BACULA_VERSION}" \  
com.redcoolbeans.image.version="1.0.1"  
  
ENV BACULA_COMPONENTS "bacula-libs bacula-common bacula-client"  
# Install customer's repository information  
RUN mkdir -p /tmp/bacula  
ADD bacula-common/configs/ /tmp/bacula  
  
RUN yum -q -y update && \  
for b in ${BACULA_COMPONENTS}; do yum -y --nogpgcheck localinstall
/tmp/bacula/$b-${BACULA_VERSION}*.rpm; done  
  
# Cleanup caches and repository information  
RUN yum clean all; rm -rf /tmp/bacula  
  
# Add and save a copy of the config file so we can re-populate it anytime  
ADD bacula-fd/configs/bacula-fd.conf /etc/bacula/bacula-fd.conf  
RUN cp /etc/bacula/bacula-fd.conf{,.orig}  
  
ADD bacula-fd/scripts/run.sh /  
  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  
EXPOSE 9102  

