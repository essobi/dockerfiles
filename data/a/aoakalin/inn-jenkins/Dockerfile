FROM cogniteev/oracle-java:java7  
  
ENV LANG C.UTF-8  
ENV JENKINS_HOME=/var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT=50000  
ENV JENKINS_UC=https://updates.jenkins.io  
ENV COPY_REFERENCE_FILE_LOG=${JENKINS_HOME}/copy_reference_file.log  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
  
WORKDIR ${JENKINS_HOME}  
  
VOLUME ${JENKINS_HOME}  
VOLUME ${MAVEN_CONFIG}  
  
COPY ["init.groovy", "/usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy"]  
COPY ["jenkins-support", "jenkins.sh", "install-plugins.sh",
"/usr/local/bin/"]  
  
EXPOSE 8080 ${JENKINS_SLAVE_AGENT_PORT}  
  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
RUN chmod +x /usr/local/bin/jenkins.sh \  
&& chmod +x /usr/local/bin/install-plugins.sh \  
\  
&& apt-get update \  
&& apt-get install -y \  
software-properties-common \  
python-software-properties \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
\  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
subversion \  
git \  
procps \  
bzr \  
mercurial \  
openssh-client \  
autoconf \  
automake \  
bzip2 \  
unzip \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
make \  
patch \  
xz-utils \  
zlib1g-dev \  
oracle-java8-installer \  
zlib1g-dev \  
xvfb \  
libxcomposite1 \  
libasound2 \  
libdbus-glib-1-2 \  
libgtk2.0-0 \  
\  
&& curl -fsSL https://github.com/krallin/tini/releases/download/v0.14.0/tini-
static-amd64 -o /bin/tini \  
&& chmod +x /bin/tini \  
\  
&& mkdir -p /usr/share/jenkins/ref/init.groovy.d \  
&& curl -fsSL https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/2.46.3/jenkins-war-2.46.3.war -o /usr/share/jenkins/jenkins.war \  
\  
&& mkdir -p /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz
https://apache.osuosl.org/maven/maven-3/3.5.0/binaries/apache-
maven-3.5.0-bin.tar.gz \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
\  
&& wget "https://download-
installer.cdn.mozilla.net/pub/firefox/releases/45.0/linux-x86_64/en-
US/firefox-45.0.tar.bz2" -O /tmp/firefox.tar.bz2 \  
&& tar xvf /tmp/firefox.tar.bz2 -C /opt \  
&& ln -s /opt/firefox/firefox /usr/bin/firefox \  
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/cache/oracle-jdk8-installer /tmp/*
/var/tmp/* /tmp/apache-maven.tar.gz \  
\  
&& install-plugins.sh \  
docker-slaves:1.0.6 \  
github-branch-source:2.0.6 \  
antisamy-markup-formatter:1.5 \  
matrix-auth:1.6 \  
pipeline-model-definition:1.1.5 \  
blueocean:1.1.1 \  
job-dsl:1.63 \  
docker-traceability:1.2 \  
ivy:1.27.1 \  
yet-another-docker-plugin:0.1.0-rc37 \  
nexus-artifact-uploader:2.9 \  
publish-over-ssh:1.17 \  
publish-over-cifs:0.3 \  
weblogic-deployer-plugin:3.6 \  
artifact-promotion:0.4.0 \  
ldap:1.15 \  
role-strategy:2.5.0 \  
email-ext:2.57.2 \  
emailext-template:1.0 \  
copyartifact:1.38.1 \  
extensible-choice-parameter:1.4.0 \  
extended-choice-parameter:0.76 \  
maven-artifact-choicelistprovider:1.1.3 \  
persistent-parameter:1.1 \  
readonly-parameters:1.0.0 \  
build-with-parameters:1.4 \  
build-monitor-plugin:1.12+build.201704111018 \  
cloudbees-disk-usage-simple:0.8 \  
cucumber-reports:3.8.0 \  
influxdb:1.12.1 \  
jacoco:2.2.1 \  
seleniumhtmlreport:1.0 \  
sonar:2.6.1 \  
text-file-operations:1.3.2 \  
ansible:0.6.2 \  
ant:1.5 \  
create-fingerprint:1.2 \  
docker-build-publish:1.3.2 \  
envinject:2.1 \  
file-operations:1.6 \  
gradle:1.26 \  
groovy:2.0 \  
http_request:1.8.20 \  
jboss:1.0.5 \  
jython:1.9 \  
liquibase-runner:1.3.0 \  
maven-plugin:2.16 \  
promoted-builds:2.29 \  
python:1.3 \  
qc:1.2.1 \  
downstream-ext:1.8 \  
jira-trigger:0.4.1 \  
workflow-aggregator:2.5 \  
build-timestamp:1.0.1 \  
golang:1.2 \  
mask-passwords:2.10.1 \  
ssh:2.4 \  
versionnumber:1.8.1 \  
xvfb:1.1.3 \  
docker-plugin:0.16.2 \  
hubot-steps:1.1.0 \  
gatling:1.2.2 \  
jira:2.3.1 \  
jira-ext:0.7 \  
livescreenshot:1.4.5 \  
maven-info:0.2.0 \  
progress-bar-column-plugin:1.0 \  
custom-job-icon:0.2 \  
description-column-plugin:1.3 \  
extra-columns:1.18 \  
pipeline-maven:2.5.0 \  
pipeline-npm:0.9.1 \  
rocketchatnotifier:0.5.1 \  
cucumber:0.0.2 \  
cucumber-living-documentation:1.0.7 \  
cucumber-testresult-plugin:0.9.7 \  
cucumber-trends-report:1.3 \  
docker-custom-build-environment:1.6.5 \  
dockerhub-notification:2.2.0 \  
hidden-parameter:0.0.4 \  
javadoc:1.4 \  
jenkins-multijob-plugin:1.25 \  
jira-steps:1.2.2 \  
jsoup:1.6.3 \  
junit-realtime-test-reporter:0.4 \  
keyboard-shortcuts-plugin:1.2 \  
matrix-combinations-parameter:1.2.0 \  
multiline-tabbar-plugin:1.1 \  
nexus-jenkins-plugin:1.2.20170428-142845.cb63c9e \  
nodejs:1.2.2 \  
sqlplus-script-runner:1.0.6 \  
validating-string-parameter:2.3 \  
packer:1.4 \  
html5-notifier-plugin:1.5 \  
ruby:1.2 \  
parallel-test-executor:1.9 \  
bootstraped-multi-test-results-report:2.1.2 \  
hudson-pview-plugin:1.8 \  
pipeline-aggregator-view:1.7 \  
radiatorviewplugin:1.29 \  
chucknorris:1.0 \  
greenballs:1.15 \  
gogs-webhook:1.0.10 \  
gerrit-trigger:2.23.3 \  
gerrit-verify-status-reporter:0.0.3 \  
ssh-slaves:1.17 \  
ws-cleanup:0.33 \  
timestamper:1.8.8 \  
job-import-plugin:1.7 \  
managed-scripts:1.3 \  
repository-connector:1.1.3 \  
saferestart:0.3 \  
svnmerge:2.6 \  
thinBackup:1.9 \  
active-directory:2.4  

