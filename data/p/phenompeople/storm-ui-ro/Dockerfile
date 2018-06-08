FROM phenompeople/apache-storm:1.0.1  
MAINTAINER Rajesh Jonnalagadda (<admin.squad@phenompeople.com>)  
EXPOSE 8881  
COPY *-server.sh /opt/deployment/  
RUN mkdir -p ${STORM_HOME}/logs && \  
touch ${STORM_HOME}/logs/storm-ui.out && \  
chown -R phenom:phenom ${STORM_HOME}  
COPY topology-page-template.html /opt/storm/public/templates/topology-page-
template.html  
USER phenom  
ENTRYPOINT ["/opt/deployment/start-server.sh"]

