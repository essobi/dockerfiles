FROM ubuntu:15.04  
MAINTAINER Alex Galkin <alex@galkin.club>  
  
#  
# Licensed to the Apache Software Foundation (ASF) under one or more  
# contributor license agreements. See the NOTICE file distributed with  
# this work for additional information regarding copyright ownership.  
# The ASF licenses this file to You under the Apache License, Version 2.0  
# (the "License"); you may not use this file except in compliance with  
# the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
  
#################################################  
# Inspired by  
# https://github.com/SeleniumHQ/docker-selenium/blob/master/Base/Dockerfile  
# https://github.com/cloudbees/java-build-tools-dockerfile  
#################################################  
  
  
#================================================  
# Customize sources for apt-get  
#================================================  
RUN echo "deb http://archive.ubuntu.com/ubuntu vivid main universe\n" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu vivid-updates main universe\n"
>> /etc/apt/sources.list  
  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install software-properties-common \  
&& add-apt-repository -y ppa:git-core/ppa  
  
#========================  
# Miscellaneous packages  
# iproute which is surprisingly not available in ubuntu:15.04 but is available
in ubuntu:latest  
# OpenJDK8  
# rlwrap is for azure-cli  
# groff is for aws-cli  
# tree is convenient for troubleshooting builds  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
iproute \  
openssh-client ssh-askpass\  
ca-certificates \  
openjdk-8-jdk \  
tar zip unzip \  
wget curl \  
git \  
build-essential \  
less nano tree \  
python python-pip groff \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
# workaround https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=775775  
RUN [ -f "/etc/ssl/certs/java/cacerts" ] || /var/lib/dpkg/info/ca-
certificates-java.postinst configure  
  
#==========  
# Maven  
#==========  
ENV MAVEN_VERSION 3.3.9  
  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
#========================================  
# Add normal user with passwordless sudo  
#========================================  
RUN useradd remoteuser --shell /bin/bash --create-home \  
&& usermod -a -G sudo remoteuser \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'remoteuser:secret' | chpasswd  
  
# https://raw.githubusercontent.com/SeleniumHQ/docker-
selenium/master/NodeFirefox/Dockerfile  
  
#===============  
# XVFB & FIREFOX  
#===============  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
xvfb firefox \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV SCREEN_WIDTH 1360  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
  
#===============  
# Google Chrome  
#===============  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/*  
  
#==================  
# Chrome webdriver  
#==================  
ENV CHROME_DRIVER_VERSION 2.20  
RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver
/opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION
/usr/bin/chromedriver  
  
  
  
RUN mkdir /tmp/.X11-unix  
RUN chmod -R go-rwx /tmp/* /tmp/.[!.]*  
RUN chmod 1777 /tmp/.X11-unix  
RUN chmod 1777 /tmp  
  
  
USER root  
  
RUN mkdir /home/remoteuser/serenity-project  
  
WORKDIR /home/remoteuser/serenity-project

