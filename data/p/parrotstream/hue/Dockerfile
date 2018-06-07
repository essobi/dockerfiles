FROM parrotstream/centos-openjdk  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
USER root  
  
ADD cloudera-cdh5.repo /etc/yum.repos.d/  
RUN rpm --import https://archive.cloudera.com/cdh5/redhat/5/x86_64/cdh/RPM-
GPG-KEY-cloudera  
RUN yum install -y gcc gcc-c++ libxml2-devel libxslt-devel cyrus-sasl-devel
cyrus-sasl-gssapi cyrus-sasl-plain python-devel python-simplejson epel-release
ant  
RUN yum install -y hue hue-beeswax hue-hbase hue-impala hue-pig hue-plugins
hue-rdbms hue-search hue-spark hue-sqoop hue-zookeeper postgresql  
RUN yum install -y python-pip  
RUN pip install --upgrade pip; \  
pip install setuptools psycopg2  
RUN yum clean all  
  
COPY etc/ /etc/  
  
ADD bin/*.sh /  
RUN chmod +x /*.sh  
  
EXPOSE 8000  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

