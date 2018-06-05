FROM jboss/keycloak:latest  
  
USER root  
  
# External IP address is required  
RUN cd /opt/jboss && cp docker-entrypoint.sh docker-entrypoint.sh.original &&
awk '/keycloak\/bin\/standalone.sh/{print "export EXTERNAL_ADDR=`curl
http://169.254.169.254/latest/meta-data/local-ipv4`"}1' docker-
entrypoint.sh.original >docker-entrypoint.sh  
  
USER jboss  
  
ENV JGROUPS_VERSION 3.6.14.Final  
ENV JGROUPS_PROTOCOL s3_ping  
  
ADD jgroups/change-jgroups.sh /opt/jboss/keycloak/bin/change-jgroups.sh  
  
ADD cli/jgroups /opt/jboss/keycloak/cli/jgroups  
RUN cd /opt/jboss/keycloak && bin/jboss-cli.sh --file=cli/jgroups/standalone-
ha-configuration.cli && rm -rf /opt/jboss/keycloak/standalone-
ha/configuration/standalone_xml_history  
  
CMD ["-b", "0.0.0.0", "--server-config", "standalone-ha.xml"]  

