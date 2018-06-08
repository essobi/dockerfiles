FROM ubuntu:xenial  
MAINTAINER "moalmeida" <moalmeida@koinosystems.com>  
  
# install main dependencies  
RUN \  
apt-get -qq update && \  
apt-get install -yq software-properties-common language-pack-en build-
essential curl && \  
apt-get install -yq git-core libssl-dev libcurl4-gnutls-dev libexpat1-dev
gettext unzip libkrb5-dev  
  
# install java dependencies  
RUN \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get -qq update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -yq oracle-java8-* maven  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $JAVA_HOME/bin/:$PATH  
  
# install gradle dependencies  
RUN \  
mkdir -p /opt/gradle && cd $_ && \  
wget https://services.gradle.org/distributions/gradle-3.5-bin.zip && \  
unzip gradle-3.5-bin.zip && \  
rm gradle-3.5-bin.zip && \  
ln \--symbolic /opt/gradle/gradle-3.5/bin/gradle /usr/bin/gradle  
  
# install ruby dependencies  
RUN \  
apt-get install -yq ruby-full && \  
gem install compass  
  
# install python dependencies  
RUN \  
apt-get install -yq python-pip  
  
# install nodejs dependencies  
RUN \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -yq nodejs  
RUN \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get -qq update && \  
apt-get install -yq yarn  
  
# clean apt cache  
RUN \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
du -sh /var/cache/apt/archives && \  
rm -rf /var/lib/apt/lists/*  

