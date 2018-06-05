FROM andresousa/jdk:1.0  
LABEL Maintainer="André Sousa <andrefelicio@live.com>"  
  
ENV ANDROID_SDK_HOME=/opt/android-sdk-linux  
ENV ANDROID_SDK_ROOT=/opt/android-sdk-linux  
ENV ANDROID_HOME=/opt/android-sdk-linux  
ENV ANDROID_SDK=/opt/android-sdk-linux  
  
  
RUN dpkg --add-architecture i386 && apt-get update -yqq && apt-get install -y
\  
expect \  
libc6:i386 \  
libgcc1:i386 \  
libncurses5:i386 \  
libstdc++6:i386 \  
zlib1g:i386 \  
vim \  
&& apt-get clean  
  
# Setup  
RUN mkdir /temp && mkdir /opt/tools && mkdir /opt/licenses  
  
RUN groupadd android && useradd -d /opt/android-sdk-linux -g android android  
  
WORKDIR /temp  
  
RUN git clone https://github.com/andrefelicio/docker.git && \  
mv docker/android/licenses /opt && \  
mv docker/android/tools /opt && \  
rm -rf /temp  
  
WORKDIR /opt/android-sdk-linux  
  
RUN chmod -R 777 /opt/tools  
  
RUN /opt/tools/entrypoint.sh built-in  
  

