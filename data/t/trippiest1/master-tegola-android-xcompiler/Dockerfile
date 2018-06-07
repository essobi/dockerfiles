FROM openjdk:8-jdk  
MAINTAINER Steven Contreras <steven@terranodo.io>  
  
#bootstrap build-environment  
RUN apt-get update  
#RUN apt-get install -y --no-install-recommends build-essential unzip wget
zlib1g-dev git  
#set up python - only if we want more recent version  
#ARG PYTHON_VERSION=3.6.5  
#ENV PYTHON_VERSION ${PYTHON_VERSION}  
#ARG PYTHON_NAME=Python-${PYTHON_VERSION}  
#RUN wget --no-check-certificate
https://www.python.org/ftp/python/${PYTHON_VERSION}/${PYTHON_NAME}.tgz  
#RUN mkdir -p /tmp  
#RUN tar -xzf ${PYTHON_NAME}.tgz -C /tmp  
#WORKDIR /tmp/${PYTHON_NAME}  
#ENV PYTHON_HOME /opt/${PYTHON_NAME}  
#RUN mkdir -p ${PYTHON_HOME}  
#RUN ./configure --prefix=${PYTHON_HOME}  
#RUN make && make install  
#RUN rm -rf /tmp/${PYTHON_NAME}  
#ENV PATH ${PATH}:${PYTHON_HOME}  
#RUN python --version  
RUN apt-get install -y --no-install-recommends unzip wget git  
  
#set up/get desired SDK version if does not exist locally  
ENV ANDROID_HOME /opt/android-sdk  
ENV PATH ${PATH}:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:${PATH}:${ANDROID_HOME}/tools  
WORKDIR /opt  
RUN \  
if [ ! -d ${ANDROID_HOME} ] ; then \  
mkdir -p ${ANDROID_HOME} \  
&& mkdir -p ~/.android \  
&& touch ~/.android/repositories.cfg \  
&& cd ${ANDROID_HOME} \  
&& wget --output-document=sdk-tools.zip
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip \  
&& unzip sdk-tools.zip \  
&& rm -f sdk-tools.zip \  
&& echo y | sdkmanager "build-tools;27.0.3" \  
&& echo y | sdkmanager "platforms;android-26" \  
&& echo y | sdkmanager "platform-tools" \  
; \  
fi  
  
#set up/get desired standalone NDK version if does not exist locally  
ENV ANDROID_STANDALONE_NDK_HOME /opt/android-standalone-ndk  
RUN mkdir -p ${ANDROID_STANDALONE_NDK_HOME}  
WORKDIR ${ANDROID_STANDALONE_NDK_HOME}  
#note:  
# we must use ndk version<=r15c, as deprecated-headers are required and this
option is no longer supported w/ version>r15c  
ARG ANDROID_NDK_VERSION=r15c  
ENV ANDROID_NDK_VERSION ${ANDROID_NDK_VERSION}  
ENV ANDROID_STANDALONE_NDK
${ANDROID_STANDALONE_NDK_HOME}/${ANDROID_NDK_VERSION}  
RUN \  
if [ ! -d ${ANDROID_STANDALONE_NDK} ] ; then \  
wget --output-document=android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip
https://dl.google.com/android/repository/android-
ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip \  
&& unzip android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip \  
&& rm -f android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip \  
&& mv android-ndk-${ANDROID_NDK_VERSION} ${ANDROID_NDK_VERSION} \  
; \  
fi  
RUN ls -F ${ANDROID_STANDALONE_NDK}  
  
#now build standalone NDK toolchains (using deprecated-headers) for each
target ABI desired (e.g. arm/api-16, arm64/api-21, x86/api-16, and
x86_64/api-21)  
ARG ANDROID_STANDALONE_NDK_TOOLCHAIN_HOME=/opt/android-standalone-ndk-
toolchain/deprecated-headers  
RUN mkdir -p ${ANDROID_STANDALONE_NDK_TOOLCHAIN_HOME}  
ENV MY_ANDROID_NDK_STANDALONE_TOOLCHAIN_HOME
${ANDROID_STANDALONE_NDK_TOOLCHAIN_HOME}/${ANDROID_NDK_VERSION}  
WORKDIR ${ANDROID_STANDALONE_NDK}/build/tools  
RUN pwd  
RUN ls  
  
#... for arm/api-16  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH=arm  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__API=16  
ARG
NDK_STANDALONE_TOOLCHAIN_TARGET=${MY_ANDROID_NDK_STANDALONE_TOOLCHAIN_HOME}/api-${NDK_STANDALONE_TOOLCHAIN_TARGET__API}/${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH}  
RUN mkdir -p ${NDK_STANDALONE_TOOLCHAIN_TARGET}  
RUN python make_standalone_toolchain.py \  
\--arch ${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH} \  
\--api ${NDK_STANDALONE_TOOLCHAIN_TARGET__API} \  
\--deprecated-headers \  
\--install-dir ${NDK_STANDALONE_TOOLCHAIN_TARGET} \  
\--force  
RUN ls ${NDK_STANDALONE_TOOLCHAIN_TARGET}/bin  
  
#...for x86/api-16  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH=x86  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__API=16  
ARG
NDK_STANDALONE_TOOLCHAIN_TARGET=${MY_ANDROID_NDK_STANDALONE_TOOLCHAIN_HOME}/api-${NDK_STANDALONE_TOOLCHAIN_TARGET__API}/${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH}  
RUN mkdir -p ${NDK_STANDALONE_TOOLCHAIN_TARGET}  
RUN python make_standalone_toolchain.py \  
\--arch ${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH} \  
\--api ${NDK_STANDALONE_TOOLCHAIN_TARGET__API} \  
\--deprecated-headers \  
\--install-dir ${NDK_STANDALONE_TOOLCHAIN_TARGET} \  
\--force  
RUN ls ${NDK_STANDALONE_TOOLCHAIN_TARGET}/bin  
  
#...for arm64/api-21  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH=arm64  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__API=21  
ARG
NDK_STANDALONE_TOOLCHAIN_TARGET=${MY_ANDROID_NDK_STANDALONE_TOOLCHAIN_HOME}/api-${NDK_STANDALONE_TOOLCHAIN_TARGET__API}/${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH}  
RUN mkdir -p ${NDK_STANDALONE_TOOLCHAIN_TARGET}  
RUN python make_standalone_toolchain.py \  
\--arch ${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH} \  
\--api ${NDK_STANDALONE_TOOLCHAIN_TARGET__API} \  
\--deprecated-headers \  
\--install-dir ${NDK_STANDALONE_TOOLCHAIN_TARGET} \  
\--force  
RUN ls ${NDK_STANDALONE_TOOLCHAIN_TARGET}/bin  
  
#...for arm64/api-21  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH=x86_64  
ARG NDK_STANDALONE_TOOLCHAIN_TARGET__API=21  
ARG
NDK_STANDALONE_TOOLCHAIN_TARGET=${MY_ANDROID_NDK_STANDALONE_TOOLCHAIN_HOME}/api-${NDK_STANDALONE_TOOLCHAIN_TARGET__API}/${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH}  
RUN mkdir -p ${NDK_STANDALONE_TOOLCHAIN_TARGET}  
RUN python make_standalone_toolchain.py \  
\--arch ${NDK_STANDALONE_TOOLCHAIN_TARGET__ARCH} \  
\--api ${NDK_STANDALONE_TOOLCHAIN_TARGET__API} \  
\--deprecated-headers \  
\--install-dir ${NDK_STANDALONE_TOOLCHAIN_TARGET} \  
\--force  
RUN ls ${NDK_STANDALONE_TOOLCHAIN_TARGET}/bin  
  
#set up/get golang  
ARG GOLANG_HOME=/opt/golang  
RUN mkdir -p ${GOLANG_HOME}  
WORKDIR ${GOLANG_HOME}  
ENV GOROOT ${GOLANG_HOME}/go  
ENV GOLANG_VERSION 1.9  
RUN \  
if [ ! -d ${GOROOT} ] ; then \  
wget --output-document=go${GOLANG_VERSION}.linux-amd64.tar.gz
https://dl.google.com/go/go${GOLANG_VERSION}.linux-amd64.tar.gz \  
&& tar -xzf go${GOLANG_VERSION}.linux-amd64.tar.gz \  
&& rm -f go${GOLANG_VERSION}.linux-amd64.tar.gz \  
; \  
fi  
ENV PATH ${PATH}:${GOROOT}/bin  
RUN go version  
  
#set up golang-workspace  
ENV GOPATH /usr/golang-workspace  
RUN mkdir -p ${GOPATH}  
ENV PATH ${PATH}:${GOPATH}/bin  
  
  
  
  
#set up gomobile pkg  
# note:  
# as of commit 6b7c05d452e752950c01b773790ee69db01e7e44
(https://github.com/golang/mobile/commit/6b7c05d452e752950c01b773790ee69db01e7e44)  
# "gomobile init" will no longer create pkg_${GOOS}_${GOARCH} directories! so
we MUST manually build and use gomobile commit just before  
# the above commit (the prior commit is
598bfe4b20d39a660581f014b68e60c5ad425336)  
#RUN go get golang.org/x/mobile/cmd/gomobile  
RUN git clone https://github.com/golang/mobile.git
${GOPATH}/src/golang.org/x/mobile  
WORKDIR ${GOPATH}/src/golang.org/x/mobile  
RUN git reset --hard 598bfe4b20d39a660581f014b68e60c5ad425336  
WORKDIR ${GOPATH}  
RUN go build golang.org/x/mobile/cmd/gomobile  
RUN go install golang.org/x/mobile/cmd/gomobile  
RUN gomobile version  
RUN gomobile init -ndk ${ANDROID_STANDALONE_NDK}  
RUN ls -F ${GOPATH}/pkg/gomobile  

