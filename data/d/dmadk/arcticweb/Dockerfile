FROM jboss/wildfly:8.2.0.Final  
  
# set locales for image to support UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
# need root to install dependencies  
USER root  
  
# remove jdk 7 and install jdk 8  
RUN yum remove -y java-1.7.0-openjdk-devel  
  
RUN yum install -y java-1.8.0-openjdk-devel  
  
RUN yum clean all  
  
USER jboss  
  
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
  
COPY standalone.xml /opt/jboss/wildfly/standalone/configuration/standalone.xml  
  
COPY mysql-connector-java-5.1.38-bin.jar
/opt/jboss/wildfly/modules/com/mysql/main/mysql-connector-java-5.1.38-bin.jar  
  
COPY module.xml /opt/jboss/wildfly/modules/com/mysql/main/module.xml  
  
RUN curl -o /opt/jboss/wildfly/standalone/deployments/arctic-web.zip
https://dma.ci.cloudbees.com/job/ArcticWeb-branch-
master/dk.dma.enav.arcticweb\$arcticweb/lastSuccessfulBuild/artifact/dk.dma.enav.arcticweb/arcticweb/**/*.war/*zip*/arctic-
web.zip  
  
RUN unzip -j -C /opt/jboss/wildfly/standalone/deployments/arctic-web.zip *.war
-d /opt/jboss/wildfly/standalone/deployments/  
  
RUN rm /opt/jboss/wildfly/standalone/deployments/arctic-web.zip  
  
RUN ls -la /opt/jboss/wildfly/standalone/deployments  
  
# with many thanks to https://github.com/vishnubob/wait-for-it  
COPY wait_for_it.sh /opt/jboss/wildfly/bin/wait_for_it.sh  
  
USER root  
  
RUN chmod +x /opt/jboss/wildfly/bin/wait_for_it.sh  
  
USER jboss  
  
VOLUME /opt/jboss/arcticweb /opt/jboss/wildfly/arcticweb-properties  
  
# wait for the mysql server to be ready and then start the wildfly server  
CMD ["/opt/jboss/wildfly/bin/wait_for_it.sh", "arctic_db:3306", "--
timeout=40", "--strict", "--", "/opt/jboss/wildfly/bin/standalone.sh", "-b",
"0.0.0.0", "-bmanagement", "0.0.0.0"]  

