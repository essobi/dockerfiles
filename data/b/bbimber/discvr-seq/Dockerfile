# DOCKER-VERSION 1.0.0  
#  
# The base Dockerfile for DISCVR-Seq Servers. This will install various
sequence tools used by the pipelines  
#  
from phusion/baseimage  
maintainer bbimber@gmail.com  
  
# these will vary by LabKey version:  
ENV SVN_BRANCH discvr17.3  
ENV LK_HOME /labkey  
  
#  
# Create directories required for running LabKey Server  
#  
run mkdir -p /labkey/  
run mkdir -p /labkey/bin  
run mkdir -p /labkey/svn  
  
# Update the Ubuntu and install required tools  
RUN (apt-get update; \  
apt-get -y -q install wget tar unzip subversion wget python-software-
properties software-properties-common; \  
apt-get clean -y)  
  
# Install Java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
#rm -rf /var/lib/apt/lists/* && \  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# this is not the ideal way to install all these tools, but the code is
currently shared by non-docker usages  
RUN svn co --username cpas --password cpas --no-auth-cache
https://hedgehog.fhcrc.org/tor/stedi/branches/${SVN_BRANCH}/externalModules/labModules/SequenceAnalysis/pipeline_code
${LK_HOME}/svn/  
RUN ${LK_HOME}/svn/sequence_tools_install.sh -d ${LK_HOME}  
RUN rm -Rf ${LK_HOME}/tool_src  
  
# Clean up  
RUN rm -rf /var/lib/apt/lists/*  
  
#note: need to sort out users/permissions  
#-u labkey  
#chown -R labkey:labkey $LK_HOME  

