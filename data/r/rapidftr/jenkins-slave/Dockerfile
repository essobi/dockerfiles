FROM ubuntu:14.04  
# Add Build Essentials  
RUN (ln -s -f /bin/true /usr/bin/chfn) && \  
(apt-get update) && \  
(apt-get install -y --no-install-recommends openjdk-7-jdk build-essential git
openssh-client curl wget rsync lib32stdc++6 lib32z1) && \  
(apt-get clean) && \  
(rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)  
  
RUN (wget
http://apache.mirrors.timporter.net/maven/maven-3/3.2.2/binaries/apache-
maven-3.2.2-bin.tar.gz) && \  
(tar -zxf apache-maven-3.2.2-bin.tar.gz) && \  
(sudo cp -R apache-maven-3.2.2 /usr/local) && \  
(sudo ln -sf /usr/local/apache-maven-3.2.2/bin/mvn /usr/bin/mvn) && \  
(mvn --version)  
  
# Download Swarm CLI  
ADD http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-
ci/plugins/swarm-client/1.16/swarm-client-1.16-jar-with-dependencies.jar
/usr/local/bin/swarm-client.jar  
  
ENTRYPOINT ["java", "-jar", "/usr/local/bin/swarm-client.jar"]  
CMD []  

