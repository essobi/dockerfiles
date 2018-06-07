FROM base/archlinux  
MAINTAINER David Ferreira <davidferreira.fz@gmail.com>  
  
LABEL com.dukitan.tag="asdk26_ionic320"  
LABEL com.dukitan.release-date="2018-05-17"  
LABEL com.dukitan.asdk_version="26"  
LABEL com.dukitan.nodejs="8.8.1"  
LABEL com.dukitan.ionic_version="3.20.0"  
LABEL com.dukitan.cordova_version="7.1.0"  
  
ENV ANDROID_BUILD_TOOLS_VERSION 27.0.3  
ENV ANDROID_SDK_HOME /opt/android-sdk  
ENV ANDROID_SDK_ROOT /opt/android-sdk  
ENV ANDROID_HOME /opt/android-sdk  
ENV ANDROID_SDK /opt/android-sdk  
ENV NPM_CONFIG_PREFIX /opt/npm/npm-global  
#ENV M2_HOME /opt/maven  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:/opt/npm/npm-
global/bin  
  
  
RUN pacman -Syu --noconfirm && \  
pacman -U http://mirror.pritunl.com/archlinux/all/icu-59.1-2 \  
http://mirror.pritunl.com/archlinux/all/http-parser-2.7.1-1 \  
http://mirror.pritunl.com/archlinux/all/nodejs-8.8.1-1 \  
http://mirror.pritunl.com/archlinux/all/lib32-zlib-1.2.11-1 --noconfirm && \  
pacman -S jdk8-openjdk fakeroot wget binutils sudo libxtst fontconfig git
freetype2 \  
libxrender lib32-glibc lib32-gcc-libs python2 make gcc npm gradle --noconfirm  
RUN useradd -m -g users -s /bin/bash user && \  
mkdir /opt/download && \  
chown user -R /opt/download && \  
mkdir /opt/npm/npm-global -p && \  
chmod 777 -R /opt/npm/npm-global && \  
mkdir /opt/maven && \  
chmod 777 -R /opt/maven  
USER user  
RUN cd /opt/download && \  
wget https://aur.archlinux.org/cgit/aur.git/snapshot/android-sdk.tar.gz && \  
tar -zxvf android-sdk.tar.gz && \  
cd android-sdk && \  
makepkg  
USER root  
RUN pacman -U /opt/download/android-sdk/android-sdk-26.1.1-1-x86_64.pkg.tar.xz
--noconfirm && \  
rm -rf /opt/download/android-sdk/ && \  
rm /opt/download/android-sdk.tar.gz  
USER user  
RUN cd /opt/download && \  
wget https://aur.archlinux.org/cgit/aur.git/snapshot/android-sdk-platform-
tools.tar.gz && \  
tar -zxvf android-sdk-platform-tools.tar.gz && \  
cd android-sdk-platform-tools && \  
makepkg  
USER root  
RUN pacman -U /opt/download/android-sdk-platform-tools/android-sdk-platform-
tools-r27.0.1-1-x86_64.pkg.tar.xz --noconfirm && \  
rm -rf /opt/download/android-sdk-platform-tools/ && \  
rm /opt/download/android-sdk-platform-tools.tar.gz  
USER user  
RUN cd /opt/download && \  
wget https://aur.archlinux.org/cgit/aur.git/snapshot/android-
platform-26.tar.gz && \  
tar -zxvf android-platform-26.tar.gz && \  
cd android-platform-26 && \  
makepkg  
USER root  
RUN pacman -U /opt/download/android-platform-26/android-
platform-26-8.0.0_r02-1-any.pkg.tar.xz --noconfirm && \  
rm -rf /opt/download/android-platform-26/ && \  
rm /opt/download/android-platform-26.tar.gz  
USER user  
RUN cd /opt/download && \  
wget https://aur.archlinux.org/cgit/aur.git/snapshot/android-sdk-build-
tools.tar.gz && \  
tar -zxvf android-sdk-build-tools.tar.gz && \  
cd android-sdk-build-tools && \  
makepkg  
USER root  
RUN pacman -U /opt/download/android-sdk-build-tools/android-sdk-build-
tools-r27.0.3-1-x86_64.pkg.tar.xz --noconfirm && \  
rm -rf /opt/download/android-sdk-build-tools/ && \  
rm /opt/download/android-sdk-build-tools.tar.gz  
RUN npm -g config set user root && \  
npm install npm@latest -g && \  
npm install -g node-gyp@3.6.2 cordova@7.1.0 ionic@3.20.0 && \  
npm install -g @ionic/app-scripts@latest && \  
cordova telemetry off && \  
ionic config set -g telemetry false && \  
npm config set offline false  
# ionic config set -g daemon.updates false && \  
# npm cache clear --force  
RUN chmod 777 /opt  
RUN pacman -Sc --noconfirm && rm -r /var/cache/pacman/pkg/*  
  
VOLUME ["/opt", "/root"]  

