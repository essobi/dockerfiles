FROM ubuntu:16.04  
# Get the latest version from
https://developer.android.com/ndk/downloads/index.html  
ENV ANDROID_NDK_VERSION 16b  
  
# Get the latest version from https://developer.android.com/studio/index.html  
ENV ANDROID_SDK_TOOLS_VERSION 3859397  
ENV ANDROID_COMPONENTS_PFM platform-tools  
ENV ANDROID_COMPONENTS_SDK platforms;android-26 platforms;android-27  
ENV ANDROID_COMPONENTS_BDT build-tools;25.0.3 build-tools;26.0.1 build-
tools;27.0.3  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV ANDROID_NDK_HOME ${ANDROID_HOME}/ndk-bundle  
ENV GRADLE_FOLDER /root/.gradle  
ENV ANDROID_NDK_COMPONENTS "ndk-bundle" \  
"lldb;2.3" \  
"cmake;3.6.4111459"  
RUN apt-get update \  
&& \  
apt-get install -y --no-install-recommends \  
curl \  
wget \  
lib32stdc++6 \  
lib32z1 \  
lib32ncurses5 \  
openjdk-8-jdk \  
unzip \  
&& \  
rm -rf /var/lib/apt/lists/ \  
&& \  
apt-get clean  
  
# Install Android SDK  
RUN wget --quiet -O android-sdk.zip
https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS_VERSION}.zip \  
&& \  
unzip -q android-sdk.zip -d android-sdk-linux \  
&& \  
mv android-sdk-linux ${ANDROID_HOME} \  
&& \  
rm android-sdk.zip  
  
# Install Android tools  
RUN yes | /usr/local/android-sdk/tools/bin/sdkmanager --licenses
--include_obsolete  
RUN /usr/local/android-sdk/tools/bin/sdkmanager ${ANDROID_COMPONENTS_PFM}
${ANDROID_COMPONENTS_SDK} ${ANDROID_COMPONENTS_BDT} ${ANDROID_NDK_COMPONENTS}
\--include_obsolete  
  
# Add android commands to PATH  
ENV PATH
$PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME_NDK}  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
ENV TERM dumb  
  
# Set up Gradle  
RUN mkdir ${GRADLE_FOLDER}  
RUN echo "allprojects {\n repositories {\n mavenLocal()\n maven {\n
credentials {\n username travenUser\n password travenPassword\n\  
}\n url \"https://truevolve-traven.appspot.com\"\n }\n }\n}\n" >
${GRADLE_FOLDER}/init.gradle  
  
RUN echo
"travenUser=REPLACE_THIS_WITH_YOUR_USERNAME\ntravenPassword=REPLACE_THIS_WITH_YOUR_PASSWORD\norg.gradle.caching=true"
> ${GRADLE_FOLDER}/gradle.properties  
  
CMD /bin/bash  

