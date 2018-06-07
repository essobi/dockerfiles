FROM ubuntu:17.10  
MAINTAINER Diego R. Antunes  
  
ENV NODE_VERSION 9.6.1  
ENV GRADLE_VERSION 4.5.1  
RUN apt-get upgrade  
RUN apt-get update && apt-get install -y --no-install-recommends \  
openjdk-8-jdk wget curl unzip xz-utils python build-essential ssh git  
  
# Setup certificates in openjdk-8  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y nodejs  
  
#Install Yarn  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
RUN yarn -v  
  
#Install ionic, cordova  
RUN yarn global add ionic cordova  
RUN ionic -v  
RUN cordova -v  
  
# Install gradle  
RUN \  
cd /usr/local && \  
curl -L https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
all.zip -o gradle-$GRADLE_VERSION-all.zip && \  
unzip gradle-$GRADLE_VERSION-all.zip && \  
rm gradle-$GRADLE_VERSION-all.zip  
  
# Export some environment variables  
ENV GRADLE_HOME=/usr/local/gradle-$GRADLE_VERSION  
ENV PATH=$PATH:$GRADLE_HOME/bin  
  
RUN gradle --version  
  
#SET CORDOVA PATH  
#ENV
CORDOVA_ANDROID_GRADLE_DISTRIBUTION_URL=$GRADLE_HOME/gradle-$GRADLE_VERSION-
all.zip  
WORKDIR /app  

