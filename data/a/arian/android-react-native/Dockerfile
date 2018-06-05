FROM openjdk:8  
# nodejs, zip, to unzip things  
RUN apt-get update && \  
apt-get -y install zip expect && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
# Install 32bit support for Android SDK  
RUN dpkg --add-architecture i386 && \  
apt-get update -q && \  
apt-get install -qy --no-install-recommends libstdc++6:i386 libgcc1:i386
zlib1g:i386 libncurses5:i386  
  
# install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
ENV GRADLE_VERSION 3.3  
ENV GRADLE_SDK_URL
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
RUN curl -sSL "${GRADLE_SDK_URL}" -o gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d /usr/local \  
&& rm -rf gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_HOME /usr/local/gradle-${GRADLE_VERSION}  
ENV PATH ${GRADLE_HOME}/bin:$PATH  
  
# copy tools folder  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# android sdk tools  
RUN cd /opt \  
&& wget -q https://dl.google.com/android/repository/tools_r25.2.3-linux.zip -O
tools.zip \  
&& mkdir -p ${ANDROID_HOME} \  
&& unzip tools.zip -d ${ANDROID_HOME} \  
&& rm -f tools.zip  
  
RUN mkdir $ANDROID_HOME/licenses  
RUN echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
$ANDROID_HOME/licenses/android-sdk-license  
RUN echo 84831b9409646a918e30573bab4c9c91346d8abd >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
# sdk  
RUN opt/tools/android-accept-licenses.sh "$ANDROID_HOME/tools/bin/sdkmanager \  
tools \  
\"platform-tools\" \  
\"build-tools;23.0.1\" \  
\"build-tools;23.0.3\" \  
\"build-tools;25.0.1\" \  
\"build-tools;25.0.2\" \  
\"platforms;android-23\" \  
\"platforms;android-25\" \  
\"extras;android;m2repository\" \  
\"extras;google;m2repository\" \  
\"extras;google;google_play_services\"" \  
&& $ANDROID_HOME/tools/bin/sdkmanager --update  
  
WORKDIR /root  

