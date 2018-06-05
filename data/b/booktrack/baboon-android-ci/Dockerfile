FROM circleci/android:api-25-alpha  
  
ENV JVM_OPTS -Xmx3200m  
ENV ANDROID_NDK /opt/android/sdk/ndk-bundle  
  
# install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& sudo apt-get install -y nodejs  
  
# install git lfs  
RUN sudo curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | sudo -E bash - \  
&& sudo apt-get install git-lfs  
  
# install ndk bundle  
RUN cd home/circleci && curl -L -o ndk.zip
https://dl.google.com/android/repository/android-ndk-r14b-linux-x86_64.zip \  
&& unzip -o -q ndk.zip \  
&& mv android-ndk-r14b /opt/android/sdk/ndk-bundle  
  
# install rust  
RUN cd home/circleci \  
&& curl https://sh.rustup.rs -sSf | sh -s -- -y  

