FROM debian:jessie  
MAINTAINER Vitus Lehner <student@vitus-lehner.de>  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
apt-get -y install wget unzip \  
ca-certificates && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV GRADLE_VERSION 3.5  
ENV GRADLE_USER_HOME /data/gradle  
RUN wget
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
unzip "gradle-${GRADLE_VERSION}-bin.zip" -d /usr/src/ && \  
rm "gradle-${GRADLE_VERSION}-bin.zip" && \  
ln -s "/usr/src/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle && \  
mkdir -p /data/gradle  
  
ADD . /opt/ulp-mir-source  
WORKDIR /opt/ulp-mir-source  
  
RUN export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8 && \  
gradle --no-daemon clean build  
CMD java -jar ./build/libs/ulp_microinforadiator-*.jar  

