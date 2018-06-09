FROM thenewvu/oracle-jdk8  
MAINTAINER Vu Le "thenewvu@gmail.com"  
# install android-studio and needed packages  
RUN sudo apt-add-repository ppa:paolorotolo/android-studio && \  
sudo dpkg --add-architecture i386 && \  
sudo apt-get update && \  
sudo apt-get install -y --no-install-recommends libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
lib32z1-dev \  
libxext-dev \  
libxrender-dev \  
libxtst-dev \  
libgtk2.0-0 \  
android-studio \  
git \  
build-essential  
  
# add android-sdk tools to $PATH  
ENV PATH $PATH:/data/android-sdk/platform-tools:/data/android-sdk/tools  
# clean up  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
# start android-studio at container start up  
ENTRYPOINT ["/opt/android-studio/bin/studio.sh"]  

