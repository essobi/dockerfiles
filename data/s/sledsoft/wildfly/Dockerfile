FROM fedora:21  
RUN yum update -y && \  
yum clean all  
  
RUN yum install -y java-1.8.0-openjdk-devel \  
apache-ivy \  
tar \  
gzip && \  
yum clean all  
  
ENV WILDFLY_VERSION 8.2.0.Final  
ENV JBOSS_HOME /usr/share/wildfly  
  
ADD image/usr/share/docker-wildfly/setup.sh \  
image/usr/share/docker-wildfly/wildfly.sh \  
/usr/share/docker-wildfly/  
  
RUN /usr/share/docker-wildfly/setup.sh  
  
EXPOSE 8080 9990  
ADD image/ /  
  
ENTRYPOINT ["/usr/share/docker-wildfly/run.sh"]  

