FROM node:7.8.0  
RUN apt-get update  
  
# CURL  
RUN apt-get install -y curl  
  
# REDIS  
RUN apt-get install -y redis-server  
#EXPOSE 6379:6379  
# MONGO 3.4  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.4.list  
RUN apt-get update  
RUN apt-get install -y mongodb-org  
#EXPOSE 27017:27017  
# UNZIP  
RUN apt-get install -y zip unzip  
  
# GRUNT  
RUN npm install -g grunt  
RUN npm install -g grunt-cli  
  
# KARMA  
RUN npm install -g karma  
  
# PROTRACTOR  
RUN npm install -g protractor  
  
# JAVA  
#RUN apt-get install -y default-jre  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
\  
\  
echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
\  
\  
echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# CHROME  
RUN set -xe  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list  
RUN apt-get update -yqqq  
RUN apt-get install -y google-chrome-stable  
RUN export CHROME_BIN=/usr/bin/google-chrome  
  
#CLEAN  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# CHROMEDRIVER 2.31  
#RUN set -e && \  
# CACHED_DOWNLOAD="${HOME}/cache/chromedriver_linux64_2.31.zip" && \  
# mkdir ${HOME}/cache/ || 0 && \  
# rm -rf "${HOME}/bin/chromedriver" && \  
# wget --continue --output-document "${CACHED_DOWNLOAD}"
"http://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip" &&
\  
# unzip -o "${CACHED_DOWNLOAD}" -d "${HOME}/bin"  
RUN CHROMEDRIVER_VERSION=2.31 && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
# WEBDRIVER  
RUN webdriver-manager clean  
  
#Fail to update webdriver  
#RUN webdriver-manager update  
#RUN webdriver-manager update --versions.chrome=${CHROMEDRIVER_VERSION}

