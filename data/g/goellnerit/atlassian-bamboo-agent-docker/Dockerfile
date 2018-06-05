FROM ubuntu:latest  
MAINTAINER Philipp Goellner <philipp@goellner.it>  
  
ENV BAMBOO_SERVER=https://build.xaltbc.de/agentServer/  
ENV BAMBOO_VERSION=5.14.1  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886
&& \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu/ precise main" >
/etc/apt/sources.list.d/java.list && \  
echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-
selections && \  
echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states \  
&& apt-get update --quiet  
RUN apt-get install --quiet --yes --force-yes libtcnative-1 xmlstarlet ssh
sudo wget curl sed unzip git ntpdate \  
&& apt-get clean  
RUN sh -c 'echo "deb https://sdkrepo.atlassian.com/debian/ stable contrib"
>>/etc/apt/sources.list' && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
B07804338C015B73 && \  
apt-get install --quiet --yes --no-install-recommends apt-transport-https && \  
apt-get update && \  
apt-get install --quiet --yes --no-install-recommends atlassian-plugin-sdk &&
\  
atlas-version && \  
mkdir -p /root/bamboo-agent-home/  
RUN wget http://www-eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
RUN tar -zxf apache-maven-3.3.9-bin.tar.gz  
RUN sudo cp -R apache-maven-3.3.9 /usr/local  
RUN sudo ln -s /usr/local/apache-maven-3.3.9/bin/mvn /usr/bin/mvn  
RUN echo ${BAMBOO_SERVER}/agentInstaller/atlassian-bamboo-agent-
installer-${BAMBOO_VERSION}.jar  
RUN wget ${BAMBOO_SERVER}/agentInstaller/atlassian-bamboo-agent-
installer-${BAMBOO_VERSION}.jar  
RUN cp atlassian-bamboo-agent-installer-${BAMBOO_VERSION}.jar /opt  
RUN mkdir -p /root/bamboo-agent-home/bin/  
RUN touch /root/bamboo-agent-home/bin/bamboo-capabilities.properties  
RUN echo 'system.git.executable=/usr/bin/git' >> /root/bamboo-agent-
home/bin/bamboo-capabilities.properties  
RUN echo 'atlassian.sdk=6.1.0' >> /root/bamboo-agent-home/bin/bamboo-
capabilities.properties  
RUN echo 'system.builder.mvn3.atlas-mvn\ 3=/usr/share/atlassian-plugin-
sdk-6.1.0/apache-maven-3.2.1' >> /root/bamboo-agent-home/bin/bamboo-
capabilities.properties  
RUN echo 'system.builder.mvn3.atlas-mvn\ 3.2=/usr/share/atlassian-plugin-
sdk-6.1.0/apache-maven-3.2.1' >> /root/bamboo-agent-home/bin/bamboo-
capabilities.properties  
RUN echo 'system.builder.mvn3.atlas-mvn\ 3.2.1=/usr/share/atlassian-plugin-
sdk-6.1.0/apache-maven-3.2.1' >> /root/bamboo-agent-home/bin/bamboo-
capabilities.properties  
RUN echo 'system.builder.mvn3.Maven\ 3=/usr/bin/mvn' >> /root/bamboo-agent-
home/bin/bamboo-capabilities.properties  
ENV DEBIAN_FRONTEND noninteractive  
  
# ------ Basic modules ------  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y \  
build-essential \  
software-properties-common \  
git \  
python \  
python-dev \  
python-pip \  
unzip \  
vim \  
curl \  
ant \  
libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 \  
libjpeg8-dev zlib1g-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# ------ Java ------  
# Based on https://github.com/dockerfile/java  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JAVA8_HOME /usr/lib/jvm/java-8-oracle  
  
  
# ------ Android SDK ------  
ENV SDK_VERSION 24.4.1  
WORKDIR /opt  
RUN \  
curl -sL https://dl.google.com/android/android-sdk_r${SDK_VERSION}-linux.tgz
-o android-sdk.tgz && \  
tar -xvzf android-sdk.tgz && \  
rm -f android-sdk.tgz  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_SDK /opt/android-sdk-linux  
ENV PATH $PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Components list via android list sdk --all --extended  
#ENV ANDROID_SDK_COMPONENTS platform-tools,build-tools-22.0.1,android-22,sys-
img-armeabi-v7a-android-22,extra-android-support,extra-
android-m2repository,extra-google-m2repository,extra-google-
google_play_services,extra-google-gcm  
#RUN \  
# echo y | android update sdk --no-ui --all --filter
"${ANDROID_SDK_COMPONENTS}"  
# Emulator  
#RUN \  
# echo "no" | android create avd \  
# --force \  
# --device "Nexus 5" \  
# --name Test_Emulator \  
# --target android-22 \  
# --abi armeabi-v7a \  
# --skin WVGA800 \  
# --sdcard 512M  
# ------ Android NDK ------  
ENV NDK_VERSION 10e  
  
WORKDIR /opt  
RUN \  
curl -sL http://dl.google.com/android/ndk/android-
ndk-r${NDK_VERSION}-linux-x86_64.bin -o android-ndk.bin && \  
chmod a+x ./android-ndk.bin && \  
./android-ndk.bin && \  
mv ./android-ndk-r${NDK_VERSION} ./android-ndk && \  
rm -f android-ndk.bin  
  
ENV ANDROID_NDK_HOME /opt/android-ndk  
ENV ANDROID_NDK /opt/android-ndk  
ENV PATH $PATH:${ANDROID_NDK_HOME}  
  
  
# ------ Gradle ------  
# Based on https://github.com/qlik-trial/gradle-docker  
ENV GRADLE_VERSION 2.5  
ENV TERM dumb  
ENV JAVA_OPTS -Xms256m -Xmx512m  
  
WORKDIR /opt  
RUN \  
curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
ENV GRADLE_HOME /opt/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
  
# ------ Python dependencies ------  
RUN pip install Pillow  
  
#RUN ssh-kegen -b 2048 -t rsa -f /tmp/sshkey -q  
#RUN cat ~/.ssh/id_rsa.pub  
RUN echo 'android.sdk=true' >> /root/bamboo-agent-home/bin/bamboo-
capabilities.properties  
RUN apt-get update && apt-get install -y wget git && rm -rf
/var/lib/apt/lists/*  
ADD https://get.docker.com/builds/Linux/x86_64/docker-1.13.0.tgz
/usr/local/bin/docker  
RUN chmod +x /usr/local/bin/docker  
#RUN echo 'Docker=true' >> /root/bamboo-agent-home/bin/bamboo-
capabilities.properties  
CMD java -jar atlassian-bamboo-agent-installer-${BAMBOO_VERSION}.jar
${BAMBOO_SERVER}  

