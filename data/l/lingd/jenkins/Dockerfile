FROM ubuntu:trusty  
MAINTAINER Lingd Wan <wll_lily@126.com>  
ENV REFRESHED_AT 2015-09-24  
RUN apt-get update && apt-get install -qqy curl openjdk-7-jdk groovy graphviz
&& rm -rf /var/lib/apt/lists/*  
  
ENV JENKINS_HOME /opt/jenkins/data  
ENV JENKINS_MIRROR http://mirrors.jenkins-ci.org  
  
# install jenkins.war and plugins  
RUN mkdir -p $JENKINS_HOME/plugins  
RUN curl -o /opt/jenkins/jenkins.war -L $JENKINS_MIRROR/war-
stable/latest/jenkins.war  
  
# Install some common jenkins plugins (fits to my need)  
# git environment  
RUN for plugin in credentials credentials-binding email-ext envinject git git-
client gerrit-trigger \  
plain-credentials scm-api workflow-step-api;\  
do curl -f -o $JENKINS_HOME/plugins/${plugin}.zip \  
-L $JENKINS_MIRROR/plugins/${plugin}/latest/${plugin}.hpi ; done   
  
RUN for plugin in claim config-file-provider extended-choice-parameter groovy-
postbuild groovy job-dsl junit testng-plugin;\  
do curl -f -o $JENKINS_HOME/plugins/${plugin}.zip \  
-L $JENKINS_MIRROR/plugins/${plugin}/latest/${plugin}.hpi ; done   
  
# more needed plugin  
RUN for plugin in build-flow-plugin buildgraph-view cobertura config-file-
provider description-setter \  
global-post-script jquery junit nested-view parameterized-trigger postbuild-
task \  
show-build-parameters token-macro throttle-concurrents testng-plugin ws-
cleanup;\  
do curl -f -o $JENKINS_HOME/plugins/${plugin}.zip \  
-L $JENKINS_MIRROR/plugins/${plugin}/latest/${plugin}.hpi ; done   
  
# the credentials needs to be later version to satisfied with other plugins  
RUN touch $JENKINS_HOME/plugins/credentials.jpi.pinned  
  
ONBUILD COPY JENKINS_HOME $JENKINS_HOME  
  
# ONBUILD RUN /install-plugins.sh  
# ONBUILD RUN /pin-plugins.sh  
# start script  
COPY . /app  
  
# start script  
COPY ./start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
EXPOSE 8080  
CMD [ "/usr/local/bin/start.sh" ]

