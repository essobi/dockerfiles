#  
# Author: Rohith  
# Date: 2015-06-15 20:40:29 +0100 (Mon, 15 Jun 2015)  
#  
# vim:ts=2:sw=2:et  
#  
FROM gambol99/store-admin:0.0.1  
MAINTAINER Rohith <gambol99@gmail.com>  
  
ADD config/rbd /bin/rbd  
ADD config/rbd-image /bin/rbd-image  
ADD config/ceph /bin/ceph  
ADD config/rados /bin/rados  
ADD config/startup /bin/startup  
  
RUN chmod +x /bin/startup  
  
CMD [ "/bin/startup" ]  

