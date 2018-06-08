# MIT license  
# our base image is the wildfly one  
FROM jboss/wildfly:10.1.0.Final  
  
LABEL Wildfly 10 with console enabled  
  
# Exposes the 9990 port in complement of the 8080 one, so that the Console can
be utilized  
EXPOSE 9990  
  
# Creates an administrative user for wildfly, which enables to log-in within
the console  
RUN /opt/jboss/wildfly/bin/add-user.sh -u admin -p admin --silent  
  
# Set the default command to run when the conatiner is bootstrapped  
# Tt starts WildFly in standalone mode and binds to all the network
interfaces.  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

