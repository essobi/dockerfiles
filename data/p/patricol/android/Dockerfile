FROM patricol/ubuntu_jdk:16.04  
USER root  
# Setup KVM  
RUN apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
usermod -aG kvm user && \  
echo "chown root:libvirtd /dev/kvm" >> /home/user/earlycommands.sh  
  
# Setup Android SDK  
RUN su user -c "umake android android-sdk /home/user/Android/Sdk --accept-
license"  
ENV ANDROID_HOME=/home/user/Android/Sdk  
ENV ANDROID_SDK_HOME=/home/user  
ENV
PATH=.:$ANDROID_HOME/emulator:$ANDROID_HOME/tools/bin:$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$PATH  
ENV SDK_VER=27  
ENV BUILD_TOOLS_MINOR_VER=0.3  
# USER user  
RUN yes | sdkmanager --licenses && \  
touch /home/user/.android/repositories.cfg && \  
sdkmanager "emulator" "platform-tools" && \  
sdkmanager "build-tools;$SDK_VER.$BUILD_TOOLS_MINOR_VER"
"platforms;android-$SDK_VER" "system-images;android-$SDK_VER;google_apis;x86"
&& \  
sdkmanager --update  
RUN echo "no" | avdmanager create avd -n default -k "system-
images;android-$SDK_VER;google_apis;x86"  
  
# Setup Android Studio  
RUN sdkmanager "extras;android;m2repository" "extras;google;m2repository"
"sources;android-$SDK_VER"  
# Things that Android Studio wants to install on first run.  
# USER root  
RUN su user -c "umake android android-studio
/home/user/.local/share/umake/android/android-studio --accept-license"  
  
# Setup shortcuts  
#COPY --chown=user:user extras/emulator.sh /home/user/#Not yet supported by
docker hub's automated builds, which use an outdated version of docker.  
COPY extras/emulator.sh /home/user/  
RUN chmod +x /home/user/emulator.sh && \  
chown -R user:user /home/user/emulator.sh  
  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
#COPY --chown=user:user extras/*.desktop
/home/user/.local/share/applications/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.desktop /home/user/.local/share/applications/  
RUN chown -R user:user /home/user/.config/ /home/user/.local/  
  
ENV GPUTOGGLE=off  
  
  
USER user

