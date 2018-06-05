FROM ubuntu:16.04  
MAINTAINER panterag  
  
  
RUN apt-get update && apt-get install -y apt-utils curl && apt-get clean  
RUN apt-get install software-properties-common -y  
RUN apt-get install python3-software-properties -y  
RUN apt-get install python-software-properties -y  
  
# auto validate license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# update repos  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
  
# install java  
RUN apt-get install oracle-java8-installer -y  
  
RUN apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install node-gyp -g  
# install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# install meteor  
RUN curl https://install.meteor.com/ | sh  
RUN apt-get install -y openssh-client  
RUN echo 'PATH="/usr/local/node/bin:${PATH}"' >> /etc/bash.bashrc  
  
# Install firefox  
RUN apt-add-repository ppa:mozillateam/firefox-next  
RUN apt-get update  
RUN apt-get install firefox xvfb -y  

