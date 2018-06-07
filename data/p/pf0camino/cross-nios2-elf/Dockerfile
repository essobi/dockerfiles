FROM codenvy/cpp_gcc  
MAINTAINER Masaki Muranaka <monaka@pizzafactory.jp>  
  
USER root  
  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 && \  
apt-get autoremove -y && \  
apt-get autoclean -y  
  
RUN curl -q
https://sourcery.mentor.com/public/gnu_toolchain/nios2-elf/sourceryg++-2016.05-9-nios2-elf-i686-pc-
linux-gnu.tar.bz2 2>/dev/null | tar xCjf /opt -  
RUN mkdir -p /opt/src/  
RUN curl -q
https://sourcery.mentor.com/public/gnu_toolchain/nios2-elf/sourceryg++-2016.05-9-nios2-elf.src.tar.bz2
2>/dev/null > /opt/src/gcc.src.tar.bz2  
  
RUN echo 'PATH=/opt/sourceryg++-2016.05/bin:$PATH' >> /home/user/.bashrc  
  
USER user  

