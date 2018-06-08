FROM debian:latest  
  
ENV ANDROID_HOME=/opt/android/sdk/  
ENV ANDROID_NDK_ROOT=/opt/android-ndk-r16b/  
ENV ANDROID_NDK_HOST=linux-x86_64  
ENV ANDROID_NDK_TOOLCHAIN_PREFIX=arm-linux-androideabi  
ENV ANDROID_NDK_TOOLCHAIN_VERSION=4.9  
ENV ANDROID_NDK_TOOLS_PREFIX=arm-linux-androideabi  
ENV ANDROID_SDK_ROOT=/opt/android/sdk/  
ENV BUILDTOOLS_REVISION=25.0.3  
ADD qt-install.qs /  
  
RUN apt-get update  
  
RUN apt-get install -y \  
wget \  
curl \  
unzip \  
git \  
g++ \  
make \  
&& apt-get clean  
  
# Abhängigkeiten für QT-Installer  
RUN apt-get install -y \  
libgl1-mesa-glx \  
libglib2.0-0 \  
&& apt-get clean  
  
# Abhängigkeiten für QT-Komponenten  
RUN apt-get install -y \  
libfontconfig1 \  
libdbus-1-3 \  
libx11-xcb1 \  
libnss3-dev \  
libasound2-dev \  
libxcomposite1 \  
libxrandr2 \  
libxcursor-dev \  
libegl1-mesa-dev \  
libxi-dev \  
libxss-dev \  
libxtst6 \  
libgl1-mesa-dev \  
default-jdk \  
&& apt-get clean  
  
# Download/Install Android-NDK  
RUN curl -LS https://dl.google.com/android/repository/android-
ndk-r16b-linux-x86_64.zip -o android-ndk.zip \  
&& unzip -q android-ndk.zip -d /opt/ \  
&& rm android-ndk.zip  
  
# Download/Install Android-SDK  
RUN curl -LS https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip -o android-tools.zip \  
&& mkdir -p /opt/android/sdk/ \  
&& unzip -q android-tools.zip -d /opt/android/sdk/ \  
&& rm android-tools.zip \  
&& cd /opt/android/sdk/tools/bin && yes | ./sdkmanager --licenses \  
&& ./sdkmanager "platform-tools" "platforms;android-25" "build-tools;25.0.3" \  
&& yes | ./sdkmanager --licenses  
  
# Abhängigkeiten für QT-Installer  
RUN apt-get install -y \  
libgl1-mesa-glx \  
libglib2.0-0 \  
&& apt-get clean  
  
# Download && Install Qt  
RUN curl -LS http://download.qt.io/official_releases/qt/5.9/5.9.3/qt-
opensource-linux-x64-5.9.3.run -o qt-install.run \  
&& chmod +x qt-install.run \  
&& ./qt-install.run --script qt-install.qs --platform minimal -v \  
&& rm qt-install.run  
  
ENV PATH="/opt/Qt/5.9.3/android_armv7/bin:${PATH}"  
CMD ["/bin/bash"]  

