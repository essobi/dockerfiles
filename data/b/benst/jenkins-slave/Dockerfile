FROM centos:7  
LABEL maintainer "Benjamin Stein <info@diffus.org>"  
RUN yum install -y epel-release  
RUN yum install -y \  
aria2 \  
curl \  
git \  
java-1.8.0-openjdk.x86_64 \  
jq \  
unzip \  
wget \  
which \  
&& wget https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/2.2/swarm-client-2.2-jar-with-dependencies.jar -O /root/swarm-
client.jar  
  
ENTRYPOINT ["/usr/bin/java", "-jar", "/root/swarm-client.jar"]  

