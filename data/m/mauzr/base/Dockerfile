FROM ubuntu:latest  
  
LABEL org.label-schema.schema-version=1.0 \  
org.label-schema.name=mauzr/base:esp \  
org.label-schema.vcs-url=https://github.com/mauzr/base \  
org.label-schema.build-date=${BUILD_DATE}  
  
RUN apt update && apt install -y autoconf automake bash bison bzip2 flex g++ \  
gawk gcc git gperf help2man libexpat-dev libtool libtool-bin make ncurses-dev
\  
python python-dev python-serial sed texinfo unrar-free unzip wget python3-pip
\  
wget  
  
ENV IDF_PATH=/opt/esp-idf \  
PATH=/opt/xtensa-esp32-elf/bin:/opt/esp-open-sdk/xtensa-lx106-elf/bin:${PATH}
\  
CT_ALLOW_BUILD_AS_ROOT_SURE=1  
  
RUN cd /opt && \  
wget -qO- https://dl.espressif.com/dl/xtensa-esp32-elf-
linux64-1.22.0-61-gab8375a-5.2.0.tar.gz | tar xz  
  
RUN cd /opt && \  
git clone --recursive https://github.com/espressif/esp-idf.git && \  
cd esp-idf && git checkout 2c95a77cf93781f296883d5dbafcdc18e4389656 && \  
git submodule update \--recursive  
  
RUN cd /opt && \  
git clone --recursive https://github.com/pfalcon/esp-open-sdk.git && \  
cd esp-open-sdk && make STANDALONE=y  

