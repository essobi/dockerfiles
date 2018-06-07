FROM ubuntu:16.10  
  
ENV ANGULAR_CLI_VERSION latest  
ENV GRADLE_VERSION 3.4.1 # TODO use this env var  
  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -q install -y curl sudo wget unzip \  
&& curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add \- \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get -qq update \  
&& apt-get -q install -y nodejs openjdk-8-jdk yarn \  
&& apt-get clean \  
&& rm -rf /var/lib/apt  
  
RUN wget -nv https://services.gradle.org/distributions/gradle-3.4.1-bin.zip \  
&& unzip -q gradle-3.4.1-bin.zip -d /opt/gradle \  
&& /opt/gradle/gradle-3.4.1/bin/gradle -help  
  
RUN yarn global add @angular/cli@${ANGULAR_CLI_VERSION}  

