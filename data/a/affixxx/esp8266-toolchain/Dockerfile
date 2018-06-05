FROM ubuntu:latest  
MAINTAINER Keiran 'Affix' Smith <opensource@keiran.scot>  
  
RUN apt-get update  
RUN apt-get -y install apt-utils  
RUN apt-get -y install git autoconf build-essential gperf bison flex texinfo \  
libtool libtool-bin unzip libncurses5-dev wget gawk libc6-dev python-serial \  
libexpat-dev  
  
RUN adduser toolchain --disabled-password  
RUN mkdir -p /opt/Espressif  
RUN chown -R toolchain:toolchain /opt/Espressif  
RUN mkdir /build  
RUN chown toolchain:toolchain /build  
  
USER toolchain  
  
WORKDIR /opt/Espressif  
  
RUN git clone -b lx106 git://github.com/jcmvbkbc/crosstool-NG.git  
  
WORKDIR /opt/Espressif/crosstool-NG  
RUN ./bootstrap && ./configure --prefix=`pwd` && make && make install  
RUN ./ct-ng xtensa-lx106-elf  
RUN ./ct-ng build  
  
USER root  
  
USER toolchain  
WORKDIR /opt/Espressif  
RUN wget -O esp_iot_sdk_v0.9.3_14_11_21.zip
https://github.com/esp8266/esp8266-wiki/raw/master/sdk/esp_iot_sdk_v0.9.3_14_11_21.zip  
RUN wget -O esp_iot_sdk_v0.9.3_14_11_21_patch1.zip
https://github.com/esp8266/esp8266-wiki/raw/master/sdk/esp_iot_sdk_v0.9.3_14_11_21_patch1.zip  
RUN unzip esp_iot_sdk_v0.9.3_14_11_21.zip  
RUN unzip -o esp_iot_sdk_v0.9.3_14_11_21_patch1.zip  
RUN mv esp_iot_sdk_v0.9.3 ESP8266_SDK  
RUN mv License ESP8266_SDK/  
  
WORKDIR /opt/Espressif/ESP8266_SDK  
RUN sed -i -e 's/xt-ar/xtensa-lx106-elf-ar/' -e 's/xt-xcc/xtensa-lx106-elf-
gcc/' -e 's/xt-objcopy/xtensa-lx106-elf-objcopy/' Makefile  
RUN mv examples/IoT_Demo .  
  
RUN wget -O lib/libc.a
https://github.com/esp8266/esp8266-wiki/raw/master/libs/libc.a  
RUN wget -O lib/libhal.a
https://github.com/esp8266/esp8266-wiki/raw/master/libs/libhal.a  
RUN wget -O include.tgz
https://github.com/esp8266/esp8266-wiki/raw/master/include.tgz  
RUN tar -xvzf include.tgz  
  
USER root  
WORKDIR /opt/Espressif  
RUN git clone https://github.com/tommie/esptool-ck.git  
WORKDIR /opt/Espressif/esptool-ck  
RUN make  
RUN cp esptool /bin/esptool  
  
WORKDIR /opt/Espressif  
USER toolchain  
RUN git clone https://github.com/themadinventor/esptool esptool-py  
USER root  
RUN ln -s /opt/Espressif/esptool-py/esptool.py crosstool-NG/builds/xtensa-
lx106-elf/bin/  
RUN chmod 777 /opt/Espressif/esptool-py/esptool.py  
USER toolchain  
  
ENV PATH=/opt/Espressif/crosstool-NG/builds/xtensa-lx106-elf/bin:$PATH  
ENV HOME=/home/toolchain  
WORKDIR /build  
CMD make  

