FROM maven:3-jdk-8  
ENV VFB_OWL_VERSION=Current  
  
ENV WORKSPACE=/opt/VFB  
  
ENV JAVA_OPTS='-Xmx20g -Xms10g'  
ENV PDBuser='neo4j'  
ENV PDBpassword='neo4j'  
ENV FILESERVER='tftp://vfbds0.inf.ed.ac.uk'  
ENV PDBSERVER='http://localhost:7474'  
VOLUME /data  
  
RUN echo Building OLS && \  
mkdir -p ${WORKSPACE} && \  
cd ${WORKSPACE} && \  
git clone https://github.com/VirtualFlyBrain/OLS_configs.git && \  
git clone https://github.com/EBISPOT/OLS.git && \  
cp ${WORKSPACE}/OLS_configs/*.properties ${WORKSPACE}/OLS/ols-apps/ols-
neo4j-app/src/main/resources/ && \  
cd ${WORKSPACE}/OLS && \  
mvn clean package  
  
RUN echo Building owltools && \  
cd ${WORKSPACE} && \  
git clone https://github.com/VirtualFlyBrain/owltools.git && \  
cd ${WORKSPACE}/owltools/OWLTools-Parent && \  
mvn install  
  
RUN curl https://releases.rancher.com/install-docker/1.13.sh | sh  
  
ENV PATH=$PATH":${WORKSPACE}/owltools/OWLTools-Runner/bin:"  
COPY loadOLS.sh /opt/VFB/loadOLS.sh  
  
RUN chmod +x /opt/VFB/loadOLS.sh  
  
RUN mkdir -p /opt/VFB/jython  
  
ADD http://search.maven.org/remotecontent?filepath=org/python/jython-
standalone/2.7.0/jython-standalone-2.7.0.jar /opt/VFB/jython/jython.jar  
  
ENTRYPOINT ["/bin/bash -c /opt/VFB/loadOLS.sh"]  

