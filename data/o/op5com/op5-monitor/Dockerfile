FROM centos:centos6.9  
MAINTAINER Misiu Pajor <misiu.pajor@op5.com>  
  
# Install OP5 Monitor  
ARG OP5_MONITOR_SOFTWARE_URL=https://s3-eu-
west-1.amazonaws.com/op5-filebase/Downloads/op5_monitor_archive/op5-monitor-7.4.0-20180320.tar.gz  
RUN yum -y install wget openssh-server python-requests \  
&& wget $OP5_MONITOR_SOFTWARE_URL -O /tmp/op5-software.tar.gz \  
&& mkdir -p /tmp/op5-monitor && tar -zxf /tmp/op5-software.tar.gz -C
/tmp/op5-monitor --strip-components=1 \  
&& cd /tmp/op5-monitor && ./install.sh --silent \  
&& rm -f /tmp/op5-software.tar.gz \  
&& cd /tmp && rm -rf /tmp/op5-monitor \  
&& yum clean all  
  
# Disable ipv6 binding for postfix  
RUN sed -i 's/inet_protocols = all/inet_protocols = ipv4/g'
/etc/postfix/main.cf  
  
# Replace the system() source because inside Docker we can't access
/proc/kmsg.  
# https://groups.google.com/forum/#!topic/docker-user/446yoB0Vx6w  
RUN sed -i -E 's/^(\s*)system\\(\\);/\1unix-stream("\/dev\/log");/'
/etc/syslog-ng/syslog-ng.conf \  
&& sed -i -E '/\proc\/kmsg/ s/^#*/#/' /etc/syslog-ng/syslog-ng.conf  
  
# Expose ports that are required by OP5  
EXPOSE 80 443 5666 15551 22 161/tcp 162/udp  
  
COPY /entrypoint.d /usr/libexec/entrypoint.d/  
COPY /entrypoint.d/licenses/* /etc/op5license/  
  
RUN chmod +x /usr/libexec/entrypoint.d/hooks/* \  
&& chmod +x /usr/libexec/entrypoint.d/entrypoint.sh \  
&& chmod +x /usr/libexec/entrypoint.d/hooks.py  
CMD ["/usr/libexec/entrypoint.d/entrypoint.sh"]  

