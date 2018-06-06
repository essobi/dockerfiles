FROM centos:7  
RUN yum install -y docker-1.6.0  
  
RUN yum install -y git wget java-1.8.0-openjdk-devel.x86_64  
  
RUN curl -sSL -o /usr/share/java/swarm-client.jar http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/2.0/swarm-client-2.0-jar-with-dependencies.jar  
  
# use hub compiled from source so we can use GIT_TOKEN  
RUN wget https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz &&\  
tar -C /usr/local -xzf go1.5.1.linux-amd64.tar.gz &&\  
export PATH=$PATH:/usr/local/go/bin &&\  
git clone https://github.com/github/hub.git &&\  
cd hub &&\  
./script/build &&\  
cp hub /usr/bin/hub &&\  
rm -rf /hub &&\  
rm -rf /go1.5.1.linux-amd64.tar.gz &&\  
rm -rf /usr/local/go  
  
COPY mvnsettings.xml /root/.m2/settings.xml  
COPY ssh-config /root/.ssh/config  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.60-2.b27.el7_1.x86_64  
ENV JENKINS_HOME /var/jenkins_home  
  
COPY bin/swarm-client.sh /usr/local/bin/swarm-client.sh  
COPY postStart.sh /var/jenkins_home/postStart.sh  
WORKDIR /var/jenkins_home  
  
ENTRYPOINT ["/usr/local/bin/swarm-client.sh"]  

