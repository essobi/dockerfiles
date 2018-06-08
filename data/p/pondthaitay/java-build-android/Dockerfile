FROM ubuntu:16.04  
  
LABEL MAINTAINER Jedsada Tiwongvorakul <pondthaitay@gmail.com>  
  
ENV LANG="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
TOOL_VER_RUBY="2.5.1"\  
JAVA_HOME="/usr/lib/jvm/java-8-oracle"  
  
RUN apt-get update -qq  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
# Do Locale gen  
&& locale-gen en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \  
curl \  
wget \  
# Common, useful  
build-essential \  
zip \  
unzip \  
awscli  
  
# Install Java 8  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \--no-install-recommends locales && \  
locale-gen en_US.UTF-8 && \  
apt-get dist-upgrade -y && \  
apt-get \--purge remove openjdk* && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
/etc/apt/sources.list.d/webupd8team-java-trusty.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-get update && \  
apt-get install -y \--no-install-recommends oracle-java8-installer oracle-
java8-set-default && \  
apt-get clean all  
  
# Install Ruby from source  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \  
build-essential \  
zlib1g-dev \  
libssl-dev \  
libreadline6-dev \  
libyaml-dev \  
libsqlite3-dev \  
&& mkdir -p /tmp/ruby-inst && cd /tmp/ruby-inst \  
&& wget -q http://cache.ruby-lang.org/pub/ruby/ruby-${TOOL_VER_RUBY}.tar.gz \  
&& tar -xvzf ruby-${TOOL_VER_RUBY}.tar.gz && cd ruby-${TOOL_VER_RUBY} \  
&& ./configure --prefix=/usr/local && make && make install \  
# cleanup  
&& cd / && rm -rf /tmp/ruby-inst \  
# gem install bundler & rubygem update  
&& gem update \--system \--no-document && gem install bundler --no-document  
  
# Install Gradle  
RUN apt-get update && apt-get -y install gradle && gradle -v  
  
# Install Maven 2  
RUN apt-get purge maven maven2 && apt-get update && apt-get -y install maven
&& mvn --version  
  
# Install Fatlane  
RUN gem install fastlane --no-document && fastlane --version  
  
# Cleaning  
RUN apt-get clean

