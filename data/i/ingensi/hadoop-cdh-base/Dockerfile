FROM ingensi/oracle-jdk:centos6-7u65  
MAINTAINER Ingensi labs <contact@ingensi.com>  
  
# ORACLE JDK INSTALLED FROM RPM  
# ADD COMPATIBILITY TO CDH (according to the doc)  
# TODO: update minor version to 67 (see readme)  
RUN ln -s /usr/java/jdk1.7.0_65 /usr/java/jdk.1.7.0_65  
  
# GET CDH5 RPM AND INSTALL  
RUN wget http://archive.cloudera.com/cdh5/one-click-
install/redhat/6/x86_64/cloudera-cdh-5-0.x86_64.rpm \  
&& yum --nogpgcheck localinstall -y cloudera-cdh-5-0.x86_64.rpm \  
&& rm cloudera-cdh-5-0.x86_64.rpm \  
&& rpm --import http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/RPM-GPG-
KEY-cloudera  

