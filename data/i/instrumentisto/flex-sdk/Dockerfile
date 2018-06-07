# https://hub.docker.com/r/frekele/gradle  
FROM frekele/gradle:3-jdk8  
  
MAINTAINER Instrumentisto Team <developer@instrumentisto.com>  
  
  
# Install Flex SDK and its dependencies  
ENV FLEX_HOME='/flex-sdk'  
RUN update-ca-certificates \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ant \  
rsync \  
bzip2 \  
\  
&& curl -fL -o /tmp/flex-sdk.tar.gz \  
http://apache.cbox.biz/flex/4.16.1/binaries/apache-flex-sdk-4.16.1-bin.tar.gz
\  
&& tar -xzf /tmp/flex-sdk.tar.gz -C /tmp \  
&& mv /tmp/apache-flex-sdk-* $FLEX_HOME \  
&& cd $FLEX_HOME \  
&& ant -f installer.xml -Dair.sdk.version=2.6 \  
-Djava.awt.headless=true \  
-Dinput.air.download=y \  
-Dinput.fontswf.download=y \  
-Dinput.flash.download=y \  
&& chown -R root:root $FLEX_HOME \  
\  
&& apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
bzip2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/*  
  
ENV PATH="$FLEX_HOME/bin:$PATH"  
# Install Flash Player and its dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libnss3 libgtk2.0-0 \  
xvfb xauth \  
\  
&& curl -fL -o /tmp/flash_player.tar.gz \  
https://fpdownload.macromedia.com/pub/flashplayer/updaters/29/flash_player_sa_linux_debug.x86_64.tar.gz
\  
&& tar -xzf /tmp/flash_player.tar.gz -C /tmp \  
&& mv /tmp/flashplayerdebugger /usr/local/bin/ \  
&& mkdir -p /usr/local/doc/flashplayerdebugger \  
&& mv /tmp/LGPL/* /usr/local/doc/flashplayerdebugger/ \  
&& chown -R root:root /usr/local/bin/flashplayerdebugger \  
/usr/local/doc/flashplayerdebugger \  
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/*  
  
# Create wrapper for xvfb-run command  
RUN echo '#!/bin/sh' >> /usr/local/bin/xvfb \  
&& echo 'num=$(echo $DISPLAY | cut -d: -f2)' >> /usr/local/bin/xvfb \  
&& echo 'args="-screen 0 $RESOLUTION -ac +extension RANDR"' \  
>> /usr/local/bin/xvfb \  
&& echo 'xvfb-run -e /dev/stderr -n $num -s "$args" "$@"' \  
>> /usr/local/bin/xvfb \  
&& chmod +x /usr/local/bin/xvfb  
  
ENV FLASH_PLAYER_EXE='/usr/local/bin/flashplayerdebugger' \  
DISPLAY=':99' \  
RESOLUTION='1024x768x24'  
# Prepare application directory  
RUN mkdir -p /app  
  
WORKDIR /app  
  
ENTRYPOINT []  

