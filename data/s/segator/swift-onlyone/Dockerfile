FROM ubuntu:14.04  
MAINTAINER curtis <curtis@serverascode.com>  
  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository cloud-archive:liberty && apt-get update && \  
apt-get install -y supervisor swift python-swiftclient rsync \  
swift-proxy swift-object memcached python-keystoneclient \  
python-swiftclient swift-plugin-s3 python-netifaces \  
python-xattr python-memcache \  
swift-account swift-container swift-object pwgen  
  
RUN mkdir -p /var/log/supervisor && mkdir /default  
ADD files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#  
# Swift configuration  
# - Partially fom
http://docs.openstack.org/developer/swift/development_saio.html  
#  
# not sure how valuable dispersion will be...  
ADD files/dispersion.conf /default/dispersion.conf  
ADD files/rsyncd.conf /etc/rsyncd.conf  
ADD files/swift.conf /etc/swift/swift.conf  
ADD files/proxy-server.conf /etc/swift/proxy-server.conf  
ADD files/account-server.conf /etc/swift/account-server.conf  
ADD files/object-server.conf /etc/swift/object-server.conf  
ADD files/container-server.conf /etc/swift/container-server.conf  
ADD files/proxy-server.conf /default/proxy-server.conf  
ADD files/startmain.sh /usr/local/bin/startmain.sh  
RUN chmod 755 /usr/local/bin/startmain.sh  
  
EXPOSE 8080  
ENV SWIFT_ADMIN_ACOUNT=admin  
ENV SWIFT_ADMIN_USER=admin  
ENV SWIFT_ADMIN_KEY=admin  
  
CMD /usr/local/bin/startmain.sh  

