FROM fedora:latest  
  
RUN yum update -y && yum install -y java tar  
  
RUN yum install python -y  
  
RUN curl -s http://archive.apache.org/dist/storm/apache-storm-0.9.3/apache-
storm-0.9.3.tar.gz | \  
tar zxf - -C /opt && \  
mv /opt/apache-storm-0.9.3 /opt/apache-storm  
  
RUN mkdir /tmp/storm-local  
  
ADD configure.sh /  

