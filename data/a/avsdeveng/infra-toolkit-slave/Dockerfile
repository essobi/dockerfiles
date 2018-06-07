FROM centos:centos7  
MAINTAINER "Andre" <andris.jersovs@accenture.com>  
  
# Software version  
ARG TERRAFORM_VERSION="0.10.6"  
ARG PACKER_VERSION="1.1.0"  
ARG ANSIBLE_VERSION="2.4.0.0"  
ARG AWS_VERSION="1.11.158"  
ARG PYPARSER_VERSION="2.18"  
ARG AZURE_VERSION="2.0.0"  
# Java Env Variables  
ENV JAVA_VERSION=1.8.0_144  
ENV JAVA_TARBALL=server-jre-8u144-linux-x64.tar.gz  
ENV JAVA_HOME=/opt/java/jdk${JAVA_VERSION}  
ENV JAVA_MAGIC="090f390dda5b47b9b721c7dfaa008135"  
ENV JAVA_VERSION_BUILD="8u144-b01"  
# Docker versions Env Variables  
ENV DOCKER_ENGINE_VERSION=17.06.2.ce-1.el7.centos  
ENV DOCKER_COMPOSE_VERSION=1.16.1  
ENV DOCKER_MACHINE_VERSION=v0.12.2  
# Swarm Env Variables (defaults)  
ENV SWARM_MASTER=http://jenkins:8080/jenkins/  
ENV SWARM_USER=jenkins  
ENV SWARM_PASSWORD=jenkins  
  
# Slave Env Variables  
ENV SLAVE_NAME="Infrastructure_Slave"  
ENV SLAVE_LABELS="docker awscli ldap-client ansible terraform packer docker"  
ENV SLAVE_MODE="exclusive"  
ENV SLAVE_EXECUTORS=1  
ENV SLAVE_DESCRIPTION="Core Jenkins Slave"  
ENV SWARM_CLIENT_VERSION="2.2"  
# Pre-requisites  
RUN yum -y install epel-release  
RUN yum install -y which \  
git \  
wget \  
tar \  
openldap-clients \  
openssl \  
perl \  
gcc \  
libffi-devel \  
openssl-devel \  
python-pip \  
PyYAML \  
python-jinja2 \  
python-httplib2 \  
python-keyczar \  
python-paramiko \  
python-setuptools \  
python-devel \  
python-simplejson \  
unzip && \  
yum clean all  
  
RUN pip install awscli==${AWS_VERSION} ansible==${ANSIBLE_VERSION}
pycparser==${PYPARSER_VERSION} azure==${AZURE_VERSION} msrestazure ansible-
lint behave selenium testinfra pywinrm  
  
RUN curl -fsSL https://get.docker.com/ | sed "s/docker-engine/docker-
engine-${DOCKER_ENGINE_VERSION}/" | sh  
  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
RUN curl -L
https://github.com/docker/machine/releases/download/${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine  
  
RUN curl -s -o /tmp/terraform.zip -k
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/terraform.zip -d /usr/bin && \  
chmod +x /usr/bin/terraform && \  
curl -s -o /tmp/packer.zip -k
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/packer.zip -d /usr/bin && \  
chmod +x /usr/bin/packer  
  
# Install Java  
RUN wget -q --no-check-certificate --directory-prefix=/tmp --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_BUILD}/${JAVA_MAGIC}/${JAVA_TARBALL}  
RUN mkdir -p /opt/java && tar -xzf /tmp/${JAVA_TARBALL} -C /opt/java/  
RUN alternatives --install /usr/bin/java java
/opt/java/jdk${JAVA_VERSION}/bin/java 100  
RUN rm -rf /tmp/* && rm -rf /var/log/*  
  
# Make Jenkins a slave by installing swarm-client  
RUN curl -s -o /bin/swarm-client.jar -k http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${SWARM_CLIENT_VERSION}/swarm-client-${SWARM_CLIENT_VERSION}-jar-with-
dependencies.jar  
  
# Start Swarm-Client  
CMD java -jar /bin/swarm-client.jar -executors ${SLAVE_EXECUTORS} -description
"${SLAVE_DESCRIPTION}" -master ${SWARM_MASTER} -username ${SWARM_USER}
-password ${SWARM_PASSWORD} -name "${SLAVE_NAME}" -labels "${SLAVE_LABELS}"
-mode ${SLAVE_MODE}  

