FROM centos:6  
RUN yum update -y && \  
yum install -y java-1.8.0-openjdk && \  
rpm -ivh http://download.igniterealtime.org/openfire/openfire-3.9.3-1.i386.rpm
\  
http://ci.tuleap.net/yum/tuleap/rhel/6/dev/x86_64/openfire-tuleap-
plugins-3.6.4-1.noarch.rpm  
  
EXPOSE 7070 5222 5223 9090 9091  
ENV PASSWORD=welcome1  
  
COPY codendi_auth.jar /opt/openfire/lib/codendi_auth.jar  
COPY openfire.tpl.xml /opt/openfire/conf/openfire.xml  
COPY run.sh /run.sh  
  
CMD /run.sh  

