FROM fedora  
MAINTAINER Michael Vorburger <vorburger@redhat.com>  
  
# Inspired by  
# https://github.com/fedora-cloud/Fedora-Dockerfiles/blob/master/java-
openjdk-8/Dockerfile  
# https://github.com/fedora-cloud/Fedora-
Dockerfiles/blob/master/maven/Dockerfile  
RUN dnf -y update && dnf clean all  
RUN dnf -y install tar gzip git java java-devel && dnf clean all  
ENV JAVA_HOME /usr/lib/jvm/java-openjdk  
  
ENV MAVEN_VERSION 3.3.9  
RUN curl -sSL http://www-
eu.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
#
https://wiki.opendaylight.org/view/GettingStarted:Development_Environment_Setup#Edit_your_.7E.2F.m2.2Fsettings.xml  
RUN mkdir ~/.m2; curl
https://raw.githubusercontent.com/opendaylight/odlparent/master/settings.xml
--output ~/.m2/settings.xml  
  
CMD ["bash"]  
  

