#  
# ementux/haproxy-serf  
#  
# HAProxy with Serf agent  
#  
# See https://github.com/ementux/docker  
#  
FROM ementux/base  
MAINTAINER Michal Grna <michal.grna@ementux.org>  
  
# install HAProxy and unzip  
RUN yum -y update && yum -y install haproxy unzip && yum clean all  
  
# add configuration file and wrapper for HAProxy  
COPY haproxy.cfg /etc/haproxy/haproxy.cfg  
RUN mkdir -p /etc/service/haproxy/  
COPY haproxy.run /etc/service/haproxy/run  
RUN chmod 755 /etc/service/haproxy/run  
  
# install Serf  
ADD https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip /tmp/serf.zip  
RUN unzip /tmp/serf.zip -d /usr/local/bin/  
RUN rm /tmp/serf.zip  
  
# add configuration files and handlers for Serf  
COPY serf-config /etc/serf  
RUN mkdir -p /etc/service/serf/  
COPY serf.run /etc/service/serf/run  
RUN chmod 755 /etc/service/serf/run  
  
# add certifications volume  
VOLUME "/srv/certs"  
  
# expose http(s) & HAProxy stats & Serf ports  
EXPOSE 80 443 7946 7373 9876  
# start HAProxy and Serf  
ENTRYPOINT [ "/usr/sbin/runit_bootstrap" ]  
  

