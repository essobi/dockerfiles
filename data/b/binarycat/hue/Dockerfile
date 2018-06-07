FROM binarycat/cx_oracle:5  
RUN yum install -y postgresql \  
postgresql-devel \  
mysql \  
mysql-devel; yum -y clean all  
  
RUN python -m pip install psycopg2 \  
mysql \  
sqlalchemy \  
Werkzeug  
  
# java  
RUN curl -H "Cookie: oraclelicense=accept-securebackup-cookie" \  
-o /tmp/jdk-8u151-linux-x64.rpm \  
http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.rpm  
  
RUN curl -H "Cookie: oraclelicense=accept-securebackup-cookie" \  
-o /tmp/jre-8u151-linux-x64.rpm \  
http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jre-8u151-linux-x64.rpm  
  
RUN yum install -y /tmp/*.rpm; yum -y clean all  
  
# hadoop client  
RUN curl -o /etc/yum.repos.d/cloudera-cdh5.repo
https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/cloudera-cdh5.repo && \  
curl -o /etc/yum.repos.d/cloudera-manager.repo
https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/cloudera-manager.repo && \  
rpm --import https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/RPM-GPG-
KEY-cloudera  
  
# hue  
RUN yum install -y hadoop-client \  
hue; yum -y clean all  
  
ENV JAVA_HOME=/usr/java/jdk1.8.0_151/  
ENV HUE_HOME=/usr/lib/hue/build/env/  
ENV HUE_CONF_DIR=/etc/hue/conf  
ENV HADOOP_CONF_DIR=/etc/hadoop/conf  
  
#  
EXPOSE 8080  
CMD ["$HUE_HOME/bin/hue", "runserver_plus", "0.0.0.0:8080"]  

