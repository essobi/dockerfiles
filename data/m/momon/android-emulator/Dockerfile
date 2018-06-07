# Android + ruby development environment for ubuntu wily.  
  
FROM ubuntu-debootstrap:wily  
  
MAINTAINER momon <momon@gmail.com>  
  
ADD entrypoint.sh /entrypoint.sh  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN chmod +x /entrypoint.sh && \  
echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-
selections && \  
echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections && \  
apt-get -y update && \  
apt-get -y install software-properties-common bzip2 net-tools socat ruby-full
ssh && \  
gem install bundler --no-ri \--no-rdoc -q && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get -y update && \  
apt-get -y install oracle-java7-installer && \  
mkdir /usr/local/android-sdk /usr/local/apache-ant && \  
wget -qO- http://dl.google.com/android/android-sdk_r23-linux.tgz | tar xz -C
/usr/local/android-sdk --strip-components=1 && \  
wget -qO- http://archive.apache.org/dist/ant/binaries/apache-
ant-1.8.4-bin.tar.gz | tar xz -C /usr/local/apache-ant --strip-components=1 &&
\  
chown -R root:root /usr/local/android-sdk && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
ENV ANDROID_HOME=/usr/local/android-sdk \  
ANT_HOME=/usr/local/apache-ant \  
JAVA_HOME=/usr/lib/jvm/java-7-oracle \  
PATH=$PATH:/usr/local/android-sdk/tools:/usr/local/android-sdk/platform-
tools:/usr/local/apache-ant/bin  
  
RUN echo "y" | android update sdk --filter platform-tool --no-ui --force && \  
echo "y" | android update sdk --filter platform --no-ui --force && \  
echo "y" | android update sdk --filter build-tools-22.0.1 \--no-ui -a && \  
echo "y" | android update sdk --filter sys-img-x86-android-19 \--no-ui -a && \  
echo "y" | android update sdk --filter sys-img-x86-android-21 \--no-ui -a && \  
echo "y" | android update sdk --filter sys-img-x86-android-22 \--no-ui -a && \  
echo "y" | android update sdk --filter sys-img-armeabi-v7a-android-19 \--no-ui
-a && \  
echo "y" | android update sdk --filter sys-img-armeabi-v7a-android-21 \--no-ui
-a && \  
echo "y" | android update sdk --filter sys-img-armeabi-v7a-android-22 \--no-ui
-a && \  
echo "y" | android update adb && \  
mkdir ${ANDROID_HOME}/tools/keymaps && \  
touch ${ANDROID_HOME}/tools/keymaps/en-us && \  
echo "root:android" | chpasswd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
echo -e "\nANDROID_HOME=/usr/local/android-sdk\nANT_HOME=/usr/local/apache-
ant\nJAVA_HOME=/usr/lib/jvm/java-7-oracle\nPATH=$PATH:/usr/local/android-
sdk/tools:/usr/local/android-sdk/platform-tools:/usr/local/apache-ant/bin" >>
/etc/env* && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
EXPOSE 22 \  
5037 \  
5554 \  
5555 \  
5900  
  
ENTRYPOINT ["/entrypoint.sh"]  

