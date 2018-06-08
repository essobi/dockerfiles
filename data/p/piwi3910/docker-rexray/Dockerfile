FROM centos:7  
MAINTAINER Pascal Watteel <pascal.watteel@emc.com>  
  
RUN yum update -y && \  
yum install -y curl dmidecode vim && \  
yum clean all && rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
RUN /usr/bin/curl -sSL https://dl.bintray.com/emccode/rexray/install | sh -s
stable  
RUN /usr/bin/curl -sSL https://dl.bintray.com/emccode/dvdcli/install | sh -s
stable  
  
COPY start_rexray.sh /  
COPY rexray-scaleIO.conf /etc/rexray/  
RUN chmod +x /start_rexray.sh  
  
EXPOSE 7979  
CMD ["/start_rexray.sh"]  

