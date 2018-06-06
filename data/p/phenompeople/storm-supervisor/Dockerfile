FROM phenompeople/apache-storm:1.0.1  
MAINTAINER Rajesh Jonnalagadda (<admin.squad@phenompeople.com>)  
COPY *-server.sh /opt/deployment/  
EXPOSE 6700 6701 6702 6703 6704 6705 6706 6707 6708 6709 6710  
ADD sourcesandchannels /opt/deployment/sourcesandchannels  
RUN mkdir -p ${STORM_HOME}/logs && \  
touch ${STORM_HOME}/logs/supervisor.out && \  
chown -R phenom:phenom ${STORM_HOME}  
USER phenom  
ENTRYPOINT ["/opt/deployment/start-server.sh"]

