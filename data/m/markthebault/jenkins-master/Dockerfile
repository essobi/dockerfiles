FROM jenkinsci/blueocean  
  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
USER root  
  
#Add maven  
RUN MAVEN_VERSION=3.3.3 \  
&& cd /usr/share \  
&& wget
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
  
RUN apk update && apk add docker && apk add alpine-sdk  
  
COPY config.xml /usr/share/jenkins/ref/config.xml.override  
  
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
COPY basic-security.groovy /usr/share/jenkins/ref/init.groovy.d  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
  
#Image specific  
COPy plugins.txt /  
RUN install-plugins.sh $(cat plugins.txt)  
  
USER ${user}  

