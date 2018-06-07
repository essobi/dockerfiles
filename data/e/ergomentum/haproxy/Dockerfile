FROM ergomentum/centos:7.2.160911182133  
MAINTAINER \  
Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
  
COPY \  
haproxy-1.5.14_patched-3.el7.centos.x86_64.rpm /  
  
RUN \  
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1213602  
touch /var/lib/rpm/* && \  
yum localinstall /haproxy-1.5.14_patched-3.el7.centos.x86_64.rpm && \  
yum install iptables iproute && \  
yum clean all && \  
rm /haproxy-1.5.14_patched-3.el7.centos.x86_64.rpm && \  
chmod u-w /var/lib/haproxy && \  
rm -f /etc/haproxy/haproxy.cfg  
  
VOLUME \  
["/etc/haproxy/haproxy.cfg"]  
  
COPY \  
entrypoint.sh /  
  
ENTRYPOINT \  
["/entrypoint.sh"]  
  
EXPOSE \  
80 443  
ENTRYPOINT \  
["haproxy", "-f", "/etc/haproxy/haproxy.cfg"]  

