FROM centos:7.3.1611  
RUN yum install epel-release -y  
ENV PATH /opt/samtools/bin:$PATH  
RUN yum group install "Development Tools" -y && \  
yum install wget \  
openssl-devel \  
which \  
git \  
bzip2-devel* \  
xz-devel \  
python \  
zlib \  
lbzip2 \  
zlib-devel \  
libcurl \  
ncurses \  
ncurses-devel \  
libcurl-devel -y  
RUN cd /root && \  
git clone git://github.com/GregoryFaust/samblaster.git && \  
cd samblaster && \  
make && \  
cp samblaster /usr/local/bin  
RUN cd /root && \  
wget -c
https://github.com/biod/sambamba/releases/download/v0.6.6/sambamba_v0.6.6_linux.tar.bz2
&& \  
tar -xf sambamba_v0.6.6_linux.tar.bz2 && \  
mv sambamba_v0.6.6 /usr/bin/sambamba  
RUN cd /root && \  
wget -c
https://github.com/samtools/samtools/releases/download/1.8/samtools-1.8.tar.bz2
-O /root/samtools-1.8.tar.bz2 && \  
tar -xf samtools-1.8.tar.bz2 && \  
cd samtools-1.8 && \  
./configure --prefix=/opt/samtools && \  
make && \  
make install  
RUN cd /root && \  
git clone \--recursive https://github.com/arq5x/lumpy-sv.git && \  
cd lumpy-sv && \  
make && \  
cp bin/* /usr/local/bin  
ENV URL http://files.happy366.cn/files/docker/  
RUN wget -c $URL/testdoc.sh -O /usr/bin/testdoc.sh && \  
wget -c $URL/rundoc.sh -O /usr/bin/rundoc.sh && \  
chmod +x /usr/bin/rundoc.sh && \  
chmod +x /usr/bin/testdoc.sh  
  

