FROM frolvlad/alpine-glibc  
  
ENV ARDUINO_IDE_VERSION 1.8.3  
  
RUN apk --no-cache add wget ca-certificates && \  
mkdir /opt && \  
wget -q -O-
https://downloads.arduino.cc/arduino-${ARDUINO_IDE_VERSION}-linux64.tar.xz |
tar xJ -C /opt && \  
ln -s /opt/arduino-${ARDUINO_IDE_VERSION}/arduino /usr/local/bin/ && \  
ln -s /opt/arduino-${ARDUINO_IDE_VERSION}/arduino-builder /usr/local/bin/ && \  
ln -s /opt/arduino-${ARDUINO_IDE_VERSION} /opt/arduino  
  
ENTRYPOINT [ "arduino-builder" ]  

