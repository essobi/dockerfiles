FROM simonallier/sosie-exp  
MAINTAINER simon.allier@gmail.com  
  
RUN sudo apt-get update && sudo apt-get install -y libswt-gtk-3-java lib32z1
lib32ncurses5 lib32stdc++6 qemu-kvm  
  
# Main Android SDK  
RUN wget -qO- "http://dl.google.com/android/android-sdk_r24-linux.tgz" | tar
-zxv -C /root/  
  
# Other tools and resources of Android SDK  
ENV ANDROID_HOME /root/android-sdk-linux  
RUN echo "export ANDROID_HOME=$ANDROID_HOME" >> /root/.bashrc  
ENV HOME /root  
RUN echo "export HOME=$HOME" >> /root/.bashrc  
  
ENV ANDROID_EMULATOR_FORCE_32BIT true  
RUN echo "export ANDROID_EMULATOR_FORCE_32BIT=true" >> /root/.bashrc  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN echo "export PATH=$PATH" >> /root/.bashrc  
RUN echo y | android update sdk --all --filter platform-tools,build-
tools-21.1.1,android-21 --no-ui --force  
RUN echo y | android update sdk --all --filter sys-img-x86-android-21 --no-ui
--force  
RUN echo Y | android update sdk --all --filter addon-google_apis-
google-21,sys-img-x86-addon-google_apis-google-21 --no-ui --force  
  
RUN echo no | android create avd -n myandroid -t "Google Inc.:Google APIs:21"
-b google_apis/x86

