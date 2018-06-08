FROM ubuntu:xenial  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
  
# Install dependencies.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
systemd systemd-cron \  
&& rm -Rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
COPY files/initctl_faker .  
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker
/sbin/initctl  
  
VOLUME [ "/sys/fs/cgroup" ]

