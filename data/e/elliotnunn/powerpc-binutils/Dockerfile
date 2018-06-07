FROM gcc  
MAINTAINER Elliot Nunn <elliotnunn@fastmail.com>  
  
# Versions after 2.22 break "lis label" and similar instructions  
# Don't particularly need the embedded ABI but it's as good as any other  
WORKDIR /binutils  
  
RUN curl http://ftp.gnu.org/gnu/binutils/binutils-2.22.tar.bz2 | tar xj
--strip-components 1 && \  
./configure \  
\--target=powerpc-eabi \  
\--disable-nls \  
\--disable-werror \  
\--prefix=/usr/local \  
\--program-prefix='' \  
&& make && make install  
  
WORKDIR /  
  
RUN rm -rf /binutils  
  
ENV PATH /usr/local/bin  

