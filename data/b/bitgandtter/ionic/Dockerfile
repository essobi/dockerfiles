# ionic develop image  
FROM bitgandtter/nodejs  
  
# basic env fix  
ENV TERM xterm  
  
# basic config  
VOLUME /runtime  
WORKDIR /runtime  
  
ENV ANDROID_BUILD_TOOLS_VERSION=23.0.2 \  
ANT_HOME="/usr/share/ant" \  
MAVEN_HOME="/usr/share/maven" \  
GRADLE_HOME="/usr/share/gradle" \  
ANDROID_HOME="/opt/android-sdk"  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-
tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin  
  
# install packages  
RUN dpkg --add-architecture i386  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get install -y htop nano curl git bison gperf lib32gcc1 ant gradle \  
libncurses5:i386 libstdc++6:i386 zlib1g:i386 libc6-i386 libxml2-utils make \  
zip g++ gcc unzip openjdk-8-jre openjdk-8-jdk  
  
# IonicFramework - NodeJS  
RUN npm install -g gulp bower cordova ionic gulp-uglify gulp-concat gulp-sass
\  
gulp-minify-css gulp-rename merge-stream  
  
# Clean up  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get autoremove -y  
RUN apt-get clean  
  
CMD sleep 36500d  

