FROM ubuntu:14.04  
MAINTAINER sinkcup <sinkcup@163.com>  
  
RUN apt-get update -qq  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential ccache curl dnsutils flex gawk gettext
git liblzma-dev libncurses5-dev libssl-dev python subversion u-boot-tools
unzip wget xsltproc zlib1g-dev  
  
RUN \  
mkdir -p /root/openwrt/ && \  
cd /root/openwrt/ && \  
ip=`nslookup downloads.openwrt.io 208.67.222.222 | grep Address | tail -n 1 |
awk '{print $2}'` && \  
echo $ip && \  
curl -o hc5761-20140619.tar.gz -H 'Host: downloads.openwrt.io'
http://$ip/vendors/gee/ralink/hc5761-20140619.tar.gz && \  
tar -zxvf hc5761-20140619.tar.gz  
  
ADD . /root/openwrt/hc5761/  
  
RUN \  
cd /root/openwrt/hc5761/ && \  
./dl.sh  
  
RUN \  
cd /root/openwrt/hc5761/ && \  
make defconfig && \  
make package/network/utils/curl/compile -j V=99  
  
WORKDIR /root/openwrt/hc5761/  

