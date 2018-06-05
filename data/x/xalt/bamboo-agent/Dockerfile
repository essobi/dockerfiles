FROM ubuntu:latest  
MAINTAINER Philipp Goellner <philipp.goellner@xaltbc.de>  
  
ENV ANSIBLE_HOST_KEY_CHECKING=false \  
BAMBOO_AGENT_HOME=/var/atlassian/bamboo-agent \  
BAMBOO_AGENT_TIMEOUT=90 \  
BAMBOO_SERVER=false \  
RAM_MIN=256m \  
RAM_MAX=512m \  
DEBIAN_FRONTEND=noninteractive \  
GRADLE_VERSION=2.5 \  
JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
JAVA8_HOME=/usr/lib/jvm/java-8-oracle \  
LANG=C.UTF-8 \  
TIME_ZONE=false  
ENV PATH=${PATH}:/opt/gradle-${GRADLE_VERSION}/bin  
  
# ------ Basic modules ------  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install --quiet -y ansible \  
ant \  
apt-transport-https \  
apt-utils \  
build-essential \  
curl \  
git \  
gnupg \  
hugo \  
jq \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
libc6-i386 \  
libjpeg8-dev \  
libtcnative-1 \  
lsb-release \  
pandoc \  
python-dev \  
python-pip \  
python3 \  
python3-pip \  
software-properties-common \  
sed \  
ssh \  
tzdata \  
unzip \  
wget \  
xmlstarlet \  
zlib1g-dev \  
&& pip install --upgrade awscli \  
Pillow \  
&& pip3 install mws \  
numpy \  
PyMySQL \  
requests  
  
  
# Install Atlassian SDK, Docker, Java, Docker-Compose, Hugo, NodeJS, Apache-
Maven and Gradle  
RUN curl -fsSL https://packages.atlassian.com/api/gpg/key/public | apt-key add
- \  
&& add-apt-repository "deb https://packages.atlassian.com/atlassian-sdk-deb
stable contrib" \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu xenial stable" \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y atlassian-plugin-sdk \  
docker-ce=17.09.1~ce-0~ubuntu \  
oracle-java8-installer \  
&& rm -rf /var/cache/oracle-jdk8-installer \  
&& curl -fsSL
https://github.com/docker/compose/releases/download/1.16.1/docker-
compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose \  
&& chmod 0755 /usr/local/bin/docker-compose \  
&& curl -fsSL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& curl -fsSL http://www-
eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
| tar xvz -C /usr/local \  
&& ln -s /usr/local/apache-maven-3.3.9/bin/mvn /usr/bin/mvn \  
&& curl -fsSLo /opt/gradle.zip
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip \  
&& unzip /opt/gradle.zip -d /opt \  
&& rm /opt/gradle.zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD configure-and-start-root.sh /  
  
VOLUME "${BAMBOO_AGENT_HOME}" \  
"/root/.aws"  
  
ENTRYPOINT ["/configure-and-start-root.sh"]  

