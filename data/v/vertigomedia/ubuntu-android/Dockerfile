#  
# Oracle JDK 8-based Android Development Dockerfile  
#  
# Pull base image.  
FROM vertigomedia/ubuntu-jdk8  
MAINTAINER Dan Fowler <dan@logickc.com>  
  
#Let people know how this was built  
ADD Dockerfile /root/Dockerfile  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -yq libstdc++6:i386 zlib1g:i386 libncurses5:i386 --no-install-
recommends && \  
apt-get clean  
  
# Download and untar SDK  
ENV ANDROID_SDK_URL http://dl.google.com/android/android-sdk_r24.1.2-linux.tgz  
RUN curl -L "${ANDROID_SDK_URL}" | tar --no-same-owner -xz -C /usr/local  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV ANDROID_SDK /usr/local/android-sdk-linux  
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH  
  
# Install Android SDK components  
ENV ANDROID_SDK_COMPONENTS platform-tools,build-tools-21.1.2,android-21,extra-
android-m2repository,extra-google-m2repository  
RUN echo y | android update sdk --no-ui --all --filter
"${ANDROID_SDK_COMPONENTS}"  
  
# Support Gradle  
ENV TERM dumb  
ENV JAVA_OPTS -Xms256m -Xmx512m  
  
# Define default command.  
CMD ["bash"]  

