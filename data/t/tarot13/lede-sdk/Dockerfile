FROM ubuntu:zesty  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
ENV SDK_URL "https://downloads.lede-
project.org/releases/17.01.4/targets/bcm53xx/generic/lede-
sdk-17.01.4-bcm53xx_gcc-5.4.0_musl-1.1.16_eabi.Linux-x86_64.tar.xz"  
ENV SDK_SUFFIX ".tar.xz"  
RUN apt-get update && \  
apt-get install -y software-properties-common wget xz-utils build-essential
ccache git libncurses5-dev libncursesw5-dev gawk && \  
cd ~ && \  
wget $SDK_URL && \  
tar xf "$(basename $SDK_URL)" && \  
rm "$(basename $SDK_URL)" && \  
mv "$(basename $SDK_URL $SDK_SUFFIX)" sdk && \  
cd sdk && \  
./scripts/feeds update -a && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root/sdk  
  
ENTRYPOINT ["/bin/bash"]

