FROM ubuntu:16.04  
MAINTAINER Adrian Bienkowski  
  
# -- install build essentials and tools  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
build-essential \  
ca-certificates \  
curl \  
git \  
jq \  
openjdk-8-jdk-headless \  
openssh-client \  
openssl \  
python \  
rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
# -- set agent version an workdir  
ARG VERSION=2.62.6  
ARG AGENT_WORKDIR=/home/jenkins/agent  
  
# -- install slave jar  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
# -- copy start up script  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
# -- create jenkins user and home directory  
ENV HOME /home/jenkins  
RUN groupadd -g 10000 jenkins \  
&& useradd -u 10000 -m -g jenkins jenkins  
  
# -- as jenkins user  
USER jenkins  
ENV AGENT_WORKDIR=${AGENT_WORKDIR}  
RUN mkdir /home/jenkins/.jenkins \  
&& mkdir -p /home/jenkins/.ssh \  
&& mkdir -p /home/jenkins/.m2 \  
&& mkdir -p ${AGENT_WORKDIR}  
  
# -- set working directory for the container  
WORKDIR /home/jenkins  
  
# -- set entrypoint for the container  
ENTRYPOINT ["/usr/local/bin/jenkins-slave"]  

