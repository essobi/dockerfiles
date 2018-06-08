FROM ubuntu:xenial  
MAINTAINER Lawrence Mulligan <lmulligan@10thmagnitude.com>  
  
ENV HOME /home/jenkins  
RUN addgroup --system --gid 10000 jenkins  
RUN adduser --system -uid 10000 --home ${HOME} \--group jenkins  
LABEL Description="Image which provides the Jenkins agent, Packer, Ansible,
Terraform, Ruby, et al" Vendor="10th Magnitude" Version="1.00"  
  
ARG REMOTING_VERSION=3.9  
ARG PACKER_VERSION=1.1.3  
ARG TF_VERSION=0.11.2  
ARG AGENT_WORKDIR=/home/jenkins/agent  
  
# Install dev/build dependencies  
RUN apt-get update && \  
apt-get install -qy wget curl unzip git ansible ruby bundler rake
openjdk-8-jdk && \  
wget -O /tmp/packer.zip
"https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip"
&& \  
unzip -o /tmp/packer.zip -d /usr/local/bin && \  
rm -f /tmp/packer.zip && \  
wget -O /tmp/terraform.zip
"https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip"
&& \  
unzip -o /tmp/terraform.zip -d /usr/local/bin && \  
rm -f /tmp/terraform.zip && \  
curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/${REMOTING_VERSION}/remoting-${REMOTING_VERSION}.jar && \  
chmod 755 /usr/share/jenkins && \  
chmod 644 /usr/share/jenkins/slave.jar && \  
apt-get remove -qy wget curl unzip  
  
USER jenkins  
ENV AGENT_WORKDIR=${AGENT_WORKDIR}  
RUN mkdir /home/jenkins/.jenkins && mkdir -p ${AGENT_WORKDIR}  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
ENTRYPOINT ["jenkins-slave"]

