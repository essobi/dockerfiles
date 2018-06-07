FROM dyhpoon/android  
  
MAINTAINER Darren "dyhpoon@gmail.com"  
# Resources of Android SDK  
RUN echo y | android update sdk -a --no-ui --filter sys-img-
armeabi-v7a-android-23 --force  
  
# Set up and run emulator  
RUN echo no | android create avd --force -n test -c 30M -t android-23  
# Avoid emulator assumes HOME as '/'.  
ENV HOME /root  
ADD wait-for-emulator /usr/local/bin/  
ADD start-emulator /usr/local/bin/  
  
VOLUME /root/.gradle  
VOLUME /workspace  
WORKDIR /workspace

