FROM ubuntu  
MAINTAINER Bertrand Retif <bertrand@sudokeys.com>  
  
ENV OSTACK_AUTH_URL https://auth.cloud.ovh.net/v2.0/  
ENV OSTACK_USERNAME username  
ENV OSTACK_PASSWORD password  
ENV OSTACK_TENANT tenant  
ENV OSTACK_REGION region  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -yq curl wget dmidecode vim && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#RUN /usr/bin/curl -sSL https://dl.bintray.com/emccode/rexray/install | sh -s
stable -- stable 0.3.3  
RUN /usr/bin/wget --quiet -O /tmp/rexray_0.3.3-1_amd64.deb
https://dl.bintray.com/emccode/rexray/stable/0.3.3/rexray_0.3.3-1_amd64.deb &&
\  
dpkg -i /tmp/rexray_0.3.3-1_amd64.deb && \  
rm /tmp/rexray_0.3.3-1_amd64.deb  
RUN /usr/bin/curl -sSL https://dl.bintray.com/emccode/dvdcli/install | sh -s
stable  
  
COPY start_rexray.sh /  
COPY rexray-openstack.conf /etc/rexray/  
RUN chmod +x /start_rexray.sh  
  
EXPOSE 7979  
CMD ["/start_rexray.sh"]  

