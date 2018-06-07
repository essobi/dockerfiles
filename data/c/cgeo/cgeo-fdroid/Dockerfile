# Compiles and installs an fdroid environment  
FROM ubuntu:artful  
MAINTAINER mathieu Alorent <cgeo@kumy.net>  
  
# Enable i386 arch (for android SDK)  
RUN dpkg --add-architecture i386  
  
# Required dependencies  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -q -y \  
curl \  
git \  
libffi-dev \  
libjpeg62-dev \  
libssl-dev \  
libstdc++6:i386 \  
openjdk-8-jdk \  
python3-dev \  
python3-pip \  
python3-pyasn1 \  
wget \  
zlib1g-dev \  
software-properties-common \  
zlib1g:i386 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install pillow  
  
# Android SDK  
ENV ANDROID_HOME /sdk  
RUN wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz  
RUN tar xvzf android-sdk_r24.4.1-linux.tgz && mv android-sdk-linux
$ANDROID_HOME && rm android-sdk_r24.4.1-linux.tgz  
  
# Add android tools and platform tools to PATH  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
  
# Install latest android tools and system image.  
RUN echo "y" | android update sdk --all --no-ui --force --filter build-
tools-24.0.1,platform-tools,tools  
  
# Install f-droid server  
RUN add-apt-repository -y ppa:guardianproject/ppa \  
&& apt-get update \  
&& apt-get install -y \  
fdroidserver \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config.py /apk/  
ADD http://www.cgeo.org/images/logo.png /apk/  
COPY run.sh /usr/local/bin/  
COPY fdroid-update.sh /usr/local/bin/  
COPY apksigner /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh /usr/local/bin/fdroid-update.sh  
COPY metadata /apk/metadata  
  
# Install jenkins slave client  
ADD http://ci.cgeo.org/jnlpJars/slave.jar /apk  
  
VOLUME ["/apk/repo"]  
  
WORKDIR /apk  
  
CMD ["/usr/local/bin/run.sh"]  
  

