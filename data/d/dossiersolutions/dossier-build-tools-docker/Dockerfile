FROM ubuntu:16.04  
MAINTAINER Viktor Dlouhy <viktor.dlouhy@dossier.no>  
  
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
# https://github.com/cloudbees/java-build-tools-
dockerfile/blob/master/Dockerfile  
#################################################  
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
# Miscellaneous packages  
# iproute which is surprisingly not available in ubuntu:15.04 but is available
in ubuntu:latest  
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
jq \  
python python-pip groff \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
# workaround https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=775775  
RUN [ -f "/etc/ssl/certs/java/cacerts" ] || /var/lib/dpkg/info/ca-
certificates-java.postinst configure  
  
# workaround "You are using pip version 8.1.1, however version 9.0.1 is
available."  
RUN pip install --upgrade pip setuptools  
  
#==========  
# SET UTF8 Locale  
#==========  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
locales locales-all \  
&& rm -rf /var/lib/apt/lists/*  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
#==========  
# Psql Client  
#==========  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
#====================================  
# NODE JS  
# See https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-
linux-distributions  
#====================================  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash \  
&& apt-get install -y nodejs  
  
#==========  
# Maven  
#==========  
ENV MAVEN_VERSION 3.5.3  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
#=====  
# XVFB  
#=====  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
gtk2-engines-pixbuf \  
libxtst6 \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-base \  
xfonts-cyrillic \  
xfonts-scalable \  
xvfb  
  
#==========  
# Ant  
#==========  
ENV ANT_VERSION 1.10.3  
RUN curl -fsSL https://www.apache.org/dist/ant/binaries/apache-
ant-$ANT_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-ant-$ANT_VERSION /usr/share/ant \  
&& ln -s /usr/share/ant/bin/ant /usr/bin/ant  
  
ENV ANT_HOME /usr/share/ant  
  
#==========  
# Selenium  
#==========  
ENV SELENIUM_MAJOR_VERSION 3.11  
ENV SELENIUM_VERSION 3.11.0  
RUN mkdir -p /opt/selenium \  
&& wget --no-verbose http://selenium-
release.storage.googleapis.com/$SELENIUM_MAJOR_VERSION/selenium-server-
standalone-$SELENIUM_VERSION.jar -O /opt/selenium/selenium-server-
standalone.jar  
  
RUN pip install -U selenium  
  
#==========  
# AWS Cli  
#==========  
RUN pip install -U awscli  
  
#=========  
# Chrome  
#=========  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
RUN apt-get update && apt-get install -y \  
google-chrome-stable  
  
#=============  
# Chrome Driver  
#=============  
ARG CHROME_DRIVER_VERSION=2.20  
RUN wget -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip  
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/  
RUN chmod ugo+rx /usr/bin/chromedriver  
  
#====================================  
# MAVEN SETTINGS  
#====================================  
COPY settings.xml /root/.m2/settings.xml  
  
#====================================  
# XVFB INIT SCRIPT  
#====================================  
ENV SCREEN_WIDTH 1360  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
ADD xvfb_init /etc/init.d/xvfb  
RUN chmod a+x /etc/init.d/xvfb  
  
COPY entry_point.sh /opt/bin/entry_point.sh  
RUN chmod +x /opt/bin/entry_point.sh  
  
ENTRYPOINT ["/opt/bin/entry_point.sh"]  
  
EXPOSE 4444

