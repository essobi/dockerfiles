FROM goldmann/f20  
  
RUN yum update -y  
  
RUN yum install -y java-1.7.0-openjdk-devel java-1.7.0-openjdk-headless  
  
ADD wildfly /opt/wildfly/  
  
RUN /opt/wildfly/bin/add-user.sh admin password1. --silent  
  
EXPOSE 8080:8080 9990:9990  
ENTRYPOINT /opt/wildfly/bin/standalone.sh -b 0.0.0.0
-Djboss.bind.address.management=0.0.0.0 -c standalone-full.xml  

