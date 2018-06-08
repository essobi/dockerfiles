FROM ubuntu:14.04  
MAINTAINER summer  
  
# install basic tools  
RUN apt-get update  
RUN apt-get install -y wget curl unzip git locales  
  
# install Android SDK dependencies  
RUN apt-get install -y openjdk-7-jdk lib32z1 lib32ncurses5 lib32bz2-1.0
g++-multilib  
# use gradle maven plugin instead  
# RUN apt-get install -y --no-install-recommends maven  
## Set LOCALE to UTF8  
#  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Main Android SDK  
RUN wget -qO- "http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz" |
tar -zxv -C /opt/  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# additional params, will pass to android update sdk command, default is empty  
# if you want to use proxy, you can pass "--proxy-host 192.168.1.7 --proxy-
port 7070", android sdk support "SOCK5 proxy"  
#  
# 附加参数，会传递到android update sdk命令，默认是空的，不需要修改  
# 如果你要使用代理，那么可以这样修改：  
# ARG ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS="--proxy-host 192.168.1.7 --proxy-
port 7070" , 支持SOCK5代理  
ARG ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS=  
  
# install android "tools", "platform-tools", "build-tools", "SDK platform"  
# build-tools  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter tools
--no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
platform-tools --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter build-
tools-23.0.2 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter build-
tools-23.0.3 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
# RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter build-
tools-24.0.1 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS  
# RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter build-
tools-24.0.2 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
# RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter build-
tools-24.0.3 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter extra-
android-support --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter extra-
android-m2repository --no-ui --force -a
${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter extra-
google-m2repository --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
  
## Android SDK  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
android-17 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
# RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
android-18 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
android-19 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
# RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
android-20 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
# RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
android-21 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
android-22 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --filter
android-23 --no-ui --force -a ${ANDROID_SDK_UPDATE_ADDITIONAL_PARAMS}  
  
# install gradle，default version is 2.14.1  
# 安装gradle，默认版本是：2.14.1  
ARG GRADLE_VERSION=2.14.1  
RUN curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
ENV GRADLE_HOME /gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# setup sshd  
RUN apt-get install -y openssh-server  
#RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
#RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
#RUN echo 'root:123456' | chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
# append envs to profile, and login by ssh to use it  
# in your jenkins slave settings, you must add "source /etc/profile && "
(notice a space at the end of commad) to Prefix Start Slave Command  
# jenkins will output log like: [SSH] Starting slave process: source
/etc/profile && cd "/workspace" && java -jar slave.jar  
RUN echo export GRADLE_HOME=/gradle >> /etc/profile  
RUN echo export ANDROID_HOME=/opt/android-sdk-linux >> /etc/profile  
RUN echo export
PATH='$PATH:$GRADLE_HOME/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools' >> /etc/profile  
RUN echo export LC_ALL=en_US.UTF-8 >> /etc/profile  
  
# copy enterpoint script  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 22  
# clean  
RUN apt-get clean  
  
VOLUME /workspace  
WORKDIR /workspace  
ENTRYPOINT ["/entrypoint.sh"]  

