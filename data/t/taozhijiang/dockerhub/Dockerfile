FROM fedora:22  
MAINTAINER taozhijiang <taozhijiang@gmail.com>  
  
RUN dnf update -y && dnf install pptpd iptables -y  
RUN dnf clean all  
  
RUN echo "\nlocalip 192.168.5.254 \nremoteip 192.168.5.200-230\n" >>
/etc/pptpd.conf  
RUN echo "\nms-dns 8.8.8.8 \nms-dns 8.8.4.4\n" >> /etc/ppp/options.pptpd  
  
EXPOSE 1723  
COPY ./pptpd_start.sh /root/pptpd_start.sh  
RUN chmod u+x /root/pptpd_start.sh  
  
CMD ["/root/pptpd_start.sh"]  

