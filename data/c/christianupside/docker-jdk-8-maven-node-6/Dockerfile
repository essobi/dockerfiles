FROM ubuntu:14.04  
MAINTAINER James Dunnam "jamesd1184@gmail.com"  
ENV MAVEN_VERSION 3.3.9  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >
/etc/apt/sources.list.d/universe.list  
RUN apt-get update && apt-get install -y wget git curl zip monit openssh-
server git iptables ca-certificates daemon net-tools libfontconfig-dev  
  
#Install Oracle JDK 8  
#--------------------  
RUN echo "# Installing Oracle JDK 8" && \  
sudo apt-get install -y software-properties-common debconf-utils && \  
sudo add-apt-repository -y ppa:webupd8team/java && \  
sudo apt-get update && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| sudo debconf-set-selections && \  
sudo apt-get install -y oracle-java8-installer  
# Maven related  
# -------------  
ENV MAVEN_ROOT /var/lib/maven  
ENV MAVEN_HOME $MAVEN_ROOT/apache-maven-$MAVEN_VERSION  
ENV MAVEN_OPTS -Xms256m -Xmx512m  
ENV TZ=UTC  
  
RUN echo "# Installing Maven " && echo ${MAVEN_VERSION} && \  
wget --no-verbose -O /tmp/apache-maven-$MAVEN_VERSION.tar.gz \  
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz && \  
mkdir -p $MAVEN_ROOT && \  
tar xzf /tmp/apache-maven-$MAVEN_VERSION.tar.gz -C $MAVEN_ROOT && \  
ln -s $MAVEN_HOME/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven-$MAVEN_VERSION.tar.gz  
  
VOLUME /var/lib/maven  
  
# Node related  
# ------------  
RUN echo "# Installing Nodejs" && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install nodejs build-essential -y && \  
npm set strict-ssl false && \  
npm install -g npm@latest && \  
npm install -g bower grunt grunt-cli && \  
npm cache clear -f && \  
npm install -g n && \  
n stable  
  
# Timezone  
# ---------  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Git-ratchet  
# ---------  
RUN wget --no-verbose -O /tmp/git-ratchet \  
https://github.com/iangrunert/git-
ratchet/releases/download/v0.3.2/linux_amd64_git-ratchet && \  
cp /tmp/git-ratchet /usr/bin && \  
chmod 700 /usr/bin/git-ratchet  
  
# gcloud  
# --------  
ENV CLOUD_SDK_REPO cloud-sdk-trusty  
RUN echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" |
sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
- && \  
sudo apt-get update && sudo apt-get install -y google-cloud-sdk  

