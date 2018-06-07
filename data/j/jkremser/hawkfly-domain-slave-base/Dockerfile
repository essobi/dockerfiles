FROM hawkular/wildfly-hawkular-agent-domain:latest  
  
MAINTAINER Jirka Kremser <jkremser@redhat.com>  
  
ADD image-data/entrypoint.sh $JBOSS_HOME/bin/entrypoint.sh  
ADD image-data/wait_for_jboss_cli.js $JBOSS_HOME/bin/wait_for_jboss_cli.js  
ADD image-data/host-slave.xml $JBOSS_HOME/domain/configuration  
  
RUN mkdir /tmp/init  
USER root  
RUN chown jboss:jboss -R $JBOSS_HOME/bin #&& yum -y install telnet nc  
USER jboss  
ONBUILD ADD init /tmp/init  
WORKDIR $JBOSS_HOME/bin  
  
ENV DOMAIN_CONTROLLER_HOST=localhost  
ENV DOMAIN_CONTROLLER_PORT=9990  
  
# by default the hostname is used as a host controller name, this can be
overridden by this env property  
#ENV HOST_CONTROLLER_NAME=host1  
  
EXPOSE 8080 9090  
  
CMD ["/opt/jboss/wildfly/bin/entrypoint.sh"]  

