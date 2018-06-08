FROM buildpack-deps:jessie-scm  
  
# Install Java 8  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list.d/jessie-backports.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
locales  
  
ENV LANG C.UTF-8  
RUN locale-gen $LANG  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
-t jessie-backports \  
ca-certificates-java \  
openjdk-8-jre-headless \  
openjdk-8-jre \  
openjdk-8-jdk-headless \  
openjdk-8-jdk  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
RUN export JAVA_HOME  
  
# Install maven  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
VOLUME /root/.m2  
  
# Install node 9  
RUN set -x \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install -y \  
nodejs \  
&& npm install -g npm@latest yarn@latest  
  
# Install Chrome  
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >
/etc/apt/sources.list.d/chrome.list  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
google-chrome-stable  
  
ENV CHROME_BIN /usr/bin/google-chrome  
  
RUN groupadd --gid 999 node \  
&& useradd --uid 999 --gid node --shell /bin/bash --create-home node  
  
USER node  
RUN mkdir ~/.npm-global  
RUN npm config set prefix '~/.npm-global'  
ENV PATH=~/.npm-global/bin:$PATH  
  
RUN npm install -g @angular/cli

