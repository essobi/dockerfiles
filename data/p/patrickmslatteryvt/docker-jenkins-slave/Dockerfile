FROM centos:centos7  
  
MAINTAINER Patrick M. Slattery <patrickmslattery@mac.com>  
  
ENV HOME=/home/jenkins-slave \  
JENKINS_SWARM_VERSION=2.2 \  
JENKINS_SWARM_JAR_PATH=/usr/share/jenkins  
ENV JENKINS_SWARM_JAR=${JENKINS_SWARM_JAR_PATH}/swarm-
client-${JENKINS_SWARM_VERSION}-jar-with-dependencies.jar  
  
COPY entrypoint.sh /  
  
RUN \  
# Create a user to run our tasks under  
useradd -d ${HOME} -m jenkins-slave && \  
# Update the base image if necessary  
yum clean all && \  
yum update -y && \  
# Install a modern version of Git  
yum install -y http://opensource.wandisco.com/rhel/7/git/x86_64/wandisco-git-
release-7-2.noarch.rpm && \  
# Install Java and some other tools  
yum install -y \  
epel-release \  
git \  
java-1.8.0-openjdk-headless \  
sshpass \  
wget && \  
# Install the Python libraries necessary for Ansible  
yum install -y \  
python-httplib2 \  
python-jinja2 \  
python-keyczar \  
python-paramiko \  
python-pip \  
python-setuptools \  
PyYAML && \  
# Upgrade to the latest versions of the Python libraries  
pip install \--upgrade \  
httplib2 \  
jinja2 \  
pip \  
PyYAML && \  
yum clean all && \  
# Setup the Ansible environment  
mkdir /etc/ansible/ && \  
echo -e '[local]\nlocalhost\n' > /etc/ansible/hosts && \  
# Install the latest version of Ansible from source  
mkdir -p /tmp/ansible && \  
git clone \--depth=1 \--branch=devel \--recursive
https://github.com/ansible/ansible.git /tmp/ansible && \  
cd /tmp/ansible && \  
python ./setup.py build && \  
python ./setup.py install && \  
cd / && \  
rm -rf /tmp/ansible && \  
# Install the Jenkins swarm jar  
mkdir -p ${JENKINS_SWARM_JAR_PATH} && \  
chmod 755 ${JENKINS_SWARM_JAR_PATH} && \  
curl -sSLo ${JENKINS_SWARM_JAR} https://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${JENKINS_SWARM_VERSION}/swarm-client-${JENKINS_SWARM_VERSION}-jar-
with-dependencies.jar && \  
JENKINS_SWARM_JAR_SHA1=$(curl -s https://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${JENKINS_SWARM_VERSION}/swarm-client-${JENKINS_SWARM_VERSION}-jar-
with-dependencies.jar.sha1) && \  
echo "${JENKINS_SWARM_JAR_SHA1} ${JENKINS_SWARM_JAR}" | sha1sum -c - && \  
chmod 755 /entrypoint.sh && \  
chown root:root /entrypoint.sh;  
  
USER jenkins-slave  
VOLUME ${HOME}  
  
ENTRYPOINT ["/entrypoint.sh"]

