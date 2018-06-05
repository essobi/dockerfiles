# Wildfly server with additional configurations  
FROM jboss/wildfly:8.2.1.Final  
  
MAINTAINER Lucas Russo  
  
# User root user to install software  
USER root  
  
# Create default admin user  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
/opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
  
# Install missing dependencies  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
yum install -y git maven && yum clean all  
  
# Setup git, only for applying patches  
RUN git config --global user.email "cables-docker@cables-docker.com"  
RUN git config --global user.name "CABLES Docker"  
  
# Create build directory  
RUN mkdir -p /build  
RUN mkdir -p /build/patches  
RUN mkdir -p /deploy  
  
# Copy compilation scripts to build directory  
COPY setup-wildfly.sh \  
env-vars.sh \  
download-pre-reqs.sh \  
deploy-app.sh \  
/build/  
  
# Add our custom configuration  
ADD configuration /opt/jboss/wildfly/standalone/configuration/  
  
# Add our patches  
ADD patches /build/patches  
  
# Change to build directory  
WORKDIR /build  
  
# Compile application  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
/build/setup-wildfly.sh && \  
cp /build/wait-for-it/wait-for-it.sh / && \  
rm -rf ~/.m2 && \  
rm -rf /root/.m2 && \  
rm -rf /build/*  
  
# Copy another entrypoint for user use  
COPY scripts/docker-entrypoint.sh /  
  
# Change to root directory  
WORKDIR /  
  
# Deploy everything  
RUN mv /deploy/* /opt/jboss/wildfly/standalone/deployments/  
  
# Expose HTTPS external port  
EXPOSE 8090  
# Switch back to jboss user  
USER jboss  

