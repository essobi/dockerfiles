FROM ubuntu:16.04  
MAINTAINER Kishore Ramanan  
  
# Expose Ports for web access and slave agents  
EXPOSE 8080  
EXPOSE 5000  
VOLUME /var/jenkins_home  
  
# Update & Install JJB and misc tools  
RUN apt-get update && apt-get install -y jenkins-job-builder && apt-get
install -y wget curl zip && apt-get install -y software-properties-common  
  
# DEBUG Tools  
RUN apt-get install -y vim elinks  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
COPY tini-static /bin/tini  
RUN chmod +x /bin/tini && echo "$TINI_SHA /bin/tini"  
  
######################################################## BUILD TOOLS
#########################################################  
# GIT  
#####  
RUN apt-get install -y git  
  
ENV user.email="jenkins@devops.com"  
ENV user.name="Jenkins"  
# JAVA  
############  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# MAVEN  
#######  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://mirror.fibergrid.in/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# Define MAVEN_HOME  
ENV MAVEN_HOME /usr/share/maven  
  
########################################################### JENKINS
###########################################################  
ENV JENKINS_VERSION 1.647  
##########################  
RUN curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
  
# Jenkins Variables  
ENV JENKINS_HOME /var/jenkins  
ENV JENKINS_PLUGINS_LOCAL $JENKINS_HOME/plugins  
ENV JENKINS_UC http://jenkins-updates.cloudbees.com  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
ENV JAVA_OPTS="-Xmx8192m"  
ENV JENKINS_OPTS="--handlerCountStartup=100 --handlerCountMax=300
--webroot=/var/cache/jenkins/war"  
# Create Directories  
RUN mkdir -p /usr/share/jenkins/ref/  
RUN mkdir -p $JENKINS_HOME  
RUN mkdir -p $JENKINS_PLUGINS_LOCAL  
RUN touch $JENKINS_HOME/copy_reference_file.log  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
# Copy initialize script for Jenkins  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
RUN chmod +x /usr/local/bin/jenkins.sh  
COPY scripts/executors.groovy $JENKINS_HOME/init.groovy.d/1executors.groovy  
COPY scripts/simple_user.groovy $JENKINS_HOME/init.groovy.d/2admin_user.groovy  
  
# Plugins script add  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN chmod +x /usr/local/bin/plugins.sh  
  
# Tini as the entry point to manage zombie processes  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# To install the plugins  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
# Copy Jenkins-Job_builder Files  
# RUN mkdir /opt/jjb && cd /opt/jjb  
# COPY jjb/ /opt/jjb/  

