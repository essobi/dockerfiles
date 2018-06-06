FROM chuross/android-java7  
  
MAINTAINER chuross <azarasi.mo.mo@gmail.com>  
  
ARG TARGET_API="android-23"  
ARG STORAGE_SIZE="128M"  
ARG SKIN="QVGA"  
ENV ANDROID_TARGET_API $TARGET_API  
ENV ANDROID_EMULATOR_STORAGE_SIZE $STORAGE_SIZE  
ENV ANDROID_EMULATOR_SKIN $SKIN  
ENV ANDROID_EMULATOR_MEMORY 1024  
ENV ANDROID_EMULATOR_NAME "armeabi-v7a-${ANDROID_TARGET_API}"  
ENV ANDROID_EMULATOR_COMPONENTS $ANDROID_TARGET_API,sys-
img-${ANDROID_EMULATOR_NAME}  
ENV ANDROID_EMULATOR_PATH $ANDROID_HOME/../emulators  
ENV ANDROID_EMULATOR_PORT 5554  
ENV ADB_PORT 5555  
EXPOSE $ADB_PORT  
EXPOSE $ANDROID_EMULATOR_PORT  
  
RUN apt-get install -y socat net-tools  
  
WORKDIR $ANDROID_HOME  
RUN rm -rf platforms/$ANDROID_TARGET_API  
RUN echo y | android update sdk --no-ui --all --filter
"${ANDROID_EMULATOR_COMPONENTS}"  
  
RUN android list targets \  
&& echo no | android create avd --force \  
-n $ANDROID_EMULATOR_NAME \  
-t $ANDROID_TARGET_API \  
-c $ANDROID_EMULATOR_STORAGE_SIZE \  
-s $ANDROID_EMULATOR_SKIN \  
&& echo hw.ramSize=$ANDROID_EMULATOR_MEMORY >>
~/.android/avd/${ANDROID_EMULATOR_NAME}.ini  
  
WORKDIR /usr/local  
  
COPY emulator.sh /usr/local  
RUN chmod +x emulator.sh  
  
CMD ["sh", "emulator.sh"]  

