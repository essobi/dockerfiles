FROM ubuntu:trusty  
MAINTAINER TIMWI <contact@timwi.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
NODE_VERSION=8.2.1 \  
SONAR_SCANNER=3.0.0.702-linux \  
SONAR_URL=http://localhost:9000 \  
DISPLAY=":1"  
# Set the timezone  
RUN sudo echo "Europe/Paris" > /etc/timezone  
RUN sudo dpkg-reconfigure -f noninteractive tzdata  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools:/opt/sonar-scanner/bin:/opt/nsis-2.46/bin:/opt/gradle-3.5/bin  
  
# Install basics  
RUN apt-get update && \  
apt-get install -y git wget curl unzip bzip2 libfontconfig build-essential
python python-dev && \  
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
  
RUN mkdir generic-user  
  
# install python-software-properties (so you can do add-apt-repository)  
RUN apt-get update && apt-get install -y -q python-software-properties
software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get -y install oracle-java8-installer  
  
#ANDROID STUFF  
COPY gradle-3.5-bin.zip /opt/gradle-3.5-bin.zip  
RUN echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y --force-yes expect ant wget libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
unzip /opt/gradle-3.5-bin.zip -d /opt  
  
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
platform-tools,android-25,build-tools-25.0.3,sys-img-
armeabi-v7a-google_apis-25,extra-android-support,extra-
android-m2repository,extra-google-m2repository"]  
RUN ln -sf /opt/android-sdk-linux/build-tools/25.0.3/zipalign /usr/bin/  
  
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
  
# Add generic-user user  
RUN useradd -ms /bin/bash generic-user && \  
chown -Rf generic-user generic-user && \  
echo 'PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools:/opt/sonar-scanner/bin\n' > /home/generic-user/.bashrc && \  
echo 'export PATH' >> /home/generic-user/.bashrc && \  
chmod +x ${ANDROID_HOME}/tools/android && \  
chmod +x /opt/sonar-scanner/bin/sonar-scanner  
  
COPY .npmrc /home/generic-user/.npmrc  
RUN chown generic-user /home/generic-user/.npmrc  
  
USER generic-user  
WORKDIR /home/generic-user  
EXPOSE 8100  
ENTRYPOINT bash  

