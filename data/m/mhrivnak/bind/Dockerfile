FROM centos:7  
  
RUN yum update -y && yum install -y bind && yum clean all  
  
EXPOSE 5053/tcp  
EXPOSE 5053/udp  
  
# see "Support Arbitrary User IDs"  
# https://docs.openshift.org/latest/creating_images/guidelines.html  
RUN chgrp -R 0 /etc/named.* && chgrp -R 0 /var/named && chmod -R g=u
/var/named  
  
RUN rm /etc/named.conf && ln -s /var/run/secrets/bind/config/named.conf
/etc/named.conf  
  
# user named  
USER 25  
  
CMD /usr/sbin/named -c /etc/named.conf -g  

