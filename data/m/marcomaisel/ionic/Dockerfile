FROM debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux  
  
# Set the locale  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
# Install git, curl, node, ionic, yarn, Chrome  
RUN apt-get update && \  
apt-get install -y wget git unzip curl ruby ruby-dev build-essential && \  
curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
  
apt-get update && \  
apt-get install -y nodejs && \  
npm install -g npm@"5.6.0" && \  
npm install -g cordova@"8.0.0" ionic@"3.19.0" yarn@"1.3.2" && \  
npm cache clear --force && \  
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
&& \  
dpkg --unpack google-chrome-stable_current_amd64.deb && \  
apt-get install -f -y && \  
apt-get clean && \  
rm google-chrome-stable_current_amd64.deb  
  
# Install Docker for Garbage Collection  
RUN apt-get install apt-transport-https ca-certificates curl gnupg2 software-
properties-common -y && \  
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(.
/etc/os-release; echo "$ID") $(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get install docker-ce -y  
  
# Install fastlane  
RUN gem install bundler && \  
gem install fastlane -NV && \  
  
# install python-software-properties (to use add-apt-repository)  
apt-get update && apt-get install -y -q python-software-properties software-
properties-common && \  
  
# install java  
add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu
xenial main" -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get -y install oracle-java8-installer && \  
  
# System libs for android enviroment  
echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y --force-yes expect ant wget libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
# Install Android Tools  
mkdir /opt/android-sdk-linux && cd /opt/android-sdk-linux && \  
wget --output-document=android-tools-sdk.zip --quiet
https://dl.google.com/android/repository/tools_r25.2.3-linux.zip && \  
unzip -q android-tools-sdk.zip && \  
rm -f android-tools-sdk.zip && \  
chown -R root. /opt  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install Android SDK  
RUN yes Y | ${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;25.0.2"
"platforms;android-25" "platform-tools"  
RUN cordova telemetry off  
  
# Install Gradle  
RUN wget https://services.gradle.org/distributions/gradle-4.3.1-bin.zip && \  
mkdir /opt/gradle && \  
unzip -d /opt/gradle gradle-4.3.1-bin.zip && \  
export PATH=$PATH:/opt/gradle/gradle-4.3.1/bin  
  
# Install docker-gc (garbage collector)  
RUN apt-get update  
RUN apt-get install git devscripts debhelper build-essential dh-make -y  
RUN git clone https://github.com/spotify/docker-gc.git /root/docker-gc  
RUN cd /root/docker-gc && debuild -us -uc -b  
RUN dpkg -i /root/docker-gc_0.1.0_all.deb  
  
# Install docker-compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
WORKDIR Sources  
EXPOSE 8100 35729  
CMD ["ionic", "serve"]  

