FROM opennms/maven:3.5.0_8u144-jdk  
  
LABEL maintainer "Ronny Trommer <ronny@opennms.org>"  
  
ARG STRESS_TOOLS_URL=https://github.com/j-white/opennms-events-stress-
tools.git  
ARG STRESS_TOOLS_VERSION=master  
ENV STRESS_TOOLS_HOME /opt/stress-tools  
  
RUN yum -y --setopt=tsflags=nodocs update && \  
yum -y groupinstall "Development tools" && \  
yum -y install git-core \  
cmake \  
net-snmp-devel \  
postgresql-contrib && \  
yum clean all && \  
git clone ${STRESS_TOOLS_URL} ${STRESS_TOOLS_HOME} && \  
cd ${STRESS_TOOLS_HOME}  
  
RUN mkdir -p ${STRESS_TOOLS_HOME}/udpgen/build && \  
cd ${STRESS_TOOLS_HOME}/udpgen/build && \  
cmake .. && \  
make  
  
RUN cd ${STRESS_TOOLS_HOME}/jdbc-events && \  
mvn clean package && \  
rm -rf /root/.m2  
  
RUN cd ${STRESS_TOOLS_HOME}/udplistener && \  
mvn clean package && \  
rm -rf /root/.m2  
  
LABEL license="AGPLv3" \  
org.opennms.stress.tools.version="${STRESS_TOOLS_VERSION}" \  
vendor="OpenNMS Community" \  
name="OpenNMS Events Stress Tools"  

