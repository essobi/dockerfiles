FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y sane-utils imagemagick  
COPY scan_image.sh /usr/local/bin/  
RUN apt-get clean  
  
VOLUME /work  
WORKDIR /work  
CMD echo ${SANE_SERVER} >>/etc/sane.d/net.conf && \  
/usr/local/bin/scan_image.sh  

