FROM ubuntu:precise  
  
MAINTAINER omri@iluz.net  
  
VOLUME [ "/etc/dnsmasq.d" ]  
  
RUN apt-get install -y dnsmasq-base  
RUN apt-get install --no-install-recommends -y dnsutils  
  
RUN echo "user=root" > /etc/dnsmasq.conf  
RUN echo "listen-address=__LOCAL_IP__" >> /etc/dnsmasq.conf  
RUN echo "conf-dir=/etc/dnsmasq.d" >> /etc/dnsmasq.conf  
RUN echo "domain=cluster.com" >> /etc/dnsmasq.conf  
  
ADD files /root/dnsmasq_files  
ADD files/redirect /bin/redirect  
RUN chmod +x /bin/redirect  
  
EXPOSE 53  
CMD ["/root/dnsmasq_files/default_cmd"]  

