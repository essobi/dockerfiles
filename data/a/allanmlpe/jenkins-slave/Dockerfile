FROM openjdk:8-jdk  
LABEL maintainer="aml-pe@outlook.com"  
  
# sshd installation  
RUN apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openssh-server &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Git installation  
RUN apt-get update && \  
apt-get install git  
  
# Scala/SBT installation  
ENV SCALA_VERSION 2.12.4  
ENV SBT_VERSION 1.0.2  
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release  
  
RUN \  
curl -fsL
https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo >> /root/.bashrc && \  
echo "export PATH=~/scala-$SCALA_VERSION/bin:$PATH" >> /root/.bashrc  
  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
# Maven installation  
ARG MAVEN_VERSION=3.5.2  
ARG USER_HOME_DIR="/home/jenkins"  
ARG SHA=707b1f6e390a65bde4af4cdaf2a24d45fc19a6ded00fff02e91626e3e42ceaff  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
# Node, npm and angular installation  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get update \  
&& apt-get install -y nodejs \  
&& npm install -g @angular/cli --unsafe-perm  
  
# Jenkins user config  
RUN groupadd -g 1001 jenkins &&\  
useradd -m -d /home/jenkins -u 1001 -g 1001 -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
# Default command  
CMD ["/usr/sbin/sshd", "-D"]  

