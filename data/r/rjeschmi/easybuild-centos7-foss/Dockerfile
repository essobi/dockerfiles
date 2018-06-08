FROM rjeschmi/easybuild-centos7:latest  
  
MAINTAINER Robert Schmidt <rjeschmi@gmail.com>  
  
USER root  
ADD build/eb.repo /etc/yum.repos.d/eb.repo  
RUN yum clean all && yum -y install foss-2016a  
RUN yum clean all && yum -y install FPM-1.3.3-Ruby-2.1.6  
ADD build/40-optarch-generic.cfg /easybuild/etc/easybuild.d/40-optarch-
generic.cfg  
ADD build/ebrpm.sh /usr/bin/ebrpm  
RUN chmod a+x /usr/bin/ebrpm  
  
WORKDIR /easybuild/packages  
  
ENTRYPOINT /bin/bash  
  
run chown easybuild /easybuild  
  
USER easybuild  
  

