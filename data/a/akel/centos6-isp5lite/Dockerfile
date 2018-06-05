# VERSION 0.0.15  
FROM centos:6.6  
MAINTAINER Akel <akel@maintainer.com>  
  
RUN yum -y update  
RUN yum -y install wget  
RUN wget -O /usr/local/src/install.sh http://download.ispsystem.com/install.sh  
RUN chmod +x /usr/local/src/install.sh  
RUN /usr/local/src/install.sh --osfamily REDHAT --osversion 6 --release stable
--silent ISPmanager-Lite  
  
COPY postinstall.sh /usr/local/src/postinstall.sh  
COPY tuning.sh /usr/local/src/tuning.sh  
  
RUN chmod +x /usr/local/src/postinstall.sh  
RUN chmod +x /usr/local/src/tuning.sh  
  
RUN /usr/local/src/postinstall.sh  
RUN /usr/local/src/tuning.sh  
  
EXPOSE 21 22 25 53 80 110 143 443 465 1500 3306  

