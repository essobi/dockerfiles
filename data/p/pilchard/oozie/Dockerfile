#  
# Author: pilchard  
  
FROM pilchard/hive  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="Oozie"  
  
WORKDIR /  
  
RUN \  
yum install -y oozie oozie-client unzip && \  
curl -o ext-2.2.zip
https://archive.cloudera.com/gplextras/misc/ext-2.2.zip?_ga=1.74549458.1365709780.1481117914
&& \  
unzip -d /var/lib/oozie/ ext-2.2.zip && \  
rm -rf ext-2.2.zip && \  
cp /usr/lib/hive/lib/mysql-connector-java.jar /var/lib/oozie/mysql-connector-
java.jar && \  
yum remove -y mysql-connector-java && yum autoremove -y && \  
yum clean all  
  
CMD "bash"  

