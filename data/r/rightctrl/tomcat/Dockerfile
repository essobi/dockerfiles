FROM rightctrl/tomcat:8  
MAINTAINER RightCtrl <support@RightCtrl.com>  
RUN yum -y install gcc gcc-c++ make flex bison gperf ruby \  
openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \  
libpng-devel libjpeg-devel  
#added fonts  
RUN yum -y install google-*fonts  
RUN yum -y -q reinstall glibc-common && locale -a  
RUN rpm -Uvh https://rpm.nodesource.com/pub_4.x/el/7/x86_64/nodesource-
release-el7-1.noarch.rpm  
RUN yum install -y nodejs bzip2 git  
RUN npm install -g grunt-cli  
RUN npm install -g grunt  
#RUN npm install -g phantomjs  
COPY node-webshot-master /node-webshot-master  
WORKDIR /node-webshot-master  
RUN npm install  
  
#EXPOSE 8080 8443  
#CMD ["/run.sh"]  

