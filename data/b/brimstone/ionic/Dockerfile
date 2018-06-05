FROM ubuntu:16.04  
EXPOSE 8100  
EXPOSE 35729  
LABEL org.label-schema.url=https://github.com/brimstone/docker-ionic \  
org.label-schema.vcs-url=https://github.com/brimstone/docker-ionic.git  
  
ENV ANDROID_HOME=/opt/android-sdk-linux \  
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/android-
sdk-linux/tools \  
HOME=/myapp \  
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
  
ENTRYPOINT ["/loader"]  
  
# install packages we need on the system  
RUN dpkg --add-architecture i386 \  
&& echo "deb [arch=i386] http://us.archive.ubuntu.com/ubuntu xenial main
restricted multiverse universe" > /etc/apt/sources.list.d/i386.list \  
&& echo "deb [arch=i386] http://us.archive.ubuntu.com/ubuntu xenial-updates
main restricted multiverse universe" >> /etc/apt/sources.list.d/i386.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends nodejs wget npm openjdk-8-jdk
ant libc6:i386 zlib1g:i386 libstdc++6:i386 \  
&& apt-get clean  
  
# fix up the node one  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# install cordova and ionic  
RUN mkdir /myapp \  
&& npm install -g cordova cordova-android@4.1.x ionic lodash._shimkeys \  
&& rm -rf /myapp  
  
# install the android sdk  
# download stuff for platform 4.1 - 16  
RUN wget http://dl.google.com/android/android-sdk_r24.1.2-linux.tgz -O - \  
| tar -C /opt -zx \  
&& chmod 755 /opt/android-sdk-linux/tools/android \  
&& ( sleep 10; printf "y\n"; sleep 10; printf "y\n") \  
| /opt/android-sdk-linux/tools/android update sdk --no-ui \  
\--filter android-16,android-23,tools,build-tools-23.0.1,platform-tools-
preview  
  
COPY loader /  

