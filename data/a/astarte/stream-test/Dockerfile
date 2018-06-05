FROM debian:stable as builder  
  
# Let's install dependencies  
RUN apt-get update && apt-get -qq install qt5-default qtbase5-dev
libqt5sql5-sqlite libssl-dev libmosquittopp-dev cmake git build-essential  
  
WORKDIR /build  
  
# Install Astarte Qt5 SDK  
RUN git clone https://github.com/astarte-platform/astarte-device-sdk-qt5.git
&& \  
cd astarte-device-sdk-qt5 && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr .. && \  
make && \  
make install && \  
cd -  
  
# Install Astarte Qt5 Stream Test  
RUN git clone https://github.com/astarte-platform/stream-qt5-test.git && \  
cd stream-qt5-test && \  
qmake . && \  
make && \  
cd -  
  
FROM debian:stable-slim  
  
# Install required dependencies  
RUN apt-get update && apt-get -qq install libmosquittopp1 libqt5network5
libqt5sql5-sqlite libssl1.1 ca-certificates  
  
# Add our fresh binaries  
COPY \--from=builder /usr/lib/libAstarteDeviceSDKQt5.so.0* /usr/lib/  
COPY \--from=builder /usr/bin/astarte-validate-interface /usr/bin/  
COPY \--from=builder /usr/share/hyperdrive /usr/share/hyperdrive  
COPY \--from=builder /build/stream-qt5-test/stream-qt5-test /usr/bin/  
  
# Add Interfaces  
COPY interfaces /interfaces/  
  
# Add utility scripts  
COPY docker-entrypoint.sh /usr/local/bin/  
  
WORKDIR /  
  
ENV FUNCTION=random INTERVAL=1000 SCALE=0.0001
ASTARTE_INTERFACE=org.astarteplatform.Values ASTARTE_INTERFACE_PATH=/realValue
PERSISTENCY_DIR=/persistency PAIRING_HOST=http://localhost:4003
IGNORE_SSL_ERRORS=false  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD /usr/bin/stream-qt5-test --device $DEVICE_ID \  
\--function $FUNCTION \  
\--interval $INTERVAL \  
\--scale $SCALE \  
\--interface "$ASTARTE_INTERFACE" \  
\--path "$ASTARTE_INTERFACE_PATH"  

