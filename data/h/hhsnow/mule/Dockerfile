FROM centos:6  
MAINTAINER Henry Snow "henry.snow@nielsen.com"  
RUN yum update -y >> /dev/null  
  
#install java7  
RUN yum install -y
http://repo.exelator.net/files/global/jdk-7u80-linux-x64.rpm  
  
#install mule-standalone  
RUN yum install -y http://repo.exelator.net/files/global/mule-
standalone-3.5.0-1.x86_64.rpm  
  
#install supervisord  
RUN yum install -y wget  
RUN wget
https://svn.apache.org/repos/asf/oodt/tools/oodtsite.publisher/trunk/distribute_setup.py  
RUN python distribute_setup.py  
RUN yum install -y python-setuptools  
RUN easy_install pip  
RUN pip install distribute --upgrade  
RUN pip install supervisor  
ADD supervisord.conf /etc/  
  
VOLUME ["/usr/share/mule-standalone/logs", "/usr/share/mule-standalone/conf",
"/usr/share/mule-standalone/apps", "/usr/share/mule-standalone/domains"]  
  
WORKDIR /usr/share/mule-standalone  
  
CMD /usr/bin/supervisord -c /etc/supervisord.conf  

