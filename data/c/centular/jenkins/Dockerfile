FROM openjdk:8-jdk  
  
RUN apt-get update && apt-get install -y --no-install-recommends git zip \  
php7.0-fpm \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-mcrypt \  
php7.0-sqlite3 \  
php7.0-xml \  
php7.0-dom \  
php7.0-mbstring \  
php7.0-zip \  
php7.0-curl \  
php7.0-gd \  
php7.0-bcmath \  
curl && rm -rf /var/lib/apt/lists/*  
  
#Install composer  
RUN curl --silent --show-error https://getcomposer.org/installer | php && mv
composer.phar /usr/local/bin/composer  
  
#Needs to match the host version  
ARG DOCKER_VERSION=1.12.6  
# Install Docker binary  
RUN curl
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz -o
docker-${DOCKER_VERSION}.tgz \  
&& tar xzf docker-${DOCKER_VERSION}.tgz -C /tmp \  
&& mv /tmp/docker/docker /usr/bin/docker \  
&& chmod +x /usr/bin/docker  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 7.5.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/bin/node /usr/bin/nodejs  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git && \  
apt-get clean && \  
npm install -g gulp bower polymer-cli generator-polymer-init-custom-build && \  
npm install git+https://github.com/centular-elements/generator-polymer-init-
ct-app  
  
ARG user=jenkins  
ARG group=docker  
ARG uid=1000  
#set this to match the docker id on the host  
ARG gid=1001  
ARG http_port=8080  
ARG agent_port=50000  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT ${agent_port}  
  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_VERSION 0.14.0  
ENV TINI_SHA 6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha256sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.60.1}  
  
# jenkins.war checksum, download will be validated using it  
ARG
JENKINS_SHA=34fde424dde0e050738f5ad1e316d54f741c237bd380bd663a07f96147bb1390  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \  
&& echo "${JENKINS_SHA} /usr/share/jenkins/jenkins.war" | sha256sum -c -  
  
ENV JENKINS_UC https://updates.jenkins.io  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
#allows jenkins user to run node updates  
RUN chown -R ${user} /usr/lib/node_modules  
  
# for main web interface:  
EXPOSE ${http_port}  
  
# will be used by attached slave agents:  
EXPOSE ${agent_port}  
  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER ${user}  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  

