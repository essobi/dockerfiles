FROM java:openjdk-8-jdk-alpine  
MAINTAINER FlexConstructor <flexconstructor@gmail.com>  
  
  
#==================================  
# Enveronment variables.  
#==================================  
ENV FLEX_SDK_VERSION 4.15.0  
ENV FLEX_HOME /flex-sdk/apache-flex-sdk-${FLEX_SDK_VERSION}-bin  
  
  
#=======================  
# Install dependencies.  
#=======================  
RUN apk update && apk upgrade && \  
apk add --no-cache bash \  
wget \  
apache-ant \  
rsync  
  
#==================================  
# Install FLEX SDK.  
#==================================  
RUN wget http://apache.cbox.biz/flex/4.15.0/binaries/apache-flex-
sdk-${FLEX_SDK_VERSION}-bin.tar.gz && \  
mkdir -p /flex-sdk && \  
tar zxvf apache-flex-sdk-${FLEX_SDK_VERSION}-bin.tar.gz -C /flex-sdk && \  
rm apache-flex-sdk-${FLEX_SDK_VERSION}-bin.tar.gz && \  
cd $FLEX_HOME && \  
ant -f installer.xml -Dair.sdk.version=2.6 \  
-Djava.awt.headless=true \  
-Dinput.air.download=y \  
-Dinput.fontswf.download=y \  
-Dinput.flash.download=y  
  
#==================================  
# Install default playerglobal.swc.  
#==================================  
RUN mkdir -p ${FLEX_HOME}/frameworks/libs/player/11.1 && \  
wget
http://download.macromedia.com/get/flashplayer/updaters/11/playerglobal11_1.swc
-O \  
${FLEX_HOME}/frameworks/libs/player/11.1/playerglobal.swc  
  
VOLUME ${FLEX_HOME}  
CMD ["bash"]  

