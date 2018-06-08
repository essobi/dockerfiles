FROM menglj/docker-imrad-dev:android-release  
  
ENV ANDROID_NDK_HOME /opt/android-ndk  
  
# ------------------------------------------------------  
# --- Android NDK  
# download  
RUN mkdir /opt/android-ndk-tmp  
RUN cd /opt/android-ndk-tmp && wget -q
http://dl.google.com/android/ndk/android-ndk-r10e-linux-x86_64.bin  
# uncompress  
RUN cd /opt/android-ndk-tmp && chmod a+x ./android-ndk-r10e-linux-x86_64.bin  
RUN cd /opt/android-ndk-tmp && ./android-ndk-r10e-linux-x86_64.bin  
# move to it's final location  
RUN cd /opt/android-ndk-tmp && cp -r ./android-ndk-r10e /opt/android-ndk  
# remove temp dir  
RUN rm -rf /opt/android-ndk-tmp  
# add to PATH  
ENV PATH ${PATH}:${ANDROID_NDK_HOME}  

