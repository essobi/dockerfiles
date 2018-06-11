FROM ubuntu:14.04  
MAINTAINER Raquel Pau <raquelpau@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean
true" | debconf-set-selections  
  
RUN apt-get update && \  
apt-get install -y oracle-java8-installer maven dnsutils git  
  
ADD . /usr/local/walkmod-nsq  
  
RUN mkdir /usr/local/logs  
ENV WALKMOD_NSQ_LOGS /usr/local/logs  
  
ENV WALKMOD_NSQ_HOME /usr/local/walkmod-nsq  
ENV NSQ_PROPERTIES ${WALKMOD_NSQ_HOME}/src/test/resources/nsq.properties  
  
RUN cd /usr/local/walkmod-nsq && mvn assembly:assembly  
  
# Main Android SDK  
RUN cd /opt && wget -q http://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz  
RUN cd /opt && tar xzf android-sdk_r24.4.1-linux.tgz  
RUN cd /opt && rm -f android-sdk_r24.4.1-linux.tgz  
  
ENV ANDROID_SDK_VERSION r24.4.1  
ENV ANDROID_BUILD_TOOLS_VERSION 23.0.1  
# Other tools and resources of Android SDK  
ENV ANDROID_API_LEVELS android-23  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN echo y | android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} \--no-
https  

