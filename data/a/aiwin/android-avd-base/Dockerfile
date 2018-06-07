FROM aiwin/android-base  
  
LABEL maintainer="javier.boo@aiwin.es"  
  
# ADB and terminal ports of AVD  
EXPOSE 5554 5555  
ENV SHELL /bin/bash  
ENV ANDROID_AVD_NAME docker-avd  
ENV USER_HOME_DIR /root  
  
RUN apt-get --quiet update --yes  
RUN apt-get --quiet install --yes --no-install-recommends lib32stdc++6 lib32z1
libqt5widgets5 libqt5svg5 file socat supervisor && \  
apt-get --quiet clean --yes && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN $ANDROID_SDK_HOME/tools/bin/sdkmanager "system-
images;android-${ANDROID_TARGET_SDK};google_apis;arm64-v8a" && \  
yes | $ANDROID_SDK_HOME/tools/bin/sdkmanager --licenses && \  
$ANDROID_SDK_HOME/tools/bin/sdkmanager --update && \  
$ANDROID_SDK_HOME/tools/bin/sdkmanager "system-
images;android-${ANDROID_TARGET_SDK};google_apis;arm64-v8a" && \  
echo no | $ANDROID_SDK_HOME/tools/bin/avdmanager create avd -f -n
${ANDROID_AVD_NAME} -k "system-
images;android-${ANDROID_TARGET_SDK};google_apis;arm64-v8a" \--abi
google_apis/arm64-v8a  
  
RUN mkdir -p $USER_HOME_DIR/scripts/android  
  
COPY stop-emulators.sh $USER_HOME_DIR/scripts/android/stop-emulators.sh  
COPY wait-for-emulator.sh $USER_HOME_DIR/scripts/android/wait-for-emulator.sh  
COPY prepare-emulator.sh $USER_HOME_DIR/scripts/android/prepare-emulator.sh  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY socat.sh /usr/local/bin/socat.sh  
  
RUN mkdir -p /var/log/supervisor && \  
chmod +x /usr/local/bin/socat.sh && \  
chmod +x $HOME/scripts/android/stop-emulators.sh && \  
chmod +x $HOME/scripts/android/wait-for-emulator.sh && \  
chmod +x $HOME/scripts/android/prepare-emulator.sh  
  
CMD /usr/bin/supervisord  

