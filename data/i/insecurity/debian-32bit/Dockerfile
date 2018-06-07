FROM 32bit/debian:jessie  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
  
# Set apt-get to automatically retry if a package download fails  
RUN echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/99AcquireRetries  
  
# The ADD lines below ensurs that the docker build cache is invalidated if the
contents of the  
# mirror and/or security archive changes, necessary for apt-get to be actually
executed.  
ADD http://httpredir.debian.org/debian/project/trace/ftp-master.debian.org
/etc/trace_ftp-master.debian.org  
ADD http://security.debian.org/project/trace/security-master.debian.org
/etc/trace_security-master.debian.org  
  
# Upgrade image  
RUN dpkg-divert --local --rename /usr/bin/ischroot && ln -sf /bin/true
/usr/bin/ischroot \  
&& apt-get update \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade --no-install-
recommends -y \  
&& apt-get clean \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

