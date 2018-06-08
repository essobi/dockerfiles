FROM resin/amd64-debian:stretch  
  
MAINTAINER Bruno Binet <bruno.binet@helioslite.com>  
  
# enable container init system.  
ENV INITSYSTEM on  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
ENV SALT_VERSION 2017.7  
#ENV REFRESHED_AT 2018-03-01  
RUN echo "deb http://repo.saltstack.com/apt/debian/9/amd64/${SALT_VERSION}
stretch main" > /etc/apt/sources.list.d/salt.list  
ADD https://repo.saltstack.com/apt/debian/9/amd64/${SALT_VERSION}/SALTSTACK-
GPG-KEY.pub /tmp/SALTSTACK-GPG-KEY.pub  
RUN echo "9e0d77c16ba1fe57dfd7f1c5c2130438 /tmp/SALTSTACK-GPG-KEY.pub" |
md5sum --check  
RUN apt-key add /tmp/SALTSTACK-GPG-KEY.pub  
  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
dbus vim ssh less net-tools procps lsb-release ifupdown \  
make git wget python2.7 python-apt apt-transport-https \  
dnsmasq wireless-tools gnupg salt-minion \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN cp /lib/systemd/system/dbus.service /etc/systemd/system/; \  
sed -i 's/OOMScoreAdjust=.*//' /etc/systemd/system/dbus.service  
  
COPY override.conf /etc/systemd/system/salt-minion.service.d/override.conf  
COPY pre-salt-minion.sh /usr/local/bin/pre-salt-minion.sh  
  
VOLUME /sys/fs/cgroup  
  
ENV BEFORE_EXEC_SCRIPT /etc/salt/before-exec.sh  
  
CMD ["/bin/date"]  

