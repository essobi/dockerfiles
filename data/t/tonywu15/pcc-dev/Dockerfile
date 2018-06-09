FROM ubuntu:trusty  
MAINTAINER Tony Wu "tonywu15@gmail.com"  
# Create User  
RUN useradd --create-home -s /bin/bash dev  
RUN adduser dev sudo  
  
# Enable sudo without password  
RUN sed -i.bkp -e \  
's/%sudo\s\\+ALL=(ALL\\(:ALL\\)\?)\s\\+ALL/%sudo ALL=NOPASSWD:ALL/g' \  
/etc/sudoers  
  
RUN apt-get update && apt-get install -y \  
sudo \  
autoconf \  
automake \  
autotools-dev \  
curl libmpc-dev \  
libmpfr-dev \  
libgmp-dev \  
gawk \  
build-essential \  
bison \  
flex \  
texinfo \  
gperf \  
git  
  
RUN mkdir /opt/riscv32i && chown dev /opt/riscv32i  
RUN git clone https://github.com/riscv/riscv-gnu-toolchain riscv-gnu-
toolchain-rv32i  
RUN cd riscv-gnu-toolchain-rv32i && git checkout 34db4e0 && mkdir build && cd
build && ../configure --with-xlen=32 --with-arch=I --prefix=/opt/riscv32i
--disable-float --disable-atomic && make -j$(nproc)  
RUN rm -rf riscv-gnu-toolchain-rv32i  
  
USER dev  
WORKDIR /home/dev  
  
ENV PATH=$PATH:/opt/riscv32i/bin  
  
ENTRYPOINT /bin/bash  

