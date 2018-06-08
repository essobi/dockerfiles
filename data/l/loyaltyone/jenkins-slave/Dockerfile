FROM ubuntu:16.04  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
#=====================  
# JAVA + Git + Python/Pip + wget/curl  
# @see https://github.com/cloudbees/java-build-tools-
dockerfile/blob/master/Dockerfile  
#=====================  
#================================================  
# Customize sources for apt-get  
#================================================  
RUN DISTRIB_CODENAME=$(cat /etc/*release* | grep DISTRIB_CODENAME | cut -f2
-d'=') \  
&& echo "deb http://archive.ubuntu.com/ubuntu ${DISTRIB_CODENAME} main
universe\n" > /etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu ${DISTRIB_CODENAME}-updates main
universe\n" >> /etc/apt/sources.list \  
&& echo "deb http://security.ubuntu.com/ubuntu ${DISTRIB_CODENAME}-security
main universe\n" >> /etc/apt/sources.list  
  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install software-properties-common \  
&& add-apt-repository -y ppa:git-core/ppa  
  
#========================  
# Packages:  
# OpenJDK8  
# groff is for aws-cli  
# tree is convenient for troubleshooting builds  
# Python (2.7) and Python 3  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
openssh-client \  
ca-certificates \  
openjdk-8-jdk \  
tar zip unzip \  
wget curl \  
git \  
jq \  
build-essential \  
less tree \  
python python-pip \  
python3 python3-pip groff \  
gosu \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
# workaround https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=775775  
RUN [ -f "/etc/ssl/certs/java/cacerts" ] || /var/lib/dpkg/info/ca-
certificates-java.postinst configure  
RUN pip install --upgrade pip setuptools && pip3 install --upgrade pip
setuptools  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
#========================================  
# Docker  
#========================================  
ENV DOCKER_CHANNEL stable  
ENV DOCKER_VERSION 17.12.0-ce  
ENV DOCKER_ARCH x86_64  
  
RUN if ! curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${DOCKER_ARCH}/docker-${DOCKER_VERSION}.tgz";
then \  
echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from
'${DOCKER_CHANNEL}' for '${DOCKER_ARCH}'"; \  
exit 1; \  
fi; \  
\  
tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/bin/ \  
; \  
rm docker.tgz;  
  
#========================================  
# Add Jenkins User  
#========================================  
ENV JENKINS_HOME=/home/jenkins  
  
RUN adduser --quiet --home $JENKINS_HOME \--shell /bin/bash jenkins \  
&& echo "jenkins:jenkins" | chpasswd  
  
RUN touch $JENKINS_HOME/.profile && \  
chown jenkins /home/jenkins/.profile  
  
#==================  
# Slave setup  
#==================  
ARG JENKINS_REMOTING_VERSION=3.16  
# See https://github.com/jenkinsci/docker-slave/blob/2.62/Dockerfile#L32  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/$JENKINS_REMOTING_VERSION/remoting-$JENKINS_REMOTING_VERSION.jar
\  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
COPY jenkins-slave entry-point /usr/local/bin/  
COPY logging.properties /usr/share/jenkins/logging.properties  
  
RUN chmod a+rwx $JENKINS_HOME  
WORKDIR ${JENKINS_HOME}  
  
ENTRYPOINT ["/usr/local/bin/entry-point", "/usr/local/bin/jenkins-slave"]  
  
#===================  
# AWS CLI  
#===================  
USER jenkins  
  
RUN pip3 install --user awscli  
  
# Add pip installs to path  
ENV PATH=${PATH}:${JENKINS_HOME}/.local/bin  
  
USER root  
COPY assume-role /usr/local/bin/  
RUN chmod +x /usr/local/bin/assume-role  
  
#============================  
# NVM (Node v6.11.0 )  
#============================  
COPY nvm-setup nvm-setup  
RUN chmod +x nvm-setup  
  
RUN mkdir -p $JENKINS_HOME/.nvm  
RUN git clone https://github.com/creationix/nvm.git $JENKINS_HOME/.nvm  
RUN ./nvm-setup && rm nvm-setup  
RUN chown -R jenkins:jenkins $JENKINS_HOME/.nvm  
RUN echo ". $JENKINS_HOME/.nvm/nvm.sh" > /etc/profile.d/nvm.sh && chmod +x
/etc/profile.d/nvm.sh  
  
#===================  
# RVM (Ruby 2.4)  
#===================  
# Load scripts  
COPY rvm-setup rvm-setup  
RUN chmod +x rvm-setup  
  
RUN gpg --keyserver hkp://keys.gnupg.net:80 --recv-keys D39DC0E3 && \  
curl -sSL https://get.rvm.io | bash -s stable && \  
./rvm-setup && rm rvm-setup  
  
RUN rm -rf /var/lib/apt/lists/* && apt-get clean  
RUN rm $JENKINS_HOME/.profile

