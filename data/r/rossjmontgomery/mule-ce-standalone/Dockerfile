# Dockerizing Mule CE  
FROM java:8u91-jdk  
  
# LABEL version="ESB 3.8.0"  
# LABEL description="Mule ESB Standalone 3.8.0."  
# MAINTAINER x@y  
# ARG MULE_ESB_VERSION  
# Define environment variables.  
ENV MULE_ESB_VERSION 3.8.1  
ENV MULE_HOME /opt/mule  
ENV MULE_BASE /opt/mule  
  
# Install Mule CE  
WORKDIR /opt  
RUN wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/$MULE_ESB_VERSION/mule-standalone-$MULE_ESB_VERSION.tar.gz  
# RUN wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.8.1/mule-standalone-3.8.1.tar.gz  
RUN tar xvzf mule-standalone-$MULE_ESB_VERSION.tar.gz  
# RUN tar xvzf mule-standalone-3.8.1.tar.gz  
RUN rm mule-standalone-$MULE_ESB_VERSION.tar.gz  
# RUN rm mule-standalone-3.8.1.tar.gz  
RUN ln -s mule-standalone-$MULE_ESB_VERSION/ mule  
# RUN ln -s mule-standalone-3.8.1/ mule  
# Define mount points.  
# VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps",
"/opt/mule/domains"]  
# Configure external access:  
# HTTP Service Port  
# Expose the necessary port ranges as required by the Mule Apps  
EXPOSE 8081  
EXPOSE 8443  
# Mule remote debugger  
EXPOSE 5000  
# Mule JMX port (must match Mule config file)  
EXPOSE 1098  
# Environment and execution:  
WORKDIR /opt/mule  
CMD bin/mule start  

