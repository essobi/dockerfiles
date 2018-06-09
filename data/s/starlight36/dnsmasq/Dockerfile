FROM centos:7  
RUN yum update -y && yum install dnsmasq -y  
  
RUN mkdir -p /etc/dnsmasq.d/ && \  
touch /etc/dnsmasq.d/resolv.dnsmasq.conf && \  
touch /etc/dnsmasq.d/dnsmasq.conf  
  
COPY dnsmasq.conf /etc/dnsmasq.conf  
  
EXPOSE 53  
EXPOSE 53/udp  
  
VOLUME /etc/dnsmasq.d/  
  
CMD ["dnsmasq", "-d"]  

