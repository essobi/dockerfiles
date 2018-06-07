FROM centos:7  
MAINTAINER Camille Meulien <camille.meulien@gmail.com>  
  
ENV HOME=/home/jenkins-slave \  
JENKINS_SWARM_VERSION=2.2 \  
JENKINS_SWARM_JAR_PATH=/usr/share/jenkins  
  
RUN yum install -y \  
java-1.8.0-openjdk \  
glibc-devel.{i686,x86_64} \  
libstdc++-devel.{i686,x86_64} \  
valgrind-devel.{i686,x86_64} \  
epel-release \  
&& yum groupinstall -y "Development Tools" \  
&& yum install -y unixODBC-devel.{i686,x86_64} \  
git \  
curl \  
wget  
  
ENV JENKINS_SWARM_JAR=${JENKINS_SWARM_JAR_PATH}/swarm-
client-${JENKINS_SWARM_VERSION}-jar-with-dependencies.jar  
  
RUN useradd -d $HOME -m jenkins-slave \  
&& mkdir -p $JENKINS_SWARM_JAR_PATH \  
&& chmod 755 $JENKINS_SWARM_JAR_PATH \  
&& curl -sSLo $JENKINS_SWARM_JAR http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar  
  
RUN env | grep -E "(JENKINS|JAVA)" > /etc/docker.properties  
  
USER jenkins-slave  
WORKDIR $HOME  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

