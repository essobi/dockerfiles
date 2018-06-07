FROM ubuntu:14.04.4  
MAINTAINER NUCAR  
  
# HSA software stack  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget git cmake clang-3.5
python  
RUN wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo
apt-key add -  
RUN sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/
trusty main > /etc/apt/sources.list.d/rocm.list'  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y amdcloc hcc_hsail
libelf1 bsdmainutils  
  
ENV HSA_RUNTIME_PATH /opt/rocm/hsa  
ENV PATH /opt/rocm/cloc/bin:$PATH  
ENV PATH /opt/rocm/hcc/bin:$PATH  
  
# OpenCL software stack  
RUN apt-get install -y fglrx-core  
COPY ./AMDAPPSDK-3.0 /opt/AMDAPPSDK-3.0  
  
ENV AMDAPPSDKROOT /opt/AMDAPPSDK-3.0  
ENV PATH /opt/$(AMDAPPSDKROOT)/bin:$PATH  
  
# Temporary fix, will be removed when repo is updated  
RUN cd /tmp  
RUN wget
https://github.com/HSAFoundation/CLOC/raw/master/packages/ubuntu/amdcloc_1.0-11_amd64.deb  
RUN wget
https://github.com/HSAFoundation/CLOC/raw/master/packages/ubuntu/hlc_3.2-4_amd64.deb  
RUN dpkg -i *.deb  

