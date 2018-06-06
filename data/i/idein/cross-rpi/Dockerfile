FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
sudo git wget curl \  
gcc g++ cmake autoconf automake libtool build-essential pkg-config \  
gperf bison flex texinfo bzip2 xz-utils help2man gawk make libncurses5-dev \  
python python-dev python-pip \  
python3 python3-dev python3-pip \  
htop apt-utils locales ca-certificates \  
&& apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
WORKDIR /tmp  
RUN curl -sLO http://crosstool-ng.org/download/crosstool-ng/crosstool-
ng-1.23.0.tar.xz \  
&& tar xvJf crosstool-ng-1.23.0.tar.xz \  
&& cd crosstool-ng-1.23.0 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf crosstool-ng-1.23.0 crosstool-ng-1.23.0.tar.xz  
  
# add idein user  
RUN useradd -m idein \  
&& echo idein:idein | chpasswd \  
&& adduser idein sudo \  
&& echo 'idein ALL=NOPASSWD: ALL' >> /etc/sudoers.d/idein  
  
USER idein  
WORKDIR /home/idein  
ENV HOME /home/idein  
  
# set locale  
RUN sudo sed 's/.*en_US.UTF-8/en_US.UTF-8/' -i /etc/locale.gen  
RUN sudo locale-gen  
RUN sudo update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV PATH /home/idein/.local/bin:$PATH  
CMD ["/bin/bash"]  
  
RUN mkdir armv6-rpi-linux-gnueabihf \  
&& cd armv6-rpi-linux-gnueabihf \  
&& ct-ng armv6-rpi-linux-gnueabi \  
&& sed 's/^CT_ARCH_FLOAT_AUTO/# CT_ARCH_FLOAT_AUTO/' -i .config \  
&& sed 's/^# CT_ARCH_FLOAT_HW is not set/CT_ARCH_FLOAT_HW=y/' -i .config \  
&& sed 's/^CT_ARCH_FLOAT="auto"/CT_ARCH_FLOAT="hard"/' -i .config \  
&& echo 'CT_ARCH_ARM_TUPLE_USE_EABIHF=y' >> .config \  
&& sed 's/^# CT_CC_GCC_LIBGOMP is not set/CT_CC_GCC_LIBGOMP=y/' -i .config \  
&& sed 's/CT_LOG_PROGRESS_BAR/# CT_LOG_PROGRESS_BAR/' -i .config \  
&& ct-ng build \  
&& cd .. \  
&& rm -rf armv6-rpi-linux-gnueabihf  
ENV PATH $HOME/x-tools/armv6-rpi-linux-gnueabihf/bin:$PATH  
  
# cross compilation with rust  
ENV CC_arm_unknown_linux_gnueabihf armv6-rpi-linux-gnueabihf-gcc  
  

