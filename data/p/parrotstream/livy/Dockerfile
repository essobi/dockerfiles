FROM parrotstream/centos-openjdk  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
USER root  
  
ENV LIVY_SERVER_VER 0.3.0  
ADD cloudera-cdh5.repo /etc/yum.repos.d/  
RUN rpm --import https://archive.cloudera.com/cdh5/redhat/5/x86_64/cdh/RPM-
GPG-KEY-cloudera  
RUN yum install -y spark-core git maven  
RUN yum clean all  
  
RUN git clone -b v$LIVY_SERVER_VER https://github.com/cloudera/livy.git
/tmp/livy  
RUN cd /tmp/livy; \  
mvn -DskipTests package  
  
COPY etc/ /etc/  
  
ADD bin/*.sh /  
RUN chmod +x /*.sh  
  
EXPOSE 8998  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

