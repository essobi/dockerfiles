FROM ubuntu:16.04  
MAINTAINER Petr Moravek v0.1  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV container docker  
ENV LC_ALL C  
ENV init /lib/systemd/systemd  
ENV TERM xterm  
  
VOLUME [ "/sys/fs/cgroup", "/tmp", "/run", "/run/lock" ]  
  
# docker run -it --privileged=true -v /sys/fs/cgroup:/sys/fs/cgroup:ro
444c127c995b /lib/systemd/systemd systemd.unit=emergency.service  
ENTRYPOINT ["/lib/systemd/systemd"]  
  
ADD 00-colors.sh /root/  
ADD 01-base.sh /root/  
RUN bash -C /root/01-base.sh 1>&2  
  
ADD 02-add.sh /root/  
ADD packages2install.txt /root/  
RUN bash -C /root/02-add.sh 1>&2  
  
ADD 03-fixSystemd.sh /root/  
RUN bash -C /root/03-fixSystemd.sh 1>&2  
  
ADD 04-sipp.sh /root/  
# RUN bash -C /root/04-sipp.sh 1>&2  
ADD 05-pjsip.sh /root/  
# RUN bash -C /root/05-pjsip.sh 1>&2  
ADD netRouter /root/netRouter/  
  
# Just for later use  
RUN chmod +x /root/*.sh  
  
# RUN systemctl enable apache2.service  
# RUN systemctl enable beanstalkd.service  
RUN systemctl set-default multi-user.target  

