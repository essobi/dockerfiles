FROM centos:7.4.1708  
MAINTAINER dy@shayulei.com  
  
ADD
https://raw.githubusercontent.com/shayulei/dockersfiles/master/ntp/start.sh
/start.sh  
  
RUN yum -y install ntp \  
&& rm -rf /etc/ntp.conf \  
&& yum clean all \  
&& chmod +x /start.sh  
  
ADD
https://raw.githubusercontent.com/shayulei/dockersfiles/master/ntp/ntp.conf
/etc/ntp.conf  
  
ENTRYPOINT ["/start.sh"]  

