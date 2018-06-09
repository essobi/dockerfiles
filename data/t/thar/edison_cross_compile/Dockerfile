FROM resin/intel-edison-python:latest  
RUN apt-get update && apt-get --yes --force-yes install git cmake wget bzip2  
RUN wget http://iotdk.intel.com/sdk/3.5/edison/iot-devkit-toolchain-
linux-32bit-edison-20160606.sh && chmod +x iot-devkit-toolchain-linux-32bit-
edison-20160606.sh && ./iot-devkit-toolchain-linux-32bit-edison-20160606.sh -y  
RUN wget -O boost_1_56_0.tar.gz
"https://downloads.sourceforge.net/project/boost/boost/1.56.0/boost_1_56_0.tar.gz?r=http%3A%2F%2Fwww.boost.org%2Fusers%2Fhistory%2Fversion_1_56_0.html&ts=1494251445&use_mirror=freefr"
&& tar -zxvf boost_1_56_0.tar.gz && rm boost_1_56_0.tar.gz && mv boost_1_56_0
/opt/poky-edison/1.7.3/sysroots/core2-32-poky-linux/  
COPY compileBoostPython.sh /opt/poky-edison/1.7.3/sysroots/core2-32-poky-
linux/  
RUN chroot /opt/poky-edison/1.7.3/sysroots/core2-32-poky-linux/
./compileBoostPython.sh  
RUN rm -rf /opt/poky-edison/1.7.3/sysroots/core2-32-poky-linux/boost_1_56_0 &&
rm /opt/poky-edison/1.7.3/sysroots/core2-32-poky-linux/compileBoostPython.sh

