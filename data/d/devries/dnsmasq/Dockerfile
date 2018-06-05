FROM ubuntu:14.04  
MAINTAINER Christopher De Vries <devries@idolstarastronomer.com>  
  
RUN apt-get update && apt-get install -y dnsmasq dnsutils inotify-tools &&
apt-get clean  
  
ADD reload.sh /etc/service/inotify/run  
  
RUN echo "addn-hosts=/etc/althosts" >> /etc/dnsmasq.conf && \  
echo "address=/.dev/127.0.0.1" >> /etc/dnsmasq.conf && \  
echo "user=root" >> /etc/dnsmasq.conf && \  
chmod +x /etc/service/inotify/run  
  
VOLUME /etc/althosts  
  
EXPOSE 53  
CMD ["/etc/service/inotify/run"]  

