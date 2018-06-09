from ubuntu:17.10  
workdir /opt  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
git build-essential \  
gcc-arm-linux-gnueabi gcc-aarch64-linux-gnu \  
python python-dev swig \  
m4 libssl-dev bison flex curl zlib1g-dev bc linux-firmware wget pkg-config
libusb-1.0-0-dev &&\  
rm -rf /var/lib/apt/lists/* && \  
wget https://chromium.googlesource.com/chromiumos/third_party/linux-
firmware/+/f151f016b4fe656399f199e28cabf8d658bcb52b/brcm/brcmfmac4356-pcie.txt?format=TEXT
-O /lib/firmware/brcm/brcmfmac4356-pcie.txt  
  
run mkdir /work  
workdir /work  

