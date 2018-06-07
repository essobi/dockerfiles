FROM ubuntu:16.04  
MAINTAINER Fer Uria <fauria@gmail.com>  
LABEL Description="NodeMCU firmware generator. Customize and build a firmware
with a single command. See README.md for more information." \  
License="MIT License" \  
Usage="docker run --rm REPLACE_THIS fauria/nodemcu" \  
Version="1.0"  
  
RUN apt-get -y update  
RUN apt-get -y install git wget zip unzip build-essential autoconf gperf flex
bison texinfo help2man gawk libtool-bin libtool libncurses5-dev python python-
dev python-pip  
RUN pip install --upgrade pip  
RUN pip install pyserial  
  
RUN useradd --create-home -s /bin/bash nodemcu  
USER nodemcu  
ENV HOME=/home/nodemcu  
WORKDIR ${HOME}  
RUN git clone \--recursive https://github.com/pfalcon/esp-open-sdk  
RUN git clone https://github.com/nodemcu/nodemcu-firmware.git  
  
WORKDIR ${HOME}/esp-open-sdk  
RUN make STANDALONE=y  
  
ENV PATH="${HOME}/esp-open-sdk/xtensa-lx106-elf/bin/:${PATH}"  
WORKDIR ${HOME}/nodemcu-firmware  
RUN make  
  
USER root  
RUN ln -s /home/nodemcu/nodemcu-firmware/bin /firmware  
COPY run-nodemcu.pl /  
RUN chmod +x /run-nodemcu.pl  
  
VOLUME /firmware  
  
CMD ["/run-nodemcu.pl"]7

