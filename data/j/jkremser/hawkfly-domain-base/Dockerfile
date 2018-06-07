FROM pilhuhn/hawkfly-domain:latest  
  
MAINTAINER Jirka Kremser <jkremser@redhat.com>  
  
ADD image-data/entrypoint.sh $JBOSS_HOME/bin/entrypoint.sh  
ADD image-data/wait_for_jboss_cli.js $JBOSS_HOME/bin/wait_for_jboss_cli.js  
ADD image-data/wait_for_hawkular.sh $JBOSS_HOME/bin/wait_for_hawkular.sh  
  
RUN mkdir /tmp/init  
USER root  
RUN chown jboss:jboss -R $JBOSS_HOME/bin  
USER jboss  
ONBUILD ADD init /tmp/init  
WORKDIR $JBOSS_HOME/bin  
  
EXPOSE 8080 9990 9991 9992  
  
CMD ["/opt/jboss/wildfly/bin/entrypoint.sh"]  

