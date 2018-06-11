# ci-base  
#  
# Basic Docker image for CI services  
#  
FROM centos:6  
MAINTAINER Kirill Evstigneev <kevstigneev@griddynamics.com>  
  
# Enable EPEL repository (https://fedoraproject.org/wiki/EPEL)  
RUN yum -y install tar wget java-1.8.0-openjdk \  
&& yum -y install epel-release \  
&& yum -y clean all && rm -rf /var/cache/*  
  
ENV PATH /opt/bin:${PATH}  
  
# Install generic ENTRYPOINT script  
# Prepare directory for the script flag files.  
# /var/opt should be mapped to a Docker volume.  
#  
COPY files/bin/do.sh /opt/bin/do  
RUN chmod 755 /opt/bin/do \  
&& mkdir /var/run/entrypoint && chmod a=rwXt /var/run/entrypoint \  
&& mkdir /var/opt/entrypoint && chmod a=rwXt /var/opt/entrypoint  
ENTRYPOINT ["do"]  

