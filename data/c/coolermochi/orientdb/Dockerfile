FROM centos:6  
MAINTAINER coolermochi@gmail.com  
  
# install  
RUN yum install -y java-1.8.0-openjdk-devel.x86_64 | true  
RUN yum install -y tar | true  
RUN yum clean all  
  
# lang  
COPY conf/i18n /etc/sysconfig/  
RUN source /etc/sysconfig/i18n && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8  
  
# clock  
COPY conf/clock /etc/sysconfig/  
RUN source /etc/sysconfig/clock  
RUN \cp -p -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
# services  
COPY conf/services.sh /etc/  
  
# permission  
RUN chmod 777 -R /opt/ && \  
chmod 777 /etc/services.sh  
  
COPY conf/orientdb/orientdb-community-2.0.10.tar.gz /opt/  
RUN tar zxvf /opt/orientdb-community-2.0.10.tar.gz -C /opt/ && mv
/opt/orientdb-community-2.0.10 /opt/orientdb  
  
RUN chmod 777 -R /opt/orientdb/  
COPY conf/orientdb/orientdb.sh /opt/orientdb/bin/orientdb.sh  
COPY conf/orientdb/orientdb-server-config.xml /opt/orientdb/config/orientdb-
server-config.xml  
  
# port  
EXPOSE 2424 2480  
# start  
ENTRYPOINT /etc/services.sh

