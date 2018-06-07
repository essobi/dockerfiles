FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
keystone \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN rm -vrf /etc/keystone/ssl/  
ONBUILD RUN keystone-manage pki_setup --keystone-user keystone --keystone-
group keystone  
  
EXPOSE 5000  
EXPOSE 35357  
CMD [ "keystone-all", "--verbose" ]  

