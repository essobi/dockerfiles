FROM jenkins/jenkins:2.101  
########################################################################  
# Set ARGs and ENVs  
########################################################################  
# Proxy server definitions are required for "apt-get ..." etc.  
#  
# These are predefined
ARGs(https://docs.docker.com/engine/reference/builder/#predefined-args)  
# and we normally do not need to define explicitly. However, when  
# only HTTP_PROXY and NO_PROXY were given, we wanted to use  
# default values for the others.  
ARG HTTP_PROXY  
ARG http_proxy=${http_proxy:-${HTTP_PROXY}}  
ARG HTTPS_PROXY=${HTTPS_PROXY:-${HTTP_PROXY}}  
ARG https_proxy=${https_proxy:-${HTTPS_PROXY}}  
ARG FTP_PROXY=${FTP_PROXY:-${HTTP_PROXY}}  
ARG ftp_proxy=${ftp_proxy:-${FTP_PROXY}}  
ARG NO_PROXY  
ARG no_proxy=${no_proxy:-${NO_PROXY}}  
  
RUN echo " HTTP_PROXY=${HTTP_PROXY}\n\  
HTTPS_PROXY=${HTTPS_PROXY}\n\  
FTP_PROXY=${FTP_PROXY}\n\  
NO_PROXY=${NO_PROXY}\n\  
http_proxy=${http_proxy}\n\  
https_proxy=${https_proxy}\n\  
ftp_proxy=${ftp_proxy}\n\  
no_proxy=${no_proxy}"  
  
# Version information built into the image.  
#  
# Note: Inheritence is handled. For example, if image B is created from  
# image A and Dockerfile of both images have following lines, then  
# image B's /version.txt file containes entries for both image A  
# and image B.  
ARG HJ_BUILD_DATE=  
ARG HJ_IMAGE=  
ARG HJ_VERSION=  
RUN echo "BUILD DATE: ${HJ_BUILD_DATE}, IMAGE: ${HJ_IMAGE}, VERSION:
${HJ_VERSION}" >> /tmp/version.txt  
  
# Disable setup wizard  
ENV JAVA_OPTS="${JAVA_OPTS} -Djenkins.install.runSetupWizard=false"  
########################################################################  
# Change user - root  
########################################################################  
USER root  
  
  
########################################################################  
# Install certificates  
# * Key and certificate to access Jenkins over HTTPS  
# * Public certificates of git, svn, Artifactory, SonarCube or other services  
# accessed through HTTPS  
# * Public certificate of proxy server  
########################################################################  
COPY certs/ /hj/certs  
RUN cp /hj/certs/* /usr/local/share/ca-certificates && update-ca-certificates  
  
########################################################################  
# Install Docker client and compose  
########################################################################  
# Docker client in Jenkins container sends commands to Docker daemon of the  
# host via /var/run/docker.sock shared as volume. The solution is called  
# Docker outside of Docker(DooD).  
#  
# We used to bind-mount the docker binary from the host instead of installing  
# it into the container. But, after we upgraded the Docker, we started to get  
# "docker: error while loading shared libraries: libltdl.so.7: cannot open  
# shared object file: No such file or directory" error when we issue "docker"  
# command in the Jenkins's container. We figured out the problem was releated  
# with how docker binary was linked: dynamically or statically:
https://github.com/moby/moby/issues/22608#issuecomment-217927530  
#  
# Later on we came accross the Petazzoni's update:  
# "Former versions of this post advised to bind-mount the docker binary from  
# the host to the container. This is not reliable anymore, because the Docker  
# Engine is no longer distributed as (almost) static libraries."  
#  
# See following articles to get better understanding of Docker-in-Docker(DinD)  
# and Docker outside of Docker(DooD):  
# - Using Docker-in-Docker for your CI or testing environment? Think twice:
http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/  
# - Jenkins with DooD (Docker outside of Docker):
https://github.com/axltxl/docker-jenkins-dood  
# - Running Docker in Jenkins (in Docker): http://container-
solutions.com/running-docker-in-jenkins-in-docker/  
# - Dockerized Jenkins with Docker CLI & Compose:
https://hub.docker.com/r/johannesw/jenkins-docker-cli/  
RUN apt-get update \  
&& apt-get install -y sudo \  
&& echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Install Docker, partly from https://github.com/docker-
library/docker/blob/master/1.12/Dockerfile  
ENV DOCKER_VERSION="17.12.0-ce"  
ENV DOCKER_COMPOSE_VERSION="1.18.0"  
RUN set -x \  
&& curl -kfSL
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
-o docker.tgz \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
&& curl -kL
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-Linux-x86_64 > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& docker-compose --version  
  
########################################################################  
# Change user - jenkins  
########################################################################  
USER jenkins  
  
  
########################################################################  
# Install plugins  
########################################################################  
COPY plugins/plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
########################################################################  
# Prepare /hj directory  
########################################################################  
RUN sudo mkdir -p /hj \  
&& sudo chown -R jenkins:jenkins /hj  
  
########################################################################  
# hj - Flyway  
########################################################################  
ENV FLYWAY_HOME="/hj/flyway"  
ENV FLYWAY_VERSION=5.0.3  
RUN curl -ko /hj/flyway.tar.gz
https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& tar -xvf /hj/flyway.tar.gz -C /hj \  
&& mv /hj/flyway-${FLYWAY_VERSION} ${FLYWAY_HOME} \  
&& rm /hj/flyway.tar.gz  
ENV PATH="${FLYWAY_HOME}:${PATH}"  
########################################################################  
# hj - Maven  
########################################################################  
ENV MAVEN_HOME="/hj/maven"  
ENV MAVEN_VERSION=3.5.0  
RUN curl -ko /hj/apache-maven-bin.tar.gz
https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& tar -xvf /hj/apache-maven-bin.tar.gz -C /hj \  
&& mv /hj/apache-maven-${MAVEN_VERSION} /hj/maven \  
&& rm /hj/apache-maven-bin.tar.gz  
  
ENV PATH="${MAVEN_HOME}/bin:${PATH}"  
########################################################################  
# hj - Scripts  
########################################################################  
ENV SCRIPTS_HOME="/hj/scripts"  
COPY scripts/ ${SCRIPTS_HOME}  
RUN sudo chown -R jenkins:jenkins ${SCRIPTS_HOME}  
  
########################################################################  
# hj - ssh  
########################################################################  
# Change owner of /ssh directory and files under it to  
# jenkins user's owner (1000:1000)  
ENV SSH_HOME="/hj/ssh"  
COPY ssh/ ${SSH_HOME}  
RUN sudo chown -R jenkins:jenkins ${SSH_HOME}  
  
########################################################################  
# hj - Templates  
########################################################################  
ENV TEMPLATES_HOME="/hj/templates"  
COPY templates/ ${TEMPLATES_HOME}  
RUN sudo chown -R jenkins:jenkins ${TEMPLATES_HOME}  
  
########################################################################  
# Configure Jenkins with some defaults  
########################################################################  
# Because JENKINS_HOME directory is defined as VOLUME in Jenkins's  
# Dockerfile(https://github.com/jenkinsci/docker/blob/master/Dockerfile),  
# files copied to it does not exist when container started. Therefore,  
# JENKINS_HOME content must be copied to /usr/share/jenkins/ref instead of  
# /var/jenkins_home. While container starting, jenkins.sh  
# (https://github.com/jenkinsci/docker/blob/master/jenkins.sh) is executed  
# and it copies the files from /usr/share/jenkins/ref to /var/jenkins_home.  
COPY conf/scriptApproval.xml /usr/share/jenkins/ref/scriptApproval.xml  
COPY conf/settings.xml ${MAVEN_HOME}/conf/settings.xml  
COPY init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d  
COPY jobs/ /usr/share/jenkins/ref/jobs

