FROM ubuntu:trusty  
MAINTAINER TIMWI <contact@timwi.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
NODE_VERSION=4.7.2 \  
NPM_VERSION=2.15.11 \  
IONIC_VERSION=1.6.5 \  
CORDOVA_VERSION=5.3.1 \  
GULP_VERSION=3.9.1 \  
SONAR_SCANNER=3.0.0.702-linux \  
SONAR_URL=http://localhost:9000  
# Set the timezone  
RUN sudo echo "Europe/Paris" > /etc/timezone  
RUN sudo dpkg-reconfigure -f noninteractive tzdata  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools:/opt/sonar-scanner/bin:/opt/nsis-2.46/bin  
  
# Install basics  
RUN apt-get update && \  
apt-get install -y git wget curl unzip ruby bzip2 libfontconfig && \  
curl --retry 3 -SLO
"http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
&& \  
tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 && \  
rm "node-v$NODE_VERSION-linux-x64.tar.gz"  
  
# NSIS  
# ttf-mscorefonts-installer has often problems with font download. Checking
this first and exit on fail  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/sources.list && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections && \  
apt-get update && apt-get install -y --no-install-recommends ttf-mscorefonts-
installer 2>&1 | tee fontinstall.log |cat && \  
if grep -q Traceback fontinstall.log ; then echo "Error on font download!" ;
exit 1; fi && rm fontinstall.log  
  
# NSIS - Basic things  
RUN set -e && \  
apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
fontconfig \  
git \  
lib32z1 \  
openssh-client \  
software-properties-common \  
wget \  
lib32ncurses5 \  
&& rm -rf /var/lib/apt/lists/*  
  
# NSIS  
RUN set -e && \  
dpkg --add-architecture i386 && \  
apt-get update && apt-get install -y --no-install-recommends \  
libstdc++6:i386 \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD nsis-2.46-linux32-bin.tar.bz2 /opt  
  
RUN npm install --global npm@"$NPM_VERSION"  
RUN npm install --global gulp@"$GULP_VERSION" \--allow-root  
RUN npm install --global cordova@"$CORDOVA_VERSION" \--allow-root  
RUN npm install --global ionic@"$IONIC_VERSION" \--allow-root  
  
RUN npm cache clear  
  
RUN gem install sass  
  
RUN mkdir myApp  
  
#ANDROID  
#JAVA  
# install python-software-properties (so you can do add-apt-repository)  
RUN apt-get update && apt-get install -y -q python-software-properties
software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get -y install oracle-java8-installer  
  
#ANDROID STUFF  
RUN echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y --force-yes expect ant wget libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Android SDK  
RUN cd /opt && \  
wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
tar xzf android-sdk.tgz && \  
rm -f android-sdk.tgz && \  
chown -R root. /opt  
  
# Install Android SDK elements  
COPY tools /opt/tools  
  
RUN chmod +x /opt/tools/android-accept-licenses.sh  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --all --no-
ui --filter \  
platform-tools,android-22,build-tools-22.0.1,sys-img-
armeabi-v7a-google_apis-23,extra-android-support,extra-
android-m2repository,extra-google-m2repository"]  
RUN sed -i 's/localhost/0.0.0.0/'
/usr/local/lib/node_modules/ionic/lib/ionic/serve.js  
RUN ln -sf /opt/android-sdk-linux/build-tools/22.0.1/zipalign /usr/bin/  
  
# Patch to cordova plugin add  
# https://github.com/apache/cordova-
lib/commit/9d75a4257c02bd033589362ba4c3d175b28fca45  
RUN sed -i".bak" '/ bumpCounter/d'
/usr/local/lib/node_modules/cordova/node_modules/cordova-
lib/src/plugman/registry/registry.js  
  
# Install Google Chrome Browser  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get update -qqy && \  
apt-get -qqy install google-chrome-stable && \  
rm /etc/apt/sources.list.d/google-chrome.list && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Sonarqube scanner  
RUN wget -q https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/sonar-scanner-cli-${SONAR_SCANNER}.zip && \  
unzip sonar-scanner-cli-${SONAR_SCANNER}.zip -d /opt && \  
rm sonar-scanner-cli-${SONAR_SCANNER}.zip && \  
mv /opt/sonar-scanner-${SONAR_SCANNER} /opt/sonar-scanner && \  
sed -i "s|#sonar.host.url=\\(.*\\)$|sonar.host.url=$SONAR_URL|" /opt/sonar-
scanner/conf/sonar-scanner.properties  
  
# Add datalait user  
RUN useradd -ms /bin/bash datalait && \  
chown -Rf datalait myApp && \  
echo 'PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools:/opt/sonar-scanner/bin\n' > /home/datalait/.bashrc && \  
echo 'export PATH' >> /home/datalait/.bashrc && \  
chmod +x ${ANDROID_HOME}/tools/android && \  
chmod +x /opt/sonar-scanner/bin/sonar-scanner  
  
USER datalait  
  
WORKDIR /home/datalait  
EXPOSE 8100  
ENTRYPOINT bash  

