FROM fedora:latest  
  
MAINTAINER Mohamed Ahmed <Mohamed.Ahmed@Magalix.com>  
  
RUN yum update -y && yum install -y java tar  
  
RUN curl -s http://archive.apache.org/dist/storm/apache-storm-0.9.3/apache-
storm-0.9.3.tar.gz | \  
tar zxf - -C /opt && \  
mv /opt/apache-storm-0.9.3 /opt/apache-storm  
  
ADD start.sh /  
ADD configure.sh /  
ADD conf.sh /  
ADD udacity-storm-hack-0.0.1-SNAPSHOT-jar-with-dependencies.jar /  
WORKDIR /opt/apache-storm  
ENTRYPOINT ["/start.sh"]  
#  

