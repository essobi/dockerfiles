FROM debian:jessie  
MAINTAINER vincent@sbr.pm  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV JAVA_VERSION 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# install java8  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VERSION}-installer shared/accepted-oracle-license-v1-1
select true | /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VERSION}-installer oracle-java${JAVA_VERSION}-set-default && \  
apt-get install -y git \  
optipng \  
libjpeg-progs \  
gifsicle \  
xvfb \  
libgconf-2-4 \  
libexif12 \  
chromium \  
supervisor \  
netcat-traditional \  
curl \  
wget \  
libfreetype6 \  
libfontconfig \  
bzip2 \  
locales && \  
locale-gen en_US.UTF-8 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
ENV MAVEN_VERSION 3.3.3  
ENV MAVEN_HOME /usr/share/maven  
ENV PATH "$PATH:$MAVEN_HOME/bin"  
  
# install maven  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.1.0  
  
# Install nodejs  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm install -g bower \  
&& npm install -g grunt-cli \  
&& npm install -g gulp  
  
RUN npm install -g protractor  
  
# Install Selenium and Chrome driver  
RUN webdriver-manager update  
  
# Add a non-privileged user for running Protrator  
RUN adduser --home /project --uid 1000 \  
\--disabled-login --disabled-password --gecos node node  
  
# Install phantomjs  
ENV PHANTOMJS_VERSION 1.9.8  
RUN mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
# Protractor test project needs to be mounted at /project  
# VOLUME ["/project"]  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
CMD [""]  
ENTRYPOINT ["/entrypoint.sh"]  

