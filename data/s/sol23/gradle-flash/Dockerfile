FROM frekele/gradle:3.2.1-jdk8  
  
MAINTAINER Carsten Stender <carsten.stender@gmail.com>  
  
##=======================  
## Environment variables  
##=======================  
ENV DISPLAY :99  
ENV GRADLE_USER_HOME /gradle  
ENV GRADLE_FOLDER /gradle  
  
ENV AIR_SDK_VERSION 22.0  
ENV FLEX_SDK_NAME AirSdkCompiler-${AIR_SDK_VERSION}  
ENV FLASH_DIR /opt/flash  
ENV FLEX_HOME /opt/flash/sdk/AirSdkCompiler-${AIR_SDK_VERSION}  
ENV FLASH_PLAYER_LOCATION /usr/lib/flashplayer/flashplayerdebugger  
  
##=======================  
## Install dependencies  
##=======================  
RUN apt-get update && \  
apt-get install -y \  
curl \  
openssl \  
tar \  
bzip2 \  
unzip \  
git \  
  
# for running standalone debug flashplayer  
  
libxcursor1 \  
libnss3 \  
libgtk2.0-0 \  
xvfb &&\  
  
apt-get clean  
  
##=======================  
## Install Debug Flash player  
##=======================  
RUN mkdir -p $FLASH_DIR &&\  
cd $FLASH_DIR &&\  
curl
https://fpdownload.macromedia.com/pub/labs/flashruntimes/flashplayer/linux64/flash_player_sa_linux_debug.x86_64.tar.gz
\  
\--progress-bar \  
-o flash_player.tar.gz &&\  
tar xzf flash_player.tar.gz &&\  
rm flash_player.tar.gz &&\  
mkdir -p /usr/lib/flashplayer &&\  
mv flashplayerdebugger /usr/lib/flashplayer/flashplayerdebugger &&\  
rm -rf /usr/bin/flashplayerdebugger &&\  
ln -s /usr/lib/flashplayer/flashplayerdebugger /usr/bin/gflashplayer  
  
# ##==========================  
# ## Install AirSDK  
# ##==========================  
WORKDIR $FLEX_HOME  
RUN curl
https://airdownload.adobe.com/air/mac/download/${AIR_SDK_VERSION}/AIRSDK_Compiler.tbz2
\  
\--progress-bar \  
-o sdk.tbz2 &&\  
tar -jxf sdk.tbz2 &&\  
rm sdk.tbz2  
  
# ##==========================  
# ## Install all playerglobal.swc  
# ##==========================  
RUN cd ${FLEX_HOME}/frameworks/libs &&\  
rm -rf player &&\  
git clone https://github.com/nexussays/playerglobal.git player  
  
##==========================  
## Mount volumes  
##==========================  
RUN mkdir -p /project && mkdir -p /gradle  
VOLUME /project  
VOLUME /gradle  
  
WORKDIR /project  
  
##==========================  
## Configure entrypoint  
##==========================  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["bash"]

