FROM centos:latest  
  
ENV TZ "Asia/Shanghai"  
ENV LANG zh_CN.UTF-8  
RUN localedef -f UTF-8 -i zh_CN zh_CN.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
#Installs Java  
ENV JAVA_VERSION 7u80-b15  
# ENV JAVA_NAME jdk-7u80-linux-x64  
ENV JAVA_NAME server-jre-7u80-linux-x64  
ENV JAVA_URL http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION/$JAVA_NAME.tar.gz  
ENV JAVA_HOME /usr/java/default  
RUN mkdir -p $JAVA_HOME \  
&& curl -skLH "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" $JAVA_URL \  
| tar --strip-components=1 -zxC /usr/java/default \  
&& ln -s $JAVA_HOME/lib/amd64/jli/libjli.so /usr/lib64/ \  
&& ln -s $JAVA_HOME/bin/java /usr/bin/  
  
# Installs Ant  
ENV ANT_VERSION 1.9.6  
ENV ANT_HOME /usr/share/ant  
RUN mkdir $ANT_HOME \  
&& curl -sSL https://www.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz \  
| tar --strip-components=1 -zxC $ANT_HOME \  
\--exclude="manual" \  
&& ln -s $ANT_HOME/bin/ant /usr/bin/ant  
  
# Installs Maven  
ENV MAVEN_VERSION 3.3.3  
ENV MAVEN_HOME /usr/share/maven  
RUN mkdir $MAVEN_HOME \  
&& curl -sSL
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
| tar --strip-components=1 -zxC $MAVEN_HOME \  
&& ln -s $MAVEN_HOME/bin/mvn /usr/bin/mvn  
  
# JENKINS  
ENV PATH
$JAVA_HOME/bin:$MAVEN_HOME/bin:$ANT_HOME/bin:/usr/bin/:/bin:/usr/sbin:/sbin:$PATH  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
# Jenkins is ran with user `jenkins`, uid = 1000  
# If you bind mount a volume from host/volume from a data container,  
# ensure you use same uid  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
# Jenkins home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
ENV JENKINS_VERSION 1.609.2  
ENV JENKINS_SHA 59215da16f9f8a781d185dde683c05fcf11450ef  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fL http://mirrors.jenkins-ci.org/war-
stable/$JENKINS_VERSION/jenkins.war -o /usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER jenkins  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# from a derived Dockerfile, can use `RUN plugin.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
  

