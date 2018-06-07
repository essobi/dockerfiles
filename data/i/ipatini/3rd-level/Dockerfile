FROM java:8  
# ======== Install needed OS packages ========  
# RUN apt-get update && apt-get --yes --force-yes install vim  
# ======== Download necessary software components ========  
WORKDIR /tmp  
ADD https://archive.apache.org/dist/activemq/5.15.0/apache-
activemq-5.15.0-bin.tar.gz /tmp  
ADD https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.9.0/mule-standalone-3.9.0.zip /tmp  
# ADD https://bitbucket.7bulls.eu/projects/TST/repos/melodic/raw/esper-
demo/2ndLevelEsper_app.zip?at=refs%2Fheads%2Fesper-demo
/tmp/2ndLevelEsper_app.zip  
ADD https://bitbucket.7bulls.eu/projects/TST/repos/melodic/raw/esper-
demo/2ndLevelEsper2outs_app.zip?at=refs%2Fheads%2Fesper-demo
/tmp/2ndLevelEsper2outs_app.zip  
ADD https://bitbucket.7bulls.eu/projects/TST/repos/melodic/raw/esper-demo/vms-
discovery-server.zip?at=refs%2Fheads%2Fesper-demo /tmp/vms-discovery-
server.zip  
# ADD vms-discovery-server-docker.zip /tmp/vms-discovery-server.zip  
# ======== Copy necessary software components from local context ========  
# COPY apache-activemq-5.15.0-bin.tar.gz /tmp  
# COPY mule-standalone-3.9.0.zip /tmp  
# # COPY 2ndLevelEsper_app.zip /tmp  
# COPY 2ndLevelEsper2outs_app.zip /tmp  
# COPY vms-discovery-server.zip /tmp  
# ======== Install necessary software components ========  
RUN mkdir -p /opt  
RUN tar xvzf apache-activemq-5.15.0-bin.tar.gz -C /opt  
RUN unzip mule-standalone-3.9.0.zip -d /opt  
# RUN cp 2ndLevelEsper_app.zip /opt/mule-standalone-3.9.0/apps  
RUN cp 2ndLevelEsper2outs_app.zip /opt/mule-standalone-3.9.0/apps  
RUN unzip vms-discovery-server.zip -d /opt  
  
# ======== Remove archives ========  
# RUN rm -f apache-activemq-5.15.0-bin.tar.gz mule-standalone-3.9.0.zip
2ndLevelEsper_app.zip vms-discovery-server.zip  
RUN rm -f apache-activemq-5.15.0-bin.tar.gz mule-standalone-3.9.0.zip
2ndLevelEsper2outs_app.zip vms-discovery-server.zip  
  
# ======== Create symbolic links and /logs/ directory ========  
RUN mkdir -p /logs  
RUN ln -s /opt/apache-activemq-5.15.0 /opt/activemq  
RUN ln -s /opt/apache-activemq-5.15.0/data /logs/activemq  
RUN ln -s /opt/mule-standalone-3.9.0/logs /logs/mule  
  
# ======== Fix execute permissions of VMS server scripts ========  
WORKDIR /opt/vms-discovery-server  
RUN chmod +x *.sh  
  
# ======== Define volumes ========  
# VOLUME /opt/vms-discovery-server/conf  
# VOLUME /logs  
# ======== Expose provided ports ========  
EXPOSE 2222 8161 61616  
RUN echo "3rd Level Installed"  
  
# ======== Define entrypoint script ========  
# ENTRYPOINT ["/bin/bash"]  
ENTRYPOINT ["./start-level-3.sh"]

