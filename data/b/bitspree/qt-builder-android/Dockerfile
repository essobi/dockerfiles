FROM bitspree/qt-builder  
  
LABEL authors="garaone@co3.de"  
  
ENV QT=5.10.0  
ENV QT_ARCH ${QT_PATH}/${QT}/android_armv7  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_SDK_ROOT ${ANDROID_HOME}  
ENV SDKMANAGER ${ANDROID_HOME}/tools/bin/sdkmanager  
ENV ANDROID_NDK_ROOT /opt/android-ndk  
ENV ANDROID_NDK_TOOLCHAIN_PREFIX arm-linux-androideabi  
ENV ANDROID_NDK_TOOLCHAIN_VERSION 4.9  
ENV ANDROID_NDK_HOST linux-x86_64  
ENV ANDROID_NDK_PLATFORM android-27  
ENV ANDROID_NDK_TOOLS_PREFIX ${ANDROID_NDK_TOOLCHAIN_PREFIX}  
ENV QMAKESPEC android-g++  
ENV
PATH=${PATH}:${QT_ARCH}/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools  
  
RUN apt-get update -q && \  
apt-get install -q -y --no-install-recommends \  
default-jdk \  
expect \  
unzip \  
&& apt-get clean \  
&& rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# START ANDROID STUFF  
RUN echo /opt/qt/${QT}/android_armv7/lib > /etc/ld.so.conf.d/qt-${QT}.conf  
  
# download & unpack android sdk  
COPY ./accept-license.sh /tmp/  
RUN mkdir -p ${ANDROID_SDK_ROOT} \  
&& cd ${ANDROID_SDK_ROOT} \  
&& curl -Lo sdk.zip 'https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip' \  
&& unzip ./sdk.zip \  
&& rm ./sdk.zip \  
&& ${SDKMANAGER} \--list \  
&& /tmp/accept-license.sh "${SDKMANAGER} \--update" \  
&& /tmp/accept-license.sh "${SDKMANAGER} platform-tools" \  
&& /tmp/accept-license.sh "${SDKMANAGER} build-tools;27.0.3" \  
&& /tmp/accept-license.sh "${SDKMANAGER} sources;android-27" \  
&& /tmp/accept-license.sh "${SDKMANAGER} extras;android;gapid;3" \  
&& /tmp/accept-license.sh "${SDKMANAGER} extras;android;m2repository" \  
&& /tmp/accept-license.sh "${SDKMANAGER} extras;google;google_play_services" \  
&& /tmp/accept-license.sh "${SDKMANAGER} extras;google;market_apk_expansion" \  
&& /tmp/accept-license.sh "${SDKMANAGER} extras;google;market_licensing" \  
&& /tmp/accept-license.sh "${SDKMANAGER} extras;google;m2repository" \  
&& /tmp/accept-license.sh "${SDKMANAGER} ${ANDROID_NDK_PLATFORM}" \  
&& /tmp/accept-license.sh "${SDKMANAGER} \--update" \  
&& ${SDKMANAGER} \--list  
  
# && echo "y" | android update sdk -u -a -t tools,platform-tools,build-
tools-21.1.2,build-tools-23.0.3,extra-android-m2repository,extra-android-
support,extra-google-google_play_services,extra-google-m2repository,extra-
google-play_apk_expansion,$ANDROID_NDK_PLATFORM \  
# download & unpack android ndk  
RUN mkdir /tmp/android \  
&& cd /tmp/android \  
&& curl -Lo ndk.zip 'https://dl.google.com/android/repository/android-
ndk-r16b-linux-x86_64.zip' \  
&& unzip ndk.zip \  
&& mv android-ndk-r16b $ANDROID_NDK_ROOT \  
&& chmod -R +rX $ANDROID_NDK_ROOT \  
&& rm -rf /tmp/android  
  
# END ANDROID STUFF  
###################  
# CLEAN UP  
RUN apt-get clean autoclean \  
&& apt-get autoremove -y  
# && rm -rf \  
# /var/lib/apt/lists/* \  
# /tmp/* \  
# /var/tmp/* \  
# /var/lib/dpkg/* \  
# /var/lib/cache/* \  
# /var/lib/log/*  
CMD ["/bin/bash"]  

