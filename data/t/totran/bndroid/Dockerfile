FROM totran/android:latest  
  
MAINTAINER Jingkai Tang <jingkaitang@gmail.com>  
  
# add sys img to docker  
ENV ANDROID_TARGET android-23  
ENV ANDROID_ABI armeabi-v7a  
ENV ANDROID_SYS_IMAGE sys-img-$ANDROID_ABI-$ANDROID_TARGET  
RUN echo y | android update sdk --no-ui --all --filter "$ANDROID_SYS_IMAGE"  
  
# create avd  
RUN echo no | android create avd -f -n test -t "$ANDROID_TARGET" -b
"$ANDROID_ABI" -d 9 -s WXGA720 -c 200M  
  
ADD android-wait-for-emulator /usr/local/bin/  
ADD start-emulator /usr/local/bin/  
  

