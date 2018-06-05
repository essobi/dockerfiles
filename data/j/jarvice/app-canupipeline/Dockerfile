FROM jarvice/base-centos-torque:6  
MAINTAINER Nimbix, Inc.  
  
RUN yum install -y wget java-1.8.0-openjdk-headless.x86_64 && yum clean all  
  
VOLUME /tmp  
WORKDIR /tmp  
  
RUN wget "https://github.com/marbl/canu/releases/download/v1.4/canu-1.4.Linux-
amd64.tar.xz" && tar xvf canu-1.4.Linux-amd64.tar.xz && mv /tmp/canu-1.4
/usr/local/canu-1.4  
  
ADD ./scripts /usr/local/scripts/canu  
ADD ./NAE/AppDef.json /etc/NAE/AppDef.json  
ADD ./NAE/AppDef.png /etc/NAE/AppDef.png  
ADD ./NAE/help.html /etc/NAE/help.html  
COPY ./NAE/screenshot.png /etc/NAE/screenshot.png  
  
CMD ["/usr/local/scripts/canu/canu-pipeline.sh"]  

