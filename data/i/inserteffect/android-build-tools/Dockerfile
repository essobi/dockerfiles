FROM openjdk:8-jdk  
MAINTAINER Philip Graf <philip.graf@insfx.com>  
  
ENV ANDROID_BUILD_TOOLS_VERSION=27.0.3  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Android SDK-tools  
ENV ANDROID_SDK_TOOLS_VERSION="3859397" \  
ANDROID_SDK_TOOLS_SHA256_SUM="444e22ce8ca0f67353bda4b85175ed3731cae3ffa695ca18119cbacef1c1bea0"
\  
ANDROID_HOME=/opt/android_sdk  
  
RUN cd /tmp \  
&& wget "https://dl.google.com/android/repository/sdk-tools-
linux-$ANDROID_SDK_TOOLS_VERSION.zip" \  
&& echo "$ANDROID_SDK_TOOLS_SHA256_SUM sdk-tools-
linux-$ANDROID_SDK_TOOLS_VERSION.zip" | sha256sum -c - \  
&& mkdir -p $ANDROID_HOME \  
&& unzip "sdk-tools-linux-$ANDROID_SDK_TOOLS_VERSION.zip" -d "$ANDROID_HOME" \  
&& rm "sdk-tools-linux-$ANDROID_SDK_TOOLS_VERSION.zip"  
  
ENV PATH="$PATH:$ANDROID_HOME/tools/bin"  
# install build-tools  
RUN yes | sdkmanager "build-tools;$ANDROID_BUILD_TOOLS_VERSION"  
RUN yes | sdkmanager "platform-tools"  
  
RUN yes | sdkmanager "extras;android;m2repository"  
RUN yes | sdkmanager "extras;google;m2repository"  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/inserteffect/docker-
android-build-tools.git"  
LABEL org.label-schema.name="Android Build Tools"  
LABEL org.label-schema.vendor="InsertEFFECT"  
LABEL org.label-schema.schema-version="1.0"  

