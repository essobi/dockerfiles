FROM jboss/wildfly:10.1.0.Final  
  
ARG POSTGRES_DRIVER_VERSION=42.1.4  
COPY configure.sh $JBOSS_HOME/bin/  
USER root  
RUN chown jboss:jboss $JBOSS_HOME/bin/configure.sh  
RUN chmod 755 $JBOSS_HOME/bin/configure.sh  
USER jboss  
  
COPY setup-postgres-driver.cli /tmp/  
  
RUN curl -o /tmp/postgresql-$POSTGRES_DRIVER_VERSION.jar
https://jdbc.postgresql.org/download/postgresql-$POSTGRES_DRIVER_VERSION.jar  
RUN $JBOSS_HOME/bin/configure.sh /tmp/setup-postgres-driver.cli  
RUN rm /tmp/postgresql-$POSTGRES_DRIVER_VERSION.jar  
  
USER root  
RUN rm /tmp/setup-postgres-driver.cli  
USER jboss  
  
RUN $JBOSS_HOME/bin/add-user.sh admin pa55w0rd --silent  
  
EXPOSE 8080 9990  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

