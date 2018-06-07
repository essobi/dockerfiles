FROM tomsontom/oracle-java8-mvn:latest  
MAINTAINER eMoflon developers <contact@emoflon.org>  
  
SHELL ["/bin/bash", "-c"]  
  
# Install utilities  
RUN apt-get update && apt-get install --yes --no-install-recommends xvfb git  
  
# Download Eclipse  
ARG eclipseDownloadFile=/opt/eclipse-modeling-oxygen-1-linux-gtk-x86_64.tar.gz  
RUN mkdir -p /opt/  
RUN wget -O $eclipseDownloadFile -nv
http://ftp.fau.de/eclipse/technology/epp/downloads/release/oxygen/1/eclipse-
modeling-oxygen-1-linux-gtk-x86_64.tar.gz #f  
RUN tar -C /opt -xzf $eclipseDownloadFile  
ENV ECLIPSE_HOME=/opt/eclipse  
RUN [ -d $ECLIPSE_HOME/plugins ] || exit 1  
  
RUN wget -O ${ECLIPSE_HOME}/plugins/com.seeq.eclipse.importprojects_1.4.0.jar
-nv https://github.com/seeq12/eclipse-import-projects-
plugin/raw/master/jar/com.seeq.eclipse.importprojects_1.4.0.jar  
  
# The following prefetch Maven resources to speed up subsequent builds  
RUN git clone https://github.com/eMoflon/emoflon-core.git  
  
# Build projects with Eclipse to trigger code generation  
# We create an Eclipse workspace rooted at ./emoflon-core, import all projects
that can be found in the repo, and finally build all projects  
ARG workspacePath=./emoflon-core  
ARG repositoryRoot=./emoflon-core  
ARG
allRepositories=http://files.idi.ntnu.no/publish/plantuml/repository/,http://download.eclipse.org/releases/oxygen/,http://emoflon.org/emoflon-
core-updatesite/stable/updatesite/  
RUN $ECLIPSE_HOME/eclipse -nosplash -application
org.eclipse.equinox.p2.director -repository $allRepositories -installIU
org.moflon.core.feature.feature.group  
  
# Prefetch Maven dependencies  
RUN (cd emoflon-core; mvn clean install integration-test; exit 0)  

