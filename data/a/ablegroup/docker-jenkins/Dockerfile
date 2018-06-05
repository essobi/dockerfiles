FROM ubuntu:xenial  
  
# Install .NET Core  
ENV DOTNET_DOWNLOAD_URL
https://download.microsoft.com/download/A/7/E/A7EF2AFF-F77B-4F77-A21B-0F7BD09A4065/dotnet-
ubuntu.16.04-x64.1.1.6.tar.gz  
  
ENV PMD_VERSION 6.3.0  
ENV PMD_DOWNLOAD_URL
https://sourceforge.net/projects/pmd/files/pmd/${PMD_VERSION}/pmd-
bin-${PMD_VERSION}.zip/download  
  
# to lazy to create symlinks for libicu55  
RUN apt-get update \  
&& apt-get install -y \  
git \  
curl \  
ant \  
apt-utils \  
ca-certificates \  
apt-transport-https \  
openjdk-8-jdk-headless \  
unzip \  
python3 \  
python3-pip \  
locales \  
software-properties-common \  
# .NET core dependencies  
ca-certificates \  
libc6 \  
libcurl3 \  
libgcc1 \  
libgssapi-krb5-2 \  
libicu55 \  
liblttng-ust0 \  
libssl1.0.0 \  
libstdc++6 \  
libunwind8 \  
libuuid1 \  
zlib1g  
  
# Import the public repository GPG keys for Microsoft  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/microsoft.list  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
  
# Add python3.6 sources  
RUN add-apt-repository ppa:jonathonf/python-3.6  
  
# Install powershell from Microsoft Repo  
RUN apt-get update \  
&& apt-get install -y \  
powershell \  
python3.6 \  
# Docker  
lsb-release \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common \  
docker-ce \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install dotnetcore  
RUN curl -SL $DOTNET_DOWNLOAD_URL \--output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
# Install pmd  
RUN curl -L ${PMD_DOWNLOAD_URL} -o pmd.zip \  
&& unzip pmd.zip \  
&& mkdir -p /opt/pmd/bin \  
&& cp -r pmd-bin-${PMD_VERSION}/lib /opt/pmd/ \  
&& cp pmd-bin-${PMD_VERSION}/bin/run.sh /opt/pmd/bin/pmd.sh \  
&& rm pmd.zip \  
&& rm -r pmd-bin-${PMD_VERSION}  
  
# Make python3 the default  
RUN ln -s /usr/bin/python3.6 /usr/bin/python  
  
# Install python packages  
RUN python -m pip install --upgrade pip \  
&& python -m pip install \  
zeep \  
simple-salesforce  
  
# set utf8 as locale  
RUN locale-gen en_US.UTF-8 \  
&& update-locale LANG=en_US.UTF-8  
  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
ARG docker_gid=117  
ARG http_port=8080  
ARG agent_port=50000  
ARG JENKINS_HOME=/var/jenkins_home  
  
ENV JENKINS_HOME $JENKINS_HOME  
ENV JENKINS_SLAVE_AGENT_PORT ${agent_port}  
  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN mkdir -p $JENKINS_HOME \  
&& chown ${uid}:${gid} $JENKINS_HOME \  
&& groupadd -g ${gid} ${group} \  
&& useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user} \  
# && DOCKER_GID=$(stat -c '%g' /var/run/docker.sock) \  
# && groupadd -g ${docker_gid} docker \  
&& groupmod -g ${docker_gid} docker \  
&& usermod -a -G docker ${user}  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME $JENKINS_HOME  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
ARG TINI_VERSION=v0.16.1  
COPY tini_pub.gpg ${JENKINS_HOME}/tini_pub.gpg  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-$(dpkg --print-architecture) -o /sbin/tini \  
&& curl -fsSL
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-$(dpkg --print-architecture).asc -o /sbin/tini.asc \  
&& gpg --import ${JENKINS_HOME}/tini_pub.gpg \  
&& gpg --verify /sbin/tini.asc \  
&& rm -rf /sbin/tini.asc /root/.gnupg \  
&& chmod +x /sbin/tini  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.107.3}  
  
# jenkins.war checksum, download will be validated using it  
ARG
JENKINS_SHA=17a9e509bec5b16bde5b50bc7f59d5f1e458a55fe433deb86fd73b865bf89ab8  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \  
&& echo "${JENKINS_SHA} /usr/share/jenkins/jenkins.war" | sha256sum -c -  
  
ENV JENKINS_UC https://updates.jenkins.io  
ENV JENKINS_UC_EXPERIMENTAL=https://updates.jenkins.io/experimental  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE ${http_port}  
  
# will be used by attached slave agents:  
EXPOSE ${agent_port}  
  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER ${user}  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
COPY tini-shim.sh /bin/tini  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  

