FROM ubuntu  
  
RUN apt-get -y update  
RUN apt-get -y install wget  
RUN wget -q -O nxlog.deb
https://nxlog.co/system/files/products/files/348/nxlog-
ce_2.9.1716_ubuntu_1604_amd64.deb  
RUN dpkg -i nxlog.deb || apt-get -y -f install  
RUN rm -rf nxlog.deb  
  
ENTRYPOINT ["/usr/bin/nxlog"]  
CMD ["-f"]  

