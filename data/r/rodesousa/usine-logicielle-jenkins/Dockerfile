FROM aespinosa/jenkins:latest  
MAINTAINER pguilbault@wemanity.com  
  
# update dpkg repositories  
RUN apt-get update  
  
# install wget  
RUN apt-get install -y wget  
  
# install git  
RUN apt-get install -y git  
  
# get maven 3.2.2  
RUN wget --no-verbose -O /tmp/apache-maven-3.2.2.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.2.2/binaries/apache-
maven-3.2.2-bin.tar.gz  
  
# verify checksum  
RUN echo "87e5cc81bc4ab9b83986b3e77e6b3095 /tmp/apache-maven-3.2.2.tar.gz" |
md5sum -c  
  
# install maven  
RUN tar xzf /tmp/apache-maven-3.2.2.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.2.2 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.2.2.tar.gz  
ENV MAVEN_HOME /opt/maven  
  
ADD https://updates.jenkins-ci.org/latest/git-client.hpi /jenkins/plugins/  
ADD https://updates.jenkins-ci.org/latest/git.hpi /jenkins/plugins/  
  
# Installs Ant  
ENV ANT_VERSION 1.9.4  
RUN cd && \  
wget -q http://www.us.apache.org/dist//ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  
  
VOLUME ["/var/run/"]  

