FROM dwolla/jenkins-agent-nucleus AS nucleus  
FROM openjdk:8-jre  
LABEL maintainer="Dwolla Dev <dev+jenkins-agent-core@dwolla.com>"  
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/jenkins-agent-
docker-core"  
  
ENV JENKINS_HOME=/home/jenkins \  
JENKINS_AGENT=/usr/share/jenkins \  
AGENT_VERSION=2.62.6  
COPY \--from=nucleus / /  
  
WORKDIR ${JENKINS_HOME}  
  
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
mkdir -p ${JENKINS_HOME} && \  
useradd --home ${JENKINS_HOME} \--system jenkins && \  
chown -R jenkins ${JENKINS_HOME} && \  
apt-get clean  
  
USER jenkins  
  
RUN git config --global user.email "dev+jenkins@dwolla.com" && \  
git config --global user.name "Jenkins Build Agent"  
  
ENTRYPOINT ["jenkins-agent"]  

