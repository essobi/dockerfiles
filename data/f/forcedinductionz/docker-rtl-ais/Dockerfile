FROM linarotechnologies/minideb:stretch  
  
ENV VER=${VER:-master} \  
REPO=https://github.com/dgiardini/rtl-ais.git \  
APP=/usr/src/app \  
GIT_SSL_NO_VERIFY=true  
  
WORKDIR $APP  
RUN install_packages git wget rtl-sdr librtlsdr-dev gnuais gnuaisgui make
build-essential pkg-config libusb-1.0-0-dev gnuradio gr-osmosdr \  
&& git clone -b $VER $REPO $APP \  
&& make  
  
ENV VER=arm_memory \  
REPO=https://github.com/asdil12/kalibrate-rtl.git \  
APP=/usr/src/kal-rtl \  
GIT_SSL_NO_VERIFY=true  
RUN install_packages libtool autoconf automake libfftw3-dev \  
&& git clone -b $VER $REPO $APP \  
&& cd $APP \  
&& ./bootstrap \  
&& ./configure \  
&& make \  
&& make install  
  
EXPOSE 10110/udp  
  
CMD $APP/rtl_ais -n  

