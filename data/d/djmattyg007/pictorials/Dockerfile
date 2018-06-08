FROM djmattyg007/arch-phpfpm:2017.01.18-1  
MAINTAINER djmattyg007  
  
ENV PICTORIALSIMAGE_VERSION=2017.01.18-2  
# Add install bash script  
COPY setup/root/*.sh /root/  
COPY setup/init-dhcpcd.sh /etc/service/dhcpcd/run  
  
ENV PICTORIALS_VERSION=0.4.0-dev  
  
# Run bash script to install additional PHP packages, dhcpcd, and download
pictorials  
RUN /root/install.sh && \  
rm /root/*.sh  
  
ENTRYPOINT ["/usr/bin/init"]  

