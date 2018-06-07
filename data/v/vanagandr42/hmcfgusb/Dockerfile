FROM lsiobase/alpine:80  
# Package version  
ARG HMCFGUSB_VER=0.103  
  
# Install build packages  
RUN apk add \--no-cache \--virtual=build-dependencies \  
build-base \  
libusb-dev \  
  
# Install runtime packages  
&& apk add \--no-cache \  
libusb \  
  
# Install app  
&& wget
http://git.zerfleddert.de/hmcfgusb/releases/hmcfgusb-$HMCFGUSB_VER.tar.gz -P
/tmp \  
&& tar -xzf /tmp/hmcfgusb-$HMCFGUSB_VER.tar.gz -C /app \  
&& ln -s /app/hmcfgusb-$HMCFGUSB_VER /app/hmcfgusb \  
&& cd /app/hmcfgusb-$HMCFGUSB_VER \  
&& make \  
  
# Cleanup  
&& apk del \--purge build-dependencies \  
&& rm *.h *.o *.c *.d \  
&& rm /tmp/hmcfgusb-$HMCFGUSB_VER.tar.gz  
  
# Add local files  
COPY rootfs/ /  
  
WORKDIR /app/hmcfgusb  
  
EXPOSE 1234  

