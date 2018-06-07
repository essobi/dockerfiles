FROM ubuntu:14.04  
RUN set -x \  
&& echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-
updates/kilo main" > /etc/apt/sources.list.d/kilo.list \  
&& apt-get -y update \  
&& apt-get -y install ubuntu-cloud-keyring \  
&& apt-get -y update \  
&& apt-get install -y apache2 libffi-dev python-dev libssl-dev python-
openstackclient\  
&& apt-get -y clean  
  
COPY openrc_admin /root/openrc_admin1  
COPY openrc_admin1 /root/openrc_admin  
COPY bootstrap.sh /etc/bootstrap.sh  
  
EXPOSE 80  
RUN chown root.root /etc/bootstrap.sh && chmod a+x /etc/bootstrap.sh  
ENTRYPOINT ["/etc/bootstrap.sh"]  
  

