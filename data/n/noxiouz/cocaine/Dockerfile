FROM ubuntu:trusty  
  
MAINTAINER Anton Tiurin "noxouz@yandex.ru"  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -qq update  
RUN apt-get -qq install build-essential devscripts equivs git-core  
  
# Fetch the latest codebase  
RUN git clone https://github.com/3Hren/cocaine-core --recursive -b v0.12.8
building/cocaine-core  
RUN git clone https://github.com/3Hren/blackhole --recursive -b develop
building/blackhole  
RUN git clone https://github.com/3Hren/cocaine-plugins --recursive -b v0.12.8
building/cocaine-plugins  
  
RUN cd building/blackhole && \  
yes | mk-build-deps -ir  
  
RUN cd building/blackhole && \  
yes | debuild -e CC -e CXX -uc -us -j$(cat /proc/cpuinfo | fgrep -c processor)
&& \  
debi  
  
# Install build dependencies  
RUN cd building/cocaine-core && \  
yes | mk-build-deps -ir  
  
# Build and install  
RUN cd building/cocaine-core && \  
debuild -e CC -e CXX -uc -us -j$(cat /proc/cpuinfo | fgrep -c processor) && \  
debi  
  
# Build and install node plugin  
RUN cd building/cocaine-plugins && \  
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCACHE=OFF -DIPVS=OFF -DDOCKER=OFF
-DURLFETCH=OFF -DELASTICSEARCH=OFF -DCHRONO=OFF -DGRAPHITE=OFF -DUNICORN=OFF
&& \  
make -j$(cat /proc/cpuinfo | fgrep -c processor) && make install  
  
# Cleanup  
RUN apt-get -qq autoremove --purge && \  
apt-get -qq purge build-essential devscripts equivs git-core && \  
rm -rf building  
  
RUN apt-get -qq install python-pip && pip install cocaine cocaine-tools  
  
ADD ./cocaine-runtime.conf /etc/cocaine/cocaine-runtime.conf  
  
# Setup runtime environment  
RUN mkdir -p /var/run/cocaine  
  
CMD ["cocaine-runtime", "-c", "/etc/cocaine/cocaine-runtime.conf"]  

