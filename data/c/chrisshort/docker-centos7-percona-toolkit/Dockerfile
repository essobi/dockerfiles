FROM centos:7  
MAINTAINER Chris Short <chris@chrisshort.net>  
  
RUN yum -y update \  
&& yum clean all  
  
RUN yum -y install http://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm \  
&& yum -y install percona-toolkit \  
&& yum clean all  
  
RUN rm -rf /usr/share/doc/* \  
&& rm -rf /usr/share/info/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  
  
ENTRYPOINT [ "/bin/sh", "-c" ]

