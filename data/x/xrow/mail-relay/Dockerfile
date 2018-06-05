# Beware! This is a fat container. Why do we do this? Legacy applications
aren't designed the microservice way. Use kubernetes for healthiness of the
service  
# docker build --rm --no-cache -t mail-relay:latest .  
# docker kill mail-relay && docker rm mail-relay  
# docker run --privileged --name mail-relay -v
/sys/fs/cgroup:/sys/fs/cgroup:ro -d mail-relay:latest  
# docker run --privileged --name mail-relay -v
/sys/fs/cgroup:/sys/fs/cgroup:ro -ti mail-relay:latest bash  
  
FROM centos/systemd:latest  
  
MAINTAINER "Björn Dieding" <bjoern@xrow.de>  
  
ENV container=docker  
ENV TERM=dumb  
ENV lang en_US  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
ADD rspamd-experimental.repo /etc/yum.repos.d/rspamd-experimental.repo  
RUN yum install -y epel-release  
RUN yum install -y fann redis rspamd  
  
  
RUN yum -y install postfix rsyslog telnet;\  
postconf -e inet_protocol=ipv4;\  
postconf -e relayhost=192.168.0.245;\  
postconf -e mynetworks="127.0.0.0/8 192.168.0.0/16 10.0.0.0/8 172.16.0.0/12";\  
postconf -e smtpd_milters="inet:localhost:11332";\  
postconf -e milter_default_action="accept"; \  
touch /etc/postfix/virtual; \  
touch /etc/postfix/access; \  
postmap hash:/etc/postfix/virtual; \  
postmap hash:/etc/postfix/access;\  
systemctl enable redis;\  
systemctl enable rspamd;\  
systemctl enable postfix;\  
echo 1  
EXPOSE 25

