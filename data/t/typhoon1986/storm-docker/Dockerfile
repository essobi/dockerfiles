FROM fedora:latest  
  
MAINTAINER wuyi <typhoon_1986@163.com>  
  
RUN yum update -y && yum install -y java tar python hostname  
  
RUN curl -s http://archive.apache.org/dist/storm/apache-storm-0.9.3/apache-
storm-0.9.3.tar.gz | \  
tar zxf - -C /opt && \  
mv /opt/apache-storm-0.9.3 /opt/apache-storm  
  
ADD storm-nimbus-daemon /  

