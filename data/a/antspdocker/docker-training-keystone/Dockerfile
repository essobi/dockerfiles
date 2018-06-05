FROM ubuntu:14.04  
  
RUN set -x \  
&& echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-
updates/kilo main" > /etc/apt/sources.list.d/kilo.list \  
&& apt-get -y update \  
&& apt-get -y install ubuntu-cloud-keyring \  
&& apt-get -y update \  
&& apt-get install -y libffi-dev python-dev libssl-dev mysql-client python-
mysqldb keystone python-openstackclient\  
&& apt-get -y clean  
  
EXPOSE 5000 35357  
  
COPY keystone.sql /root/keystone.sql  
COPY keystone.conf /etc/keystone/keystone.conf  
  
COPY bootstrap-keystone.sh /etc/bootstrap.sh  
  
RUN chown root.root /etc/bootstrap.sh && chmod a+x /etc/bootstrap.sh  
ENTRYPOINT ["/etc/bootstrap.sh"]  
  
  

