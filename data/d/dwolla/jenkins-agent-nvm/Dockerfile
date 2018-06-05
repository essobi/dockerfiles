FROM openjdk:8-jre  
LABEL maintainer="dev+jenkins-nvm@dwolla.com"  
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/jenkins-agent-
docker-nvm"  
  
ENV JENKINS_HOME=/home/jenkins \  
JENKINS_AGENT=/usr/share/jenkins \  
AGENT_VERSION=2.62.6 \  
NVM_VERSION=v0.33.6  
ENV NVM_DIR="${JENKINS_HOME}/.nvm"  
WORKDIR ${JENKINS_HOME}  
COPY jenkins-agent install.sh verify.sh /usr/local/bin/  
  
# apt-key loop inspired by https://github.com/nodejs/docker-
node/issues/340#issuecomment-321669029  
RUN set -ex && \  
apt-get update && \  
apt-get install -y \  
apt-transport-https \  
bash \  
bc \  
ca-certificates \  
curl \  
git \  
jq \  
make \  
python \  
python-pip \  
zip \  
&& \  
for key in \  
58118E89F3A912897C070ADBF76221572C52609D \  
; do \  
apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \  
apt-key adv --keyserver hkp://keyserver.pgp.com:80 --recv-keys "$key" || \  
apt-key adv --keyserver hkp://ipv4.pool.sks-keyservers.net:80 --recv-keys
"$key" ; \  
done && \  
echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install -y docker-engine && \  
pip install \  
awscli \  
virtualenv \  
&& \  
curl --create-dirs -sSLo ${JENKINS_AGENT}/agent.jar https://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar && \  
chmod 755 ${JENKINS_AGENT} && \  
chmod 644 ${JENKINS_AGENT}/agent.jar && \  
mkdir -p ${JENKINS_HOME} && \  
useradd --home ${JENKINS_HOME} \--system jenkins && \  
chown -R jenkins ${JENKINS_HOME} && \  
chmod 755 /usr/local/bin/jenkins-agent && \  
apt-get clean  
  
USER jenkins  
  
RUN curl -L
https://raw.githubusercontent.com/creationix/nvm/${NVM_VERSION}/install.sh |
/bin/bash && \  
git config --global user.email "dev+jenkins@dwolla.com" && \  
git config --global user.name "Jenkins Build Agent"  
  
ENTRYPOINT ["jenkins-agent"]  

