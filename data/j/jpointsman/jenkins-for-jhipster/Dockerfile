FROM jenkins:2.7.1  
MAINTAINER JPointsman (jpointsman@gmail.com)  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_HOME /usr/share/maven  
ENV PATH "$PATH:$MAVEN_HOME/bin"  
ENV GRADLE_VERSION 2.14  
ENV GRADLE_HOME /gradle-$GRADLE_VERSION  
ENV PATH "$PATH:$GRADLE_HOME/bin"  
USER root  
  
# install utilities  
RUN apt-get -y update && \  
apt-get -y install \  
wget \  
curl \  
vim \  
nano \  
sudo \  
bzip2 \  
unzip \  
fontconfig  
  
# install maven  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# install gradle  
RUN wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip gradle-${GRADLE_VERSION}-bin.zip  
  
# install node.js  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo bash -  
RUN apt-get install -y nodejs python g++ build-essential  
  
# update npm  
RUN npm install --silent -g npm  
# install yeoman bower grunt gulp  
RUN npm install --silent -g yo bower grunt-cli gulp-cli gulp  
  
# clean  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* gradle-${GRADLE_VERSION}-bin.zip  
  
VOLUME /var/jenkins_home  
  
RUN chown -R jenkins:jenkins /usr/lib/node_modules  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
USER jenkins  

