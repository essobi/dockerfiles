FROM node:6.11.5-slim  
MAINTAINER Rémy Greinhofer <remy.greinhofer@gmail.com>  
  
# Define environment variables.  
ENV CODE_DIR=/code  
  
# Add Oracle Java.  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java.list \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
  
# Install system packages.  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
firefox-esr \  
git \  
oracle-java8-installer \  
oracle-java8-set-default \  
wget \  
xvfb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Node packages.  
RUN npm install -g \  
bower@1.8.0 \  
gulp@3.9.1 \  
polymer-cli@1.5.7  
  
# Configure bower to run as root.  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Set the the entrypoint.  
COPY xvfb.sh /usr/bin/  
ENTRYPOINT ["/usr/bin/xvfb.sh"]  
  
# Expose the `polymer serve` port.  
EXPOSE 8080  
# Create the directory containing the code.  
RUN mkdir -p "${CODE_DIR}"  
WORKDIR "${CODE_DIR}"  

