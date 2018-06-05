FROM ubuntu:16.04  
MAINTAINER Aurelian Dumanovschi <aurasd@gmail.com>  
  
ENV AGENT_DIR /opt/buildAgent  
ENV USER teamcity  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV JRE_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre  
ENV GRADLE_USER_HOME /opt/gradle  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_NDK_HOME /opt/android-sdk-linux/ndk-bundle  
ENV NDK_HOME /opt/android-sdk-linux/ndk-bundle  
ENV ANDROID_SDK_TOOLS_VERSION 3859397  
ENV SHELL /bin/bash  
ENV RUBY_VERSION 2.4  
ENV PATH "$ANDROID_HOME/emulator:$PATH"  
ENV PATH "$ANDROID_HOME/platform-tools:$PATH"  
ENV PATH "$ANDROID_HOME/tools/bin:$PATH"  
ENV PATH "$ANDROID_HOME/tools:$PATH"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common
python-software-properties \  
&& apt-add-repository ppa:brightbox/ruby-ng \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
aufs-tools wget file language-pack-en sudo openjdk-8-jdk default-jdk libpulse0
libx11-6 \  
libgl1-mesa-glx mesa-utils pciutils ruby$RUBY_VERSION ruby$RUBY_VERSION-dev
ruby ruby-switch unzip lxc \  
fontconfig libffi-dev build-essential git curl ca-certificates ca-
certificates-java \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create user  
RUN adduser --disabled-password --gecos "" $USER \  
&& sed -i -e "s/%sudo.*$/%sudo ALL=(ALL:ALL) NOPASSWD:ALL/" /etc/sudoers \  
&& usermod -a -G sudo $USER  
  
# Fix locale.  
ENV LANG en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
RUN locale-gen en_US && update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Install fastlane  
RUN ruby-switch --set ruby$RUBY_VERSION  
RUN gem install fastlane -NV --no-rdoc --no-ri  
  
# Import the Let's Encrypt Authority certificate for Java to accept TeamCity
server certificate  
RUN curl -o /root/lets-encrypt.der https://letsencrypt.org/certs/lets-
encrypt-x3-cross-signed.der \  
&& keytool -trustcacerts -keystore $JRE_HOME/lib/security/cacerts -storepass
changeit \  
-noprompt -importcert -alias lets-encrypt-x3-cross-signed -file /root/lets-encrypt.der \  
&& rm /root/lets-encrypt.der  
  
# Configure gradle  
RUN mkdir -p $GRADLE_USER_HOME \  
&& chmod 777 $GRADLE_USER_HOME  
ADD gradle.properties $GRADLE_USER_HOME/gradle.properties  
  
# Install Android command line tools  
RUN mkdir -p $ANDROID_HOME \  
&& chmod 777 $ANDROID_HOME \  
&& wget -nc https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS_VERSION}.zip \  
&& unzip sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip -d $ANDROID_HOME \  
&& rm sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip \  
&& chmod +x $ANDROID_HOME/tools/android  
  
# Install Android licenses to not accept them manually during builds  
ADD licenses.tar.gz $ANDROID_HOME/  
  
# Install ndk  
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;google;m2repository" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "extras;google;google_play_services" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "cmake;3.6.4111459" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "lldb;2.3" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "ndk-bundle" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "patcher;v4" \  
&& chown -R $USER:$USER $ANDROID_HOME  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME /opt/buildAgent  
VOLUME /opt/android-sdk-linux  
VOLUME /opt/gradle  
  
EXPOSE 9090  

