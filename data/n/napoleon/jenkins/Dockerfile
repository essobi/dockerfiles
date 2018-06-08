FROM jenkins/jenkins:2.114  
MAINTAINER lbognini@gmail.com  
  
ARG MAVEN_VERSION=3.5.0  
# if we want to install via apt  
USER root  
  
#Install Docker  
COPY install-docker.sh /tmp/install-docker.sh  
RUN chmod +x /tmp/install-docker.sh  
RUN /tmp/install-docker.sh  
  
# install maven  
RUN wget --no-verbose -O /tmp/apache-maven.tar.gz
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz  
# verify checksum  
RUN echo "35c39251d2af99b6624d40d801f6ff02 /tmp/apache-maven.tar.gz" | md5sum
-c  
RUN tar xzf /tmp/apache-maven.tar.gz -C /opt/ && \  
ln -s /opt/apache-maven-${MAVEN_VERSION} /opt/maven && \  
ln -s /opt/maven/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven.tar.gz  
  
ENV MAVEN_HOME /opt/maven  
  
COPY jq-linux-x86_64 $JENKINS_HOME/tools/  
RUN chmod 555 $JENKINS_HOME/tools/jq-linux-x86_64  
  
# Install mermaid and PhantomJS  
# RUN wget --no-verbose -O /tmp/phantomjs.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
# tar xzf /tmp/phantomjs.tar.bz2 -C /opt/ && \  
# ln -s /opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs &&
\  
# rm -f /tmp/phantomjs.tar.bz2  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && npm install mermaid  
  
RUN apt-get install unzip python \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py --user \  
&& ~/.local/bin/pip install awscli  
  
# drop back to the regular jenkins user - good practice  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
USER jenkins  

