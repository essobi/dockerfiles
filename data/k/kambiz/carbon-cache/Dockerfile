FROM centos  
  
# Setup repos  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
  
# Install packages  
RUN yum clean all && yum install -y python-carbon && yum clean all  
  
# carbon-cache  
COPY storage-schemas.conf /etc/carbon/storage-schemas.conf  
COPY carbon.conf /etc/carbon/carbon.conf  
RUN touch /etc/carbon/storage-aggregation.conf  
  
# holding externally mounted data from the host  
VOLUME /var/lib/carbon  
  
CMD ["/usr/bin/carbon-cache", "--config=/etc/carbon/carbon.conf", "--
pidfile=/var/run/carbon-cache.pid", "--logdir=/var/log/carbon/", "--debug",
"start"]  
  

