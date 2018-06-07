FROM ubuntu:16.04  
MAINTAINER xirax (bad-hombres)  
  
# Install Dependencies  
WORKDIR /root/src  
RUN apt-get update -y  
RUN apt-get -y install wget \  
git \  
build-essential \  
libssl-dev \  
libgmp-dev \  
libpcap-dev \  
pkg-config \  
libbz2-dev\  
cmake \  
bison \  
flex \  
libicu-dev \  
sudo  
  
# Install REXGEN  
RUN git clone \--recursive https://github.com/teeshop/rexgen.git  
WORKDIR /root/src/rexgen  
RUN ./install.sh  
RUN ldconfig  
  
WORKDIR /root/src  
RUN git clone https://github.com/magnumripper/JohnTheRipper.git -b bleeding-
jumbo john  
  
WORKDIR /root/src/john/src  
RUN ./configure && make -s clean && make -sj4  
  
WORKDIR /root/src/john/run  
RUN git clone https://github.com/danielmiessler/SecLists.git && mv
SecLists/Passwords ./wordlists && rm -rf SecLists  
  
COPY entrypoint.sh .  
ENTRYPOINT ["./entrypoint.sh"]  
  

