#FROM node:7.8.0  
#  
#RUN apt-get update  
#  
## CURL  
#RUN apt-get install -y curl  
#  
## GRUNT  
#RUN npm install -g grunt  
#RUN npm install -g grunt-cli  
#  
## KARMA  
#RUN npm install -g karma  
#  
## PROTRACTOR  
#RUN npm install -g protractor  
#  
## JAVA  
##RUN apt-get install -y default-jre  
#RUN \  
# echo "===> add webupd8 repository..." && \  
# echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
# echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
# apt-get update && \  
# \  
# \  
# echo "===> install Java" && \  
# echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
# echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
# DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
# \  
# \  
# echo "===> clean up..." && \  
# rm -rf /var/cache/oracle-jdk8-installer && \  
# apt-get clean && \  
# rm -rf /var/lib/apt/lists/*  
#  
#  
## CHROME  
#RUN set -xe  
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
#RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list  
#RUN apt-get update -yqqq  
#RUN apt-get install -y google-chrome-stable  
#RUN export CHROME_BIN=/usr/bin/google-chrome  
#  
## WEBDRIVER  
#RUN webdriver-manager update  
  
  
  
  
  
  
  
  
FROM node:7.8.0  
  
RUN apt-get update  
  
# XVBF  
RUN apt-get -y install xvfb  
  
# CHROMIUM  
#RUN apt-get -y install chromium  
#ENV CHROME_BIN /usr/bin/chromium  
  
# CHROME  
RUN set -xe  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list  
RUN apt-get update -yqqq  
RUN apt-get install -y google-chrome-stable  
RUN export CHROME_BIN=/usr/bin/google-chrome  
  
# JAVA  
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
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# CLEAN  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
# GRUNT  
RUN npm install -g grunt  
RUN npm install -g grunt-cli  
  
# KARMA  
RUN npm install -g karma  
  
# PROTRACTOR  
RUN npm install -g protractor  
  
# WEBDRIVER  
RUN webdriver-manager update

