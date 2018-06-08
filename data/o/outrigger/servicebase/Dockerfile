FROM centos:7  
LABEL maintainer "Phase2 <outrigger@phase2technology.com>"  
  
# Install our yum wrapper.  
COPY root /  
  
# Install base packages.  
RUN yum -y install epel-release yum-plugin-ovl deltarpm && \  
yum -y update && \  
yum -y install sudo ssh curl less vim-minimal dnsutils openssl  
  
# Add the s6 overlay.  
ENV S6_VERSION v1.19.1.1  
RUN curl -L "https://github.com/just-
containers/s6-overlay/releases/download/$S6_VERSION/s6-overlay-amd64.tar.gz" >
/tmp/s6-overlay-amd64.tar.gz  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / --exclude="./bin" && \  
tar xzf /tmp/s6-overlay-amd64.tar.gz -C /usr ./bin  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 1  
# Download confd.  
ENV CONFD_VERSION 0.11.0  
RUN curl -L
"https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64" > /usr/bin/confd && \  
chmod +x /usr/bin/confd  
ENV CONFD_OPTS '--backend=env --onetime'  
# Run the s6-based init.  
ENTRYPOINT ["/init"]  
  
# Set up a standard volume for logs.  
VOLUME ["/var/log/services"]  

