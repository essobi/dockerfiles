FROM bdero/devkitarm-3ds  
MAINTAINER Mike Eastes "overlord@gmail.com"  
RUN apt-get update && \  
apt-get install -y build-essential zip && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
RUN git clone https://github.com/devkitPro/3ds_portlibs && \  
git clone \--recursive https://github.com/Steveice10/bannertool && \  
git clone https://github.com/profi200/Project_CTR.git  
  
WORKDIR /opt/3ds_portlibs  
RUN make zlib && \  
make install-zlib  
  
WORKDIR /opt/bannertool  
RUN make && \  
cp output/linux-x86_64/bannertool /usr/local/bin  
  
WORKDIR /opt/Project_CTR/makerom  
RUN make && \  
cp makerom /usr/local/bin  
  
WORKDIR /source  
  
CMD ["bash"]  

