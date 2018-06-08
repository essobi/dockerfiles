FROM phusion/baseimage  
  
ENV JAVA8_HOME=/opt/jdk1.8.0_151 \  
ANDROID_HOME=/opt/androidsdk \  
PATH="$PATH:/opt/jdk1.8.0_151/bin:/opt/androidsdk/tools:/opt/androidsdk/platform-
tools"  
  
  
RUN apt-get update -qq \  
&& apt-get install -y \--no-install-recommends wget lib32stdc++6 lib32z1 unzip
\  
&& echo 'Y' | apt-get install awscli \  
  
# fetch wget  
#RUN apt-get install -y --no-install-recommends wget  
# enable 32bit apps for android sdk  
#RUN apt-get install -y lib32stdc++6 lib32z1  
# allow to send .apk to s3 bucket on succesfull build  
#RUN echo 'Y' | apt-get install awscli  
#RUN echo 'Y' | apt-get install git  
###################  
# JDK8  
###################  
# the oracle site wants us to click a radiobox to prove we accept the license,
otherwise download will fail  
# this is for testing docker builds because oracle site is horribly slow  
# download the file somewhere and run 'python -m SimpleHTTPServer' to start a
fileserver in that directory. Replace with own IP nr.  
  
&& cd /opt \  
&& wget \--no-check-certificate \--header "Cookie: oraclelicense=accept-
securebackup-cookie" -O jdk8.tar.gz http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz
\  
#&& cd /opt && wget http://172.30.0.7:8000/jdk8.tar.gz \  
&& tar xzf jdk8.tar.gz \  
&& rm jdk8.tar.gz \  
  
#RUN cd /opt && tar xzf jdk8.tar.gz  
#RUN cd /opt && rm jdk8.tar.gz  
##################  
# Gradle 2.2.0 doesn't allow us to skip licenses, should remove when fixed.  
# https://code.google.com/p/android/issues/detail?id=212309  
##################  
&& mkdir /opt/androidsdk/ \  
&& mkdir /opt/androidsdk/licenses/ \  
&& echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >
/opt/androidsdk/licenses/android-sdk-license \  
&& echo "84831b9409646a918e30573bab4c9c91346d8abd" >
/opt/androidsdk/licenses/android-sdk-preview-license \  
&& echo "d975f751698a77b662f1254ddbeed3901e976f5a" >
/opt/androidsdk/licenses/intel-android-extra-license \  
  
###################  
# Android SDK  
###################  
# fetch android SDK  
# find url here: https://developer.android.com/sdk/index.html#Other  
&& wget -O androidsdk.zip
https://dl.google.com/android/repository/tools_r25.2.3-linux.zip \  
#&& wget -O androidsdk.tgz http://172.30.0.7:8000/androidsdk.tgz \  
&& unzip -a androidsdk.zip \  
&& rm androidsdk.zip \  
&& mv /opt/tools /opt/androidsdk/tools \  
&& echo 'y' | android update sdk \--no-ui -a \--filter platform-tools,build-
tools-25.0.2,android-25,extra-android-support,extra-google-support,extra-
google-google_play_services,extra-google-m2repository,extra-
android-m2repository \--force \  
  
  
#RUN cd /opt && tar xf androidsdk.tgz  
#RUN cd /opt && rm androidsdk.tgz  
#RUN mv /opt/android-sdk-linux /opt/androidsdk  
  
  
  
&& rm -rf /opt/androidsdk/add-ons \  
&& rm /opt/jdk1.8.0_151/src.zip \  
&& rm /opt/jdk1.8.0_151/javafx-src.zip \  
  
  
#RUN rm /opt/jdk1.8.0_151/src.zip  
#RUN rm /opt/jdk1.8.0_151/javafx-src.zip  
# fetch code and try to build  
#RUN git clone https://...@bitbucket.org/to-increase/emaintenance_android.git  
#RUN cd emaintenance_android && git checkout machine_specs  
#RUN cd emaintenance_android && ./gradlew clean assembleDebug  
##################  
# Speeding up android builds  
# gradle will pick these properties when running  
##################  
&& mkdir ~/.gradle \  
&& echo "org.gradle.daemon=true" >> ~/.gradle/gradle.properties \  
&& echo "org.gradle.jvmargs=-Xmx4096m -XX:MaxPermSize=512m
-XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8" >>
~/.gradle/gradle.properties \  
&& echo "org.gradle.parallel=true" >> ~/.gradle/gradle.properties \  
&& echo "org.gradle.configureondemand=true" >> ~/.gradle/gradle.properties \  
&& echo "android.builder.sdkDownload=true" >> ~/.gradle/gradle.properties \  
  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN echo "org.gradle.daemon=true" >> ~/.gradle/gradle.properties  
#RUN echo "org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m
-XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8" >>
~/.gradle/gradle.properties  
#RUN echo "org.gradle.parallel=true" >> ~/.gradle/gradle.properties  
#RUN echo "org.gradle.configureondemand=true" >> ~/.gradle/gradle.properties  
# running locally?  
# remember to checkout proper branch!!!  

