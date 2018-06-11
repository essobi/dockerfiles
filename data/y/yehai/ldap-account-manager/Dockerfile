FROM phusion/baseimage:0.9.15  
MAINTAINER Carlos Alberto <aexo@aexo.com.br>  
  
ENV HOME /root  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Configure apt  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise universe' >>
/etc/apt/sources.list  
RUN apt-get -y update  
  
#install ldap account manager  
RUN C_ALL=C DEBIAN_FRONTEND=noninteractive apt-get -y install ldap-account-
manager  
  
# copy default config lam  
RUN cp -r /var/lib/ldap-account-manager/config /opt/lam  
  
EXPOSE 80  
RUN rm /etc/apache2/sites-enabled/*default*  
  
RUN mkdir /etc/service/apache2  
ADD apache2.sh /etc/service/apache2/run  
  
# To store the data outside the container, mount /var/lib/ldap as a data
volume  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

