FROM phenompeople/apache-storm:1.1.0  
MAINTAINER Rajesh Jonnalagadda (<admin.squad@phenompeople.com>)  
EXPOSE 6627  
COPY *-server.sh /opt/deployment/  
RUN mkdir -p ${STORM_HOME}/logs && \  
touch ${STORM_HOME}/logs/nimbus.out && \  
chown -R phenom:phenom ${STORM_HOME}  
USER phenom  
ENTRYPOINT ["/opt/deployment/start-server.sh"]

