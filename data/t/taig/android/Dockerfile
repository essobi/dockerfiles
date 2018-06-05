FROM taig/scala:1.0.9  
MAINTAINER Niklas Klein "mail@taig.io"  
ENV ANDROID_SDK 25.2.3  
ENV ANDROID_BUILD_TOOLS 25.0.2  
ENV ANDROID_PLATFORM 25  
ENV HELLO_SCALA cdb89331fa8bc80013136fe7731adbf5d73f1b63  
  
WORKDIR /root/  
  
RUN apt-get install -y --no-install-recommends \  
unzip \  
wget  
RUN apt-get clean  
  
# Install Android SDK  
WORKDIR /root/android-sdk/  
RUN wget -q --output-document=android-tools.zip
https://dl.google.com/android/repository/tools_r$ANDROID_SDK-linux.zip  
RUN unzip -q ./android-tools.zip  
RUN rm -f ./android-tools.zip  
ENV ANDROID_HOME /root/android-sdk/  
ENV PATH $PATH:$ANDROID_HOME/tools/:$ANDROID_HOME/platform-tools/  
  
# Install major Android SDK components  
RUN echo y | android update sdk --no-ui --all --filter platform-tools  
RUN echo y | android update sdk --no-ui --all --filter build-
tools-$ANDROID_BUILD_TOOLS  
RUN echo y | android update sdk --no-ui --all --filter
android-$ANDROID_PLATFORM  
RUN echo y | android update sdk --no-ui --all --filter "extra-
android-m2repository,extra-android-support,extra-google-
google_play_services,extra-google-m2repository"  
  
# Install and test a sample project to cache the major dependencies  
WORKDIR /root/  
RUN wget https://github.com/taig/hello-scala/archive/$HELLO_SCALA.zip  
RUN unzip ./$HELLO_SCALA.zip  
RUN cd ./hello-scala-$HELLO_SCALA && sbt test  
RUN rm -r ./$HELLO_SCALA.zip ./hello-scala-$HELLO_SCALA

