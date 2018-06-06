FROM rhel6.6  
MAINTAINER Suriya Soutmun <deu@odd-e.co.th>  
  
ENV GCC_VER 4.9.2  
ADD centos.repo /etc/yum.repos.d/  
  
RUN yum install -y wget tar bzip2 gzip gcc openssh-server zlib-devel && \  
(yum groupinstall -y 'Development Tools' || \  
yum groupinstall -y 'Development Tools' || \  
yum groupinstall -y 'Development Tools') && \  
wget -O /root/gcc-${GCC_VER}.tar.bz2
https://ftp.gnu.org/gnu/gcc/gcc-${GCC_VER}/gcc-${GCC_VER}.tar.bz2 && \  
cd /root && tar xvjf gcc-${GCC_VER}.tar.bz2 && \  
cd /root/gcc-${GCC_VER} && contrib/download_prerequisites && \  
mkdir -p /root/gcc-${GCC_VER}/build && cd /root/gcc-${GCC_VER}/build && \  
../configure --prefix=/usr/local/gcc --disable-bootstrap --with-system-zlib
--enable-languages=c,c++ --build=x86_64-redhat-linux --disable-multilib && \  
make -j8 && \  
make install && \  
yum clean all && \  
rm -rf /root/* && \  
rm /usr/bin/gcc /usr/bin/g++ /usr/bin/cpp && \  
ln -s /usr/local/gcc/bin/gcc /usr/bin/ && \  
ln -s /usr/local/gcc/bin/g++ /usr/bin/ && \  
ln -s /usr/local/gcc/bin/cpp /usr/bin/ && \  
service sshd start && \  
echo 'root:$And@ais;' | chpasswd  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd","-D"]  

