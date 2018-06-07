FROM ubuntu:xenial  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
  
# Set apt-get to automatically retry if a package download fails and  
# Set apt-get \--no-install-recommend/--no-install-suggest values  
RUN echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/99AcquireRetries \  
&& echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
  
# Upgrade image \  
&& dpkg-divert --local --rename /usr/bin/ischroot && ln -sf /bin/true
/usr/bin/ischroot \  
&& apt-get update \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y wget ca-
certificates unzip vim-tiny \  
&& apt-get dist-upgrade --no-install-recommends -y \  
&& apt-get clean \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

