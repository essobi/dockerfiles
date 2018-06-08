FROM centos:6.9  
RUN yum install -y \  
git \  
wget \  
gcc gcc-c++ \  
gcc-gfortran libgfortran \  
autoconf \  
flex \  
bison byacc \  
doxygen \  
graphviz \  
ghostscript \  
python-devel \  
java-1.7.0-openjdk-devel && \  
mkdir /root/src && \  
cd /root/src && \  
wget ftp://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz && \  
mkdir autoconf && \  
tar xf autoconf-2.69.tar.gz -C autoconf --strip-components=1 && \  
cd /root/src/autoconf && \  
autoconf && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
cd /root/src && \  
wget ftp://ftp.gnu.org/gnu/automake/automake-1.15.1.tar.gz && \  
mkdir automake && \  
tar xf automake-1.15.1.tar.gz -C automake --strip-components=1 && \  
cd /root/src/automake && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
cd /root/src && \  
wget http://ftpmirror.gnu.org/libtool/libtool-2.4.6.tar.gz && \  
mkdir libtool && \  
tar xf libtool-2.4.6.tar.gz -C libtool --strip-components=1 && \  
cd /root/src/libtool && \  
autoconf && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
cd /root/src && \  
wget http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz && \  
mkdir bzip2 && \  
tar xf bzip2-1.0.6.tar.gz -C bzip2 --strip-components=1 && \  
cd /root/src/bzip2 && \  
sed -i -e 's/CFLAGS=-Wall/CFLAGS=-fpic -fPIC -Wall/g' Makefile && \  
make && \  
make install PREFIX=/usr && \  
make -f Makefile-libbz2_so && \  
cp libbz2.so.1.0* /usr/lib && \  
cd /root/src && \  
wget https://zlib.net/zlib-1.2.11.tar.gz && \  
mkdir zlib && \  
tar xf zlib-1.2.11.tar.gz -C zlib --strip-components=1 && \  
cd /root/src/zlib && \  
./configure --prefix=/usr --shared --libdir=/lib && \  
make && \  
cd /root/src && \  
wget
https://jaist.dl.sourceforge.net/project/boost/boost/1.54.0/boost_1_54_0.tar.gz
&& \  
mkdir /root/src/boost && \  
tar xf boost_1_54_0.tar.gz -C boost --strip-components=1 && \  
cd /root/src/boost && \  
export ZLIB_SOURCE=/root/src/zlib && \  
./bootstrap.sh && \  
./b2 install -j8 --prefix=/opt/boost-1.54 && \  
cd /root/src && \  
rm -rf /root/src/* && \  
git clone https://github.com/xevolver/rose-xev.git && \  
cd /root/src/rose-xev && \  
export JAVA_HOME=`readlink /etc/alternatives/java_sdk_openjdk` && \  
export
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${JAVA_HOME}/lib:${JAVA_HOME}/jre/lib/amd64/server
&& \  
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/boost-1.54/lib && \  
export
PATH=$PATH:/opt/boost-1.54:/opt/boost-1.54/lib:/opt/boost-1.54/include:${JAVA_HOME}/lib:${JAVA_HOME}/jre/lib/amd64/server
&& \  
./build && \  
mkdir mybuild && \  
cd mybuild && \  
../configure --prefix=/opt/rose \--with-java --with-boost=/opt/boost-1.54
\--with-boostlib=/opt/boost-1.54/lib && \  
make -j8 && \  
make install && \  
cd /root && \  
rm -rf /root/src && \  
echo 'export JAVA_HOME=`readlink /etc/alternatives/java_sdk_openjdk`' >
/opt/rose/setPATH.sh && \  
echo 'export
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rose/lib:/opt/boost-1.54/lib:${JAVA_HOME}/lib:${JAVA_HOME}/jre/lib/amd64/server'
>> /opt/rose/setPATH.sh && \  
echo 'export
C_INCLUDE_PATH=$C_INCLUDE_PATH:/opt/rose/include/rose:/opt/boost-1.54/include'
>> /opt/rose/setPATH.sh && \  
echo 'export
CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/opt/rose/include/rose:/opt/boost-1.54/include'
>> /opt/rose/setPATH.sh && \  
echo 'export PATH=$PATH:/opt/rose/bin' >> /opt/rose/setPATH.sh && \  
echo 'source /opt/rose/setPATH.sh' > /etc/profile.d/rose.sh  

