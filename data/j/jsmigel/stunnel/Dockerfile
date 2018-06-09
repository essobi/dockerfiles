FROM centos:centos6  
  
RUN yum -y install stunnel  
RUN yum -y update  
  
RUN mkdir -p /etc/stunnel  
RUN chown nobody:nobody -R /etc/stunnel  
RUN mkdir /var/run/stunnel  
RUN chown nobody:nobody /var/run/stunnel  
  
USER nobody  
ENTRYPOINT [ "/usr/bin/stunnel" ]  

