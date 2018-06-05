# Yocto build image with Yocto 2.2 support (based on Ubuntu 16.04 LTS)  
FROM axellenta/yocto-build:1.1.2  
  
USER root  
  
# Install JRE 8  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -qq install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openjdk-8-jre-headless && \  
apt-get -q clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -f /var/cache/apt/*.bin && \  
find /usr/share/man -name "*.gz" | xargs rm -f  
  
# Install Jenkins swarm client  
RUN mkdir /opt/jenkins && \  
wget -q -O /opt/jenkins/swarm-client-jar-with-dependencies.jar
https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/2.2/swarm-client-2.2-jar-with-dependencies.jar  
  
USER builduser  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "java", "-jar",
"/opt/jenkins/swarm-client-jar-with-dependencies.jar"]  

