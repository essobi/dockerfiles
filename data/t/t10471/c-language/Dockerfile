  
FROM t10471/base:latest  
  
MAINTAINER t10471 <t104711202@gmail.com>  
  
## disable prompts from apt  
ENV DEBIAN_FRONTEND noninteractive  
  
## custom apt-get install options  
ENV OPTS_APT -y --force-yes --no-install-recommends  
  
RUN apt-get update\  
&& apt-get install ${OPTS_APT}\  
gdb \  
valgrind \  
strace \  
cmake \  
scons \  
libcunit1 \  
libcunit1-dev \  
libgtest-dev \  
libgoogle-perftools-dev \  
kcachegrind \  
doxygen \  
clang \  
clang-format-3.5 \  
m4 \  
flex \  
bison \  
libreadline6 \  
zlib1g \  
libc6 \  
libc6-dev \  
libgmp10 \  
libgmp-dev \  
libncursesw5 \  
libtinfo5  
  
WORKDIR /root/tmp  
RUN wget -O- http://tamacom.com/global/global-6.3.2.tar.gz | tar xz  
WORKDIR /root/tmp/global-6.3.2  
RUN ./configure  
RUN make  
RUN checkinstall \  
\--type=debian \  
\--install=yes \  
\--pkgname="global" \  
\--maintainer="ubuntu-devel-discuss@lists.ubuntu.com" \  
\--nodoc \  
\--default  
  
## ダイナミックライブラリを追加  
RUN touch /etc/ld.so.conf.d/my.conf  
RUN echo '/root/workspace/HeadFistC/lib' > /etc/ld.so.conf.d/my.conf  
  
ADD init.sh /root/  
ADD gtags.sh /root/  

