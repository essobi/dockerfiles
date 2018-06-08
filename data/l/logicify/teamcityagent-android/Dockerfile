FROM logicify/teamcityagent-common  
  
MAINTAINER Alexander Beskrovny <alexander.beskrvny@logicify.com>  
  
USER root  
  
ENV ANDROID_SDK_VERSION=25.1.7  
RUN yum makecache fast && yum -y update && yum install glibc.i686 zlib.i686
libstdc++.i686 ncurses-libs.i686 libgcc.i686 -y  
  
RUN cd /opt && curl -o android-sdk.zip -L
https://dl.google.com/android/repository/tools_r$ANDROID_SDK_VERSION-linux.zip  
  
RUN cd /opt && mkdir android-sdk && unzip -d ./android-sdk android-sdk.zip &&
rm -f android-sdk.zip \  
&& chmod -R +x android-sdk/tools/* && chown -R app:app ./android-sdk  
  
USER app  
  
ENV ANDROID_HOME=/opt/android-sdk  
  
ENV PATH="$PATH:/opt/android-sdk/tools:/opt/android-sdk/platform-tools"  
RUN echo y | /opt/android-sdk/tools/android update sdk --all --filter
platform-tools,build-tools-25.0.1,extra-android-m2repository --no-ui --force  
RUN echo y | /opt/android-sdk/tools/android update sdk --all --filter
sysimg-21,android-21 --no-ui --force  
RUN echo y | /opt/android-sdk/tools/android update sdk --all --filter
sysimg-25,android-25 --no-ui --force  
  
RUN cd /opt && chmod -R +x android-sdk/build-tools/*  

