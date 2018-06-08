FROM ubuntu:16.04  
MAINTAINER Yusen QIN qin.yusen@gmail.com  
  
RUN apt-get update  
  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:admin123' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN apt-get update -qq  
  
RUN apt-get install -y openjdk-8-jdk wget expect  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
RUN cd /opt && wget -q https://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz -O android-sdk.tgz  
RUN cd /opt && tar -xvzf android-sdk.tgz  
RUN cd /opt && rm -f android-sdk.tgz  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
RUN echo y | android update sdk --no-ui --all \--filter platform-tools | grep
'package installed'  
#RUN echo y | android update sdk --no-ui --all \--filter extra-android-support
| grep 'package installed'  
  
# SDKs  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all \--filter android-25 | grep
'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter android-24 | grep
'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter android-23 | grep
'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter android-18 | grep
'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter android-16 | grep
'package installed'  
  
# build tools  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-25.0.2 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-25.0.1 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-25.0.0 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-24.0.3 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-24.0.2 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-24.0.1 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-23.0.3 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-23.0.2 |
grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter build-tools-23.0.1 |
grep 'package installed'  
  
# Android System Images, for emulators  
# Please keep these in descending order!  
#RUN echo y | android update sdk --no-ui --all \--filter sys-
img-x86_64-android-25 | grep 'package installed'  
#RUN echo y | android update sdk --no-ui --all \--filter sys-
img-x86-android-25 | grep 'package installed'  
#RUN echo y | android update sdk --no-ui --all \--filter sys-img-
armeabi-v7a-android-25 | grep 'package installed'  
  
RUN echo y | android update sdk --no-ui --all \--filter sys-
img-x86_64-android-24 | grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter sys-img-x86-android-24
| grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter sys-img-
armeabi-v7a-android-24 | grep 'package installed'  
  
#RUN echo y | android update sdk --no-ui --all \--filter sys-
img-x86-android-23 | grep 'package installed'  
#RUN echo y | android update sdk --no-ui --all \--filter sys-img-
armeabi-v7a-android-23 | grep 'package installed'  
  
# Extras  
RUN echo y | android update sdk --no-ui --all \--filter extra-
android-m2repository | grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter extra-
google-m2repository | grep 'package installed'  
RUN echo y | android update sdk --no-ui --all \--filter extra-google-
google_play_services | grep 'package installed'  
  
RUN apt-get install -y unzip  
  
# Gradle  
ENV GRADLE_VERSION 3.3  
RUN wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d ${ANDROID_HOME} \  
&& rm -rf gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_HOME ${ANDROID_HOME}/gradle-${GRADLE_VERSION}  
ENV PATH ${GRADLE_HOME}/bin:$PATH  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  

