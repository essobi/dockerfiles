FROM ubuntu:14.04.2  
MAINTAINER "Sunny" <hotsun@hotmail.com.hk>  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install software requirements  
RUN apt-get update && \  
BUILD_PACKAGES="pptpd iptables" && \  
apt-get -y install $BUILD_PACKAGES  
  
# Add server and client IP  
RUN echo "localip 192.168.0.1" >> /etc/pptpd.conf  
RUN echo "remoteip 192.168.0.100-200" >> /etc/pptpd.conf  
  
# Configure DNS server  
RUN echo "ms-dns 8.8.8.8" >> /etc/ppp/pptpd-options  
RUN echo "ms-dns 8.8.4.4" >> /etc/ppp/pptpd-options  
  
# Disable logwtmp  
RUN sed -i 's/^logwtmp/#logwtmp/g' /etc/pptpd.conf  
  
# Setup IP Forwarding  
RUN sed -i 's/^net.ipv4.ip_forward = 0/net.ipv4.ip_forward = 1/g'
/etc/sysctl.conf && \  
sysctl -p && \  
echo "iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j SNAT --to-source
`ifconfig | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk 'NR==1
{ print $1}'`" > /etc/rc.local && \  
echo "iptables -A FORWARD -p tcp --syn -s 192.168.0.0/24 -j TCPMSS --set-mss
1356" >> /etc/rc.local && \  
echo "exit 0" >> /etc/rc.local  
  
# Enable iptables  
#RUN ufw enable  
EXPOSE 1723  
CMD ["/usr/sbin/pptpd", "-f"]  

