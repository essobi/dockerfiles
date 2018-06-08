FROM plumbee/nvidia-virtualgl  
  
LABEL version="1.0"  
  
MAINTAINER Marc Peña Segarra <segarrra@gmail.com>  
  
# Tell debconf to run in non-interactive mode (but just during the image
build).  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get dist-upgrade -yf && \  
apt-get install -y \  
vim software-properties-common git && \  
add-apt-repository -y ppa:ettusresearch/uhd && \  
add-apt-repository -y ppa:myriadrf/drivers && \  
add-apt-repository -y ppa:myriadrf/gnuradio && \  
add-apt-repository -y ppa:wireshark-dev/stable && \  
apt-get update && \  
apt-get install -y \  
gnuradio gnuradio-dev \  
osmo-sdr libosmosdr-dev \  
libosmocore libosmocore-dev \  
pkg-config libusb-1.0-0-dev cmake m4 automake autotools-dev \  
cmake libboost-all-dev libcppunit-dev swig doxygen liblog4cpp5-dev python-
scipy gr-osmosdr wireshark && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
# We don't install these packages from the repos: rtl-sdr, librtlsdr-dev  
RUN git clone https://github.com/rtlsdrblog/rtl-sdr && \  
cd rtl-sdr && \  
mkdir build && \  
cd build && \  
cmake ../ -DINSTALL_UDEV_RULES=ON && \  
make && \  
make install && \  
ldconfig  
  
# This seems to be the most up to date fork  
RUN git clone https://github.com/viraptor/kalibrate-rtl && \  
cd kalibrate-rtl && \  
./bootstrap && CXXFLAGS='-W -Wall -O3' && \  
./configure && \  
make && \  
make install  
  
# Some QT-based applications need this variable set  
RUN echo export QT_X11_NO_MITSHM=1 >> /etc/bash.bashrc  
  
# Disable LUA scripts in wireshark, as we will run it as root.  
# https://ask.wireshark.org/questions/17190/running-tshark-as-a-root-dofile-
file-is-disabled-problem  
RUN sed -i -e 's/disable_lua = false/disable_lua = true/'
/usr/share/wireshark/init.lua  
  
ENTRYPOINT ["/bin/bash"]  

