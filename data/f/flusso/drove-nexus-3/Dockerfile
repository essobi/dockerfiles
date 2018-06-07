FROM sonatype/nexus3  
  
MAINTAINER Joost van der Griendt <j.vandergriendt@flusso.nl>  
LABEL authors="Joost van der Griendt <j.vandergriendt@flusso.nl>"  
LABEL version="3.5.2-1"  
LABEL description="Docker container for Nexus 3 For Docker Swarm"  
  
ENV NEXUS_BLOB_DATA="/blob"  
USER root  
RUN mkdir -p "${NEXUS_BLOB_DATA}" \  
&& chown -R nexus:nexus ${NEXUS_BLOB_DATA}  
  
USER nexus  
  
  
RUN mkdir -p "${NEXUS_BLOB_DATA}/maven" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/npm" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/docker" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/bower" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/gitlfs" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/nuget" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/pypi" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/raw" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/rubygems" \  
&& mkdir -p "${NEXUS_BLOB_DATA}/yum"  
  
VOLUME "${NEXUS_DATA}"  
VOLUME "${NEXUS_BLOB_DATA}"  
  
WORKDIR ${NEXUS_HOME}  
  
ENV INSTALL4J_ADD_VM_PARAMS="-Xms1200m -Xmx1200m -XX:MaxDirectMemorySize=2g
-Djava.util.prefs.userRoot=${NEXUS_DATA}/javaprefs"  
CMD ["bin/nexus", "run"]  

