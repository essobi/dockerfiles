FROM ubuntu:17.10  
ARG ESPIDF_VERSION=v3.0-rc1  
ARG TOOLCHAIN_VERSION=1.22.0-75-gbaf03c2-5.2.0  
ENV ESPIDF_VERSION ${ESPIDF_VERSION}  
ENV TOOLCHAIN_VERSION ${TOOLCHAIN_VERSION}  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gcc \  
git \  
make \  
wget \  
libncurses-dev \  
flex \  
bison \  
gperf \  
python \  
python-serial && \  
apt-get autoremove -yqq && \  
apt-get autoclean -yqq && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt && \  
mkdir -p /esp && \  
cd /esp && \  
wget --no-check-certificate https://dl.espressif.com/dl/xtensa-esp32-elf-
linux64-$TOOLCHAIN_VERSION.tar.gz && \  
tar -xzf xtensa-esp32-elf-linux64-$TOOLCHAIN_VERSION.tar.gz && \  
rm xtensa-esp32-elf-linux64-$TOOLCHAIN_VERSION.tar.gz && \  
git -c http.sslVerify=false clone --depth 1 --recursive -b $ESPIDF_VERSION
https://github.com/espressif/esp-idf.git && \  
rm -rf esp-idf/.git  
ENV PATH /esp/xtensa-esp32-elf/bin:$PATH  
ENV IDF_PATH /esp/esp-idf

