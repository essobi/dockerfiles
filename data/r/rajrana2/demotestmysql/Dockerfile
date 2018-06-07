FROM jboss/wildfly  
MAINTAINER rana  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-c", "standalone-full.xml",
"-b", "0.0.0.0"]  
  
RUN curl -L https://github.com/rajrana2/demotest/raw/master/DemoTest.war -o
/opt/jboss/wildfly/standalone/deployments/DemoTest.war  
  

