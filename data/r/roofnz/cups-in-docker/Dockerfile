FROM debian:stretch  
  
MAINTAINER Graeme Gellatly "graemeg@roof.co.nz"  
# Install cups  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y cups cups-bsd cups-pdf locales sudo
whois printer-driver-all hpijs-ppds hp-ppd hplip  
  
# Setup UTF-8 locale  
RUN sed -i "s/^#\ \\+\\(en_US.UTF-8\\)/\1/" /etc/locale.gen && locale-gen
en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && mkdir
/var/lib/apt/lists/partial  
  
# Disbale some cups backend that are unusable within a container  
RUN mv /usr/lib/cups/backend/parallel /usr/lib/cups/backend-available/ &&\  
mv /usr/lib/cups/backend/serial /usr/lib/cups/backend-available/ &&\  
rm /usr/lib/cups/backend/usb  
  
ADD etc-cups /etc/cups  
RUN mkdir -p /etc/cups/ssl  
VOLUME /etc/cups/  
VOLUME /var/log/cups  
VOLUME /var/spool/cups  
VOLUME /var/cache/cups  
  
ADD etc-pam.d-cups /etc/pam.d/cups  
  
EXPOSE 631  
ADD start_cups.sh /root/start_cups.sh  
RUN chmod +x /root/start_cups.sh  
CMD ["/root/start_cups.sh"]  

