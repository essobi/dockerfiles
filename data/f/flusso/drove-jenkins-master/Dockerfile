FROM jenkins/jenkins:2.107.1-slim  
  
MAINTAINER Joost van der Griendt <joostvdg@gmail.com>  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL version="2.107.1-1"  
LABEL description="Docker container for Jenkins Master For Docker Swarm"  
  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
  
ENV JENKINS_OPTS "$JENKINS_OPTS --prefix=/jenkins"  
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false -server
-XX:+AlwaysPreTouch"  
  
RUN /usr/local/bin/install-plugins.sh ghprb:1.40.0 async-http-client:1.9.40.0
workflow-remote-loader:1.4 docker-commons:1.11 mailer:1.20 ssh-
credentials:1.13 docker-build-step:2.0 aws-java-sdk:1.11.264 android-
signing:2.2.5 github:1.29.0 jsch:0.1.54.2 htmlpublisher:1.14
nodelabelparameter:1.7.2 dashboard-view:2.9.11 matrix-auth:2.2 dockerhub-
notification:2.2.1 conditional-buildstep:1.3.6 sse-gateway:1.15 external-
monitor-job:1.7 swarm:3.10 pubsub-light:1.12 ssh:2.5 pipeline-milestone-
step:1.3.1 workflow-basic-steps:2.6 google-oauth-plugin:0.5 multiple-scms:0.6
github-pullrequest:0.1.0-rc29 publish-over-dropbox:1.2.2 github-branch-
source:2.3.3 ssh-agent:1.15 run-condition:1.0 jenkins-design-language:1.4.2
node-iterator-api:1.5 jacoco:3.0.1 ws-cleanup:0.34 PrioritySorter:3.6.0
blueocean-rest:1.4.2 blueocean-commons:1.4.2 m2-repo-reaper:1.0 pipeline-
input-step:2.8 oauth-credentials:0.3 docker-workflow:1.15.1 momentjs:1.1.1
blueocean-display-url:2.2.0 maven-plugin:3.1 icon-shim:2.0.3 variant:1.1
blueocean-rest-impl:1.4.2 blueocean-jira:1.4.2 publish-over:0.21
timestamper:1.8.9 credentials-binding:1.15 metrics:3.1.2.11 blueocean-
pipeline-scm-api:1.4.2 jira:2.5 pipeline-graph-analysis:1.6 gravatar:2.1
handlebars:1.1.1 ec2:1.39 pam-auth:1.3 custom-tools-plugin:0.5 build-monitor-
plugin:1.12+build.201708172343 command-launcher:1.2 pegdown-formatter:1.3
nexus-artifact-uploader:2.10 file-leak-detector:1.4 blueocean-config:1.4.2
workflow-durable-task-step:2.19 gradle:1.28 durable-task:1.22 antisamy-markup-
formatter:1.5 plain-credentials:1.4 workflow-step-api:2.14 docker-
traceability:1.2 golang:1.2 blueocean-events:1.4.2 build-name-setter:1.6.9
gogs-webhook:1.0.13 favorite:2.3.1 extended-choice-parameter:0.76 github-
api:1.90 pipeline-build-step:2.7 pipeline-stage-tags-metadata:1.2.7 slack:2.3
token-macro:2.3 ldap:1.20 pipeline-stage-step:2.3 git:3.8.0 project-stats-
plugin:0.4 blueocean:1.4.2 docker-java-api:3.0.14 BlazeMeterJenkinsPlugin:4.0
android-emulator:3.0 ace-editor:1.1 nodejs:1.2.5 percentage-du-node-
column:0.1.0 hidden-parameter:0.0.4 copyartifact:1.39 pipeline-model-api:1.2.7
resource-disposer:0.8 http_request:1.8.22 checkstyle:3.50 workflow-api:2.26
github-organization-folder:1.6 blueocean-web:1.4.2 sonar:2.6.1 extra-tool-
installers:0.4 cloudbees-bitbucket-branch-source:2.2.10 ssh-slaves:1.26
junit:1.24 workflow-job:2.17 docker-plugin:1.1.3 pipeline-stage-view:2.9
pipeline-github-lib:1.0 script-security:1.42 maven-info:0.2.0 analysis-
core:1.95 scm-api:2.2.6 google-play-android-publisher:1.7 publish-over-
ssh:1.19.1 pipeline-rest-api:2.9 authentication-tokens:1.3 build-pipeline-
plugin:1.5.8 mercurial:2.3 branch-api:2.0.18 build-timeout:1.19 mask-
passwords:2.11.0 built-on-column:1.1 jenkinslint:0.14.0 matrix-project:1.12
jquery-detached:1.2.1 android-lint:2.6 groovy:2.0 pipeline-model-
extensions:1.2.7 mapdb-api:1.0.9.0 translation:1.16 blueocean-pipeline-
editor:1.4.2 build-keeper-plugin:1.3 apache-httpcomponents-
client-4-api:4.5.3-2.1 ant:1.8 repository-connector:1.2.3 notification:1.12
dependencyanalyzer:0.7 blueocean-github-pipeline:1.4.2 pipeline-aggregator-
view:1.8 jackson2-api:2.8.11.1 pipeline-model-declarative-agent:1.1.1
blueocean-pipeline-api-impl:1.4.2 blueocean-personalization:1.4.2 blueocean-
autofavorite:1.2.2 pipeline-model-definition:1.2.7 publish-over-ftp:1.15
Exclusion:0.12 pipeline-utility-steps:2.0.1 systemloadaverage-monitor:1.2
simple-theme-plugin:0.4 credentials:2.1.16 workflow-cps:2.45 junit-
attachments:1.5 blueocean-jwt:1.4.2 email-ext:2.61 job-parameter-summary:0.5
job-dsl:1.68 logstash:1.4.0 project-description-setter:1.2 stashNotifier:1.13
docker-custom-build-environment:1.7.3 bouncycastle-api:2.16.2 workflow-
support:2.18 cloudbees-folder:6.3 blueocean-core-js:1.4.2 config-file-
provider:2.18 gitlab-plugin:1.5.3 lockable-resources:2.2 workflow-
multibranch:2.17 jobConfigHistory:2.18 hudson-wsclean-plugin:1.0.5
parameterized-trigger:2.35.2 windows-slaves:1.3.1 build-environment:1.6
cvs:2.14 git-client:2.7.1 diskcheck:0.30 handy-uri-templates-2-api:2.1.6-1.0
port-allocator:1.8 ci-game:1.26 javadoc:1.4 display-url-api:2.2.0 docker-
build-publish:1.3.2 embeddable-build-status:1.9 nodenamecolumn:1.2 blueocean-
bitbucket-pipeline:1.4.2 rebuild:1.27 jquery:1.12.4-0 git-server:1.7 aws-
credentials:1.23 subversion:2.10.3 blueocean-dashboard:1.4.2 pipeline-
maven:3.4.3 build-with-parameters:1.4 workflow-cps-global-lib:2.9 workflow-
aggregator:2.5 description-setter:1.10 blueocean-i18n:1.4.2 blueocean-git-
pipeline:1.4.2 workflow-scm-step:2.6 structs:1.14 cloudbees-disk-usage-
simple:0.9 violations:0.7.11  

