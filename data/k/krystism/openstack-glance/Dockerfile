FROM ubuntu:14.04  
MAINTAINER krystism "krystism@gmail.com"  
# install packages  
RUN set -x \  
&& echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-
updates/juno main" > /etc/apt/sources.list.d/juno.list \  
&& apt-get -y update \  
&& apt-get -y install ubuntu-cloud-keyring \  
&& apt-get -y update \  
&& apt-get -y install \  
mysql-client \  
glance \  
python-glanceclient \  
python-keystoneclient \  
python-mysqldb \  
&& apt-get -y clean \  
&& rm -f /var/lib/glance/glance.sqlite  
  
EXPOSE 9191 9292  
  
#copy sql script  
COPY glance.sql /root/glance.sql  
#copy glance config file  
COPY glance-api.conf /etc/glance/glance-api.conf  
COPY glance-registry.conf /etc/glance/glance-registry.conf  
# add bootstrap script and make it executable  
COPY bootstrap.sh /etc/bootstrap.sh  
  
RUN chown root.root /etc/bootstrap.sh && chmod a+x /etc/bootstrap.sh  
  
ENTRYPOINT ["/etc/bootstrap.sh"]  

