FROM ubuntu:16.04  
  
MAINTAINER Magnus <github@aadl.org>  
  
# Set apt sources list to a snapshot  
# COPY sources.list /etc/apt/  
  
RUN apt-get update && apt-get -y install \  
cups \  
cups-filters \  
cups-pdf \  
whois \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN add-apt-repository ppa:simon-cadman/niftyrepo && \  
apt-get update && \  
apt-get -y install cupscloudprint  
  
  
# Remove backends that don't make sense for container  
RUN rm /usr/lib/cups/backend/parallel \  
&& rm /usr/lib/cups/backend/serial \  
&& rm /usr/lib/cups/backend/usb  
  
COPY etc-cups /etc/cups  
  
VOLUME /etc/cups/ /var/log/cups /var/spool/cups /var/cache/cups  
  
COPY etc-pam.d-cups /etc/pam.d/cups  
  
COPY start_cups.sh /root/start_cups.sh  
RUN chmod +x /root/start_cups.sh \  
&& mkdir -p /etc/cups/ssl  
  
CMD ["/root/start_cups.sh"]  
  
EXPOSE 631  

