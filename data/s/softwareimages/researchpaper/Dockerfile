# This is the base image for the containers that run zeromq  
FROM maven:3.5-jdk-8-alpine  
MAINTAINER Okusanya David (coolodavid@gmail.com)  
  
RUN apk --update --no-cache --virtual build.deps add \  
make \  
cmake \  
gcc \  
g++ \  
libstdc++ \  
libgcc \  
asciidoc \  
xmlto \  
bash-completion \  
bash-doc \  
python2 \  
util-linux-dev \  
libsodium-dev \  
automake \  
autoconf \  
ca-certificates \  
openssl \  
zeromq \  
zeromq-dev \  
git \  
libtool \  
pkgconfig \  
wget \  
nano  
  
ENV GRADLE_VERSION=4.0  
ENV GRADLE_HOME=/opt/gradle  
  
WORKDIR /tmp  
  
RUN wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& mkdir /opt \  
&& unzip -q gradle-${GRADLE_VERSION}-bin.zip -d /opt \  
&& ln -s /opt/gradle-${GRADLE_VERSION} /opt/gradle \  
&& rm -f gradle-${GRADLE_VERSION}-bin.zip  
  
ENV PATH $PATH:${GRADLE_HOME}/bin  
  
WORKDIR /home  
  
RUN git clone https://github.com/zeromq/jzmq.git \  
&& cd jzmq/jzmq-jni \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
COPY jzmq_prompt.sh /etc/profile  
  
CMD ["/bin/bash", "--login"]  

