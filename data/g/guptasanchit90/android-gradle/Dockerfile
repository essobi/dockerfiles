FROM centos  
  
MAINTAINER Sanchit Gupta <gupta.sanchit90@outlook.com>  
  
# Install Development Tools  
RUN yum -y groupinstall "Development Tools"  
  
# yum update  
RUN yum -y update  
  
# Install java (OpenJDK)  
RUN yum -y install java-1.8.0-openjdk-devel  
  
# Install Expect  
RUN yum -y install expect  
  
# Install 32bit Library  
RUN yum -y install glibc.i686  
RUN yum -y install libstdc++.i686  
RUN yum -y install glibc-devel.i686  
RUN yum -y install zlib-devel.i686  
RUN yum -y install ncurses-devel.i686  
RUN yum -y install libX11-devel.i686  
RUN yum -y install libXrender.i686  
  
# Download and unzip Android SDK  
RUN cd /usr/local/ && curl -L -O http://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz && tar xf android-sdk_r24.4.1-linux.tgz  
  
# Install Android tools  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--force -a --filter tools  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--force -a --filter platform-tools  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--force -a --filter build-tools-24.0.3  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--force -a --filter android-24  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--force -a --filter android-15  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--force -a --filter extra  
  
# Download and unzip Gradle  
RUN cd /usr/local/ && curl -L -O
http://services.gradle.org/distributions/gradle-2.14.1-all.zip && unzip -o
gradle-2.14.1-all.zip  
  
# Set Environment variables  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV GRADLE_HOME /usr/local/gradle-2.14.1  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk  
  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Removed downloaded setups  
RUN rm -rf /usr/local/android-sdk_r24.4.1-linux.tgz  
RUN rm -rf /usr/local/gradle-2.14.1-all.zip  
RUN yum clean all  

