FROM ubuntu:14.04.3  
MAINTAINER Todd Sampson "toddsampson+docker@gmail.com"  
# IMPORTANT: Update these values to your primary computer user id and group id  
# On OSX use `id -u` and `id -g` to find the correct values  
# Will be used to allow access to gui components  
ENV uid 1000  
ENV gid 1000  
# Update apt and install a few needed packages  
RUN sudo apt-get update && sudo apt-get install -y wget unzip libxtst6
libXrender1 \  
libXi6 lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6 git subversion
mercurial \  
vim ant usbutils cmake && \  
apt-get clean && apt-get purge  
  
# (NOTE: Not using KVM since Project Tango doesn't have an emulator)  
# sudo apt-get install -y qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils  
# adduser android libvirtd && adduser android kvm  
# Create android user directory and empty .bashrc file  
RUN mkdir -p /home/android && touch /home/android/.bashrc  
  
# Install Oracle JVM (Don't use OpenJVM with Android Studio)  
RUN mkdir -p /usr/lib/jvm && cd /usr/lib/jvm && \  
wget -c --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.tar.gz && \  
tar -xzvf jdk-8u60-linux-x64.tar.gz && \  
rm -f jdk-8u60-linux-x64.tar.gz  
  
# Install Android Studio and Android SDK  
RUN mkdir -p /usr/lib/android-studio && cd /usr/lib/android-studio && \  
wget -c https://dl.google.com/dl/android/studio/ide-zips/1.4.0.10/android-
studio-ide-141.2288178-linux.zip && \  
unzip android-studio-ide-141.2288178-linux.zip -d /usr/lib && \  
rm -f android-studio-ide-141.2288178-linux.zip  
# TODO: Install more default sdk packages?  
# Add Google Vendor ID to UDEV Rules  
RUN echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="18d1", MODE="0666",
GROUP="plugdev"' | sudo tee -a /etc/udev/rules.d/51-android.rules && \  
sudo chmod a+r /etc/udev/rules.d/51-android.rules  
  
# Setup android user, permissions and paths  
RUN export uid=${uid} gid=${gid} && \  
echo "android:x:${uid}:${gid}:android,,,:/home/android:/bin/bash" >>
/etc/passwd && \  
echo "android:x:${uid}:" >> /etc/group && \  
echo "android ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/android && \  
chmod 0440 /etc/sudoers.d/android && \  
chown ${uid}:${gid} -R /home/android && \  
printf "export JDK_HOME=/usr/lib/jvm/jdk1.8.0_60\nexport
JAVA_HOME=/usr/lib/jvm/jdk1.8.0_60 \nexport
PATH=$PATH:/usr/lib/jvm/jdk1.8.0_60/bin:/usr/lib/android-
studio/bin:/home/android/Android/android-ndk-r10e \n" | tee -a ~/.bashrc
/home/android/.bashrc > /dev/null && \  
sudo -s source ~/.bashrc  
USER android  
ENV HOME /home/android  
  
# Install Android NDK  
RUN mkdir -p /home/android/Android && cd /home/android/Android && \  
wget -c http://dl.google.com/android/ndk/android-ndk-r10e-linux-x86_64.bin &&
\  
chmod a+x android-ndk-r10e-linux-x86_64.bin && \  
./android-ndk-r10e-linux-x86_64.bin && \  
rm -f android-ndk-r10e-linux-x86_64.bin  
  
# Add Project Tango C, Java and Unity Example Code and SDK files under /srv  
RUN sudo chmod 777 /srv && cd /srv && mkdir -p ~/.ssh && \  
printf "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config && \  
git clone https://github.com/googlesamples/tango-examples-c.git && \  
git clone https://github.com/googlesamples/tango-examples-java.git && \  
git clone https://github.com/googlesamples/tango-examples-unity.git && \  
mkdir project-tango-sdk-files && cd project-tango-sdk-files && \  
wget https://developers.google.com/project-
tango/downloads/TangoSDK_Yamabe_C.zip && \  
wget https://developers.google.com/project-
tango/downloads/TangoSDK_Yamabe_Java.jar && \  
wget https://developers.google.com/project-
tango/downloads/TangoSDK_Yamabe_Unity.unitypackage && \  
wget https://developers.google.com/project-
tango/downloads/TangoUX_Yamabe_Java.aar  
  
CMD bash  

