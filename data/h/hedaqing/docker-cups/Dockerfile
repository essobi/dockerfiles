FROM ubuntu:14.04  
  
MAINTAINER Li Ling <liling@bit.edu.cn>  
  
# Setup timezone  
RUN echo Asia/Shanghai > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
# Setup locale  
RUN locale-gen zh_CN.UTF-8 && locale-gen zh_CN && locale-gen zh_CN.GBK &&
locale-gen zh_CN.GB18030  
  
# RUN sed -i -e 's/archive.ubuntu.com/mirror.bit.edu.cn/'
/etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y  
  
# Install cups  
RUN apt-get update && apt-get install cups cups-pdf whois -y && apt-get clean
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Disbale some cups backend that are unusable within a container  
RUN mv /usr/lib/cups/backend/parallel /usr/lib/cups/backend-available/ &&\  
mv /usr/lib/cups/backend/serial /usr/lib/cups/backend-available/ &&\  
mv /usr/lib/cups/backend/usb /usr/lib/cups/backend-available/  
  
RUN mkdir -p /etc/cups  
#VOLUME /var/log/cups  
#VOLUME /var/spool/cups  
#VOLUME /var/cache/cups  
  
ADD etc-pam.d-cups /etc/pam.d/cups  
  
EXPOSE 631  
  
ADD start_cups.sh /root/start_cups.sh  
RUN chmod +x /root/start_cups.sh  
CMD ["/root/start_cups.sh"]  

