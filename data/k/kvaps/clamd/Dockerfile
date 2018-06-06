FROM centos:centos6  
MAINTAINER kvaps <kvapss@gmail.com>  
ENV REFRESHED_AT 2016-09-29  
RUN yum -y install epel-release  
RUN yum -y install clamd  
RUN sed -i '/TCPAddr/s/ .*/ 0.0.0.0/' /etc/clamd.conf  
  
ENTRYPOINT ["/bin/start.sh"]  
VOLUME ["/data"]  
EXPOSE 3310  
ADD clamd-wrapper.sh /bin/clamd-wrapper.sh  
ADD start.sh /bin/start.sh  

