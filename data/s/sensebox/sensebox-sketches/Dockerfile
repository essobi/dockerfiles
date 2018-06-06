FROM debian:9.4-slim as builder  
  
ENV IDE_VERSION=1.8.5 \  
SENSEBOXCORE_VERSION=1.0.4 \  
ARDUINO_SAMD_VERSION=1.6.18 \  
ARDUINO_AVR_VERSION=1.6.21 \  
SENSEBOXCORE_URL=https://github.com/watterott/senseBox-
MCU/raw/master/package_sensebox_index.json \  
SENSEBOX_LIBRARIES_URL=https://github.com/sensebox/resources/raw/master/libraries/senseBox_Libraries.zip
\  
SENSEBOX_LIBRARY_URL=https://github.com/sensebox/senseBox_library/archive/master.zip
\  
PATH=$PATH:/arduino-ide  
  
RUN apt-get update && apt-get install -y xz-utils unzip wget \  
&& wget http://downloads.arduino.cc/arduino-$IDE_VERSION-linux64.tar.xz \  
&& tar xf arduino-$IDE_VERSION-linux64.tar.xz \  
&& mv arduino-$IDE_VERSION /arduino-ide \  
&& wget -O senseBox_Libraries.zip $SENSEBOX_LIBRARIES_URL \  
&& wget -O senseBox_Library.zip $SENSEBOX_LIBRARY_URL \  
&& unzip senseBox_Libraries.zip -d /arduino-ide \  
&& unzip senseBox_Library.zip -d /arduino-ide/libraries \  
&& arduino --pref boardsmanager.additional.urls=$SENSEBOXCORE_URL \--install-
boards sensebox:samd:$SENSEBOXCORE_VERSION \  
&& arduino --install-boards arduino:samd:$ARDUINO_SAMD_VERSION \  
&& arduino --install-boards arduino:avr:$ARDUINO_AVR_VERSION \  
&& mkdir -p /arduino-ide/build-cache \  
&& mv /root/.arduino15/packages /arduino-ide/packages \  
&& apt-get purge -y xz-utils unzip wget \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf arduino-$IDE_VERSION-linux64.tar.xz senseBox_Libraries.zip
senseBox_Library.zip /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& bash -c 'rm -rf /arduino-
ide/{java,lib,reference,examples,arduino,install.sh,revisions.txt,uninstall.sh}'
\  
&& find /arduino-ide -type d -name "examples" -exec rm -rf \;  
  
FROM node:8-slim  
  
WORKDIR /app  
  
ENV NODE_ENV=production  
  
COPY package.json /app  
COPY yarn.lock /app  
  
RUN yarn install --pure-lockfile --production  
  
COPY src /app/src  
COPY \--from=builder /arduino-ide /app/src/arduino-ide  
  
CMD ["yarn","start"]  

