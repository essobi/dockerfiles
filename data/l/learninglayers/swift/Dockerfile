FROM learninglayers/base  
MAINTAINER Gordon Lawrenz <lawrenz@dbis.rwth-aachen.de>  
  
# Update & Intall Swift+Necessary Tools  
RUN apt-get install -y swift python-swiftclient rsync \  
swift-proxy swift-object memcached python-keystoneclient \  
python-swiftclient swift-plugin-s3 python-netifaces \  
python-xattr python-memcache swift-object-expirer\  
swift-account swift-container swift-object pwgen  
  
#  
# You can see an example swift configuration here:  
# - Partially fom
http://docs.openstack.org/developer/swift/development_saio.html  
#  
# not sure how valuable dispersion will be...  
ADD src/main/files/swift /etc/swift  
ADD src/main/files/startmain.sh /opt/startmain.sh  
RUN chmod 755 /opt/startmain.sh  
  
EXPOSE 8080  
CMD /opt/startmain.sh  
  

