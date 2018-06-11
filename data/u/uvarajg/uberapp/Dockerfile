FROM ubuntu:16.04  
MAINTAINER Uvaraj Gunasekaran <uvaraj.guna@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
NODE_VERSION=8.7.0 \  
NPM_VERSION=5.5.1 \  
IONIC_VERSION=3.19.0 \  
CORDOVA_VERSION=7.1.0 \  
UBER_APP_HOME=/var/local/git  
  
#BASIC STUFF  
RUN apt-get update \  
&& apt-get install -y python-software-properties software-properties-common
build-essential git wget curl unzip ruby \  
&& git config --global user.email "uvaraj.guna@gmail.com" \  
&& git config --global user.name "uvarajg" \  
&& curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh \  
&& bash nodesource_setup.sh \  
&& apt-get install -y nodejs \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm install -g cordova@"$CORDOVA_VERSION" ionic@"$IONIC_VERSION"  
  
RUN git clone
https://uvarajg:zKxcdcgmpSTArKTDMgqE@bitbucket.org/uvarajg/uberapp.git
/var/local/git  
  
WORKDIR /var/local/git  
  
RUN npm install @ionic/app-scripts@latest --save-dev  
  
RUN echo $PWD  
RUN echo .* *  
  
EXPOSE 8100 35729  
CMD ["ionic", "serve --address 35.185.223.14"]  

