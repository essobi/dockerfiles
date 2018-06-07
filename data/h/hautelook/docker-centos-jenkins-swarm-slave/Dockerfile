FROM centos:7.2.1511  
MAINTAINER rgoodwin  
  
# set image release for security updates  
ENV IMAGE_RELEASE=1  
RUN yum upgrade -y > /dev/null  
  
# install epel and yum dependencies  
RUN yum install -y epel-release > /dev/null && \  
yum install -y wget git python-pip gcc python-devel libffi-devel openssl-devel
python-setuptools > /dev/null  
  
# upgrade pip  
RUN pip install --upgrade pip > /dev/null  
  
# install oracle jdk  
RUN wget -q --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.rpm &&
\  
rpm -ivh jdk-8u51-linux-x64.rpm > /dev/null && \  
rm jdk-8u51-linux-x64.rpm  
  
# install pip dependencies  
# FIXME ansible is broken for ECS deploys in newer versions than this  
ENV ANSIBLE_VERSION=2.0.2.0  
RUN pip install ansible==$ANSIBLE_VERSION boto boto3 awscli setuptools
--upgrade > /dev/null  
  
# install docker  
RUN ( curl -sSL https://get.docker.com/ | sh ) > /dev/null  
  
# download and install the jenkins swarm client jar  
ENV JENKINS_SWARM_CLIENT_VERSION 2.0  
ENV JENKINS_DATA_DIRECTORY /var/lib/jenkins  
  
RUN curl --create-dirs -sSLo "/usr/share/jenkins/swarm-client-jar-with-
dependencies.jar" \  
"http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-
ci/plugins/swarm-client/$JENKINS_SWARM_CLIENT_VERSION/swarm-
client-${JENKINS_SWARM_CLIENT_VERSION}-jar-with-dependencies.jar" && \  
chmod 755 /usr/share/jenkins  
  
# to be extra verbose about what we're doing  
USER root  
WORKDIR $JENKINS_DATA_DIRECTORY  
  
# run the jenkins swarm client as the entrypoint  
ENTRYPOINT [ "java", "-Dfile.encoding=UTF8", "-jar",
"/usr/share/jenkins/swarm-client-jar-with-dependencies.jar" ]  

