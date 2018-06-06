FROM debian:wheezy  
  
MAINTAINER firemilesxu@gmail.com firemiles  
  
# ---  
# crosstool-NG  
# see https://github.com/crosstool-ng/crosstool-ng.git  
# ---  
# install package  
RUN apt-get update && apt-get install -y \  
git \  
sudo \  
autoconf \  
build-essential \  
gperf \  
bison \  
flex \  
texinfo \  
libtool \  
libncurses5-dev \  
wget \  
gawk \  
libc6-dev \  
help2man \  
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# add user firemiles  
RUN mkdir /home/firemiles \  
&& groupadd -r firemiles -g 1000 \  
&& useradd -u 1000 -r -g firemiles -d /home/firemiles -s /bin/bash -c "Docker
image user" firemiles \  
&& chown -R firemiles:firemiles /home/firemiles \  
&& adduser firemiles sudo \  
&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
WORKDIR /home/firemiles  
USER firemiles  
  
# build and install  
RUN git clone -b 1.22 https://github.com/crosstool-ng/crosstool-ng.git \  
&& cd /home/firemiles/crosstool-ng \  
&& ./bootstrap \  
&& ./configure \  
&& make \  
&& sudo make install \  
&& rm -rf ../crosstool-ng/  
  
# work like command  
ENTRYPOINT ["ct-ng"]  
  
# add commit label for microbadger  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license=MIT \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/work-on-docker/crosstool-ng"  
  

