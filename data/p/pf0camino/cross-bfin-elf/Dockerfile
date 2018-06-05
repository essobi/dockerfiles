FROM codenvy/cpp_gcc  
MAINTAINER Masaki Muranaka <monaka@pizzafactory.jp>  
  
USER root  
  
RUN mkdir -p /opt/uClinux  
RUN curl -q http://jaist.dl.sourceforge.net/project/adi-
toolchain/2014R1/2014R1-RC2/x86_64/blackfin-
toolchain-2014R1-RC2.x86_64.tar.bz2 2>/dev/null | tar xCjf / -  
RUN curl -q http://jaist.dl.sourceforge.net/project/adi-
toolchain/2014R1/2014R1-RC2/x86_64/blackfin-toolchain-elf-
gcc-4.3-2014R1-RC2.x86_64.tar.bz2 2>/dev/null | tar xCjf / -  
RUN curl -q http://jaist.dl.sourceforge.net/project/adi-
toolchain/2014R1/2014R1-RC2/x86_64/blackfin-toolchain-uclibc-
full-2014R1-RC2.x86_64.tar.bz2 2>/dev/null | tar xCjf / -  
  
RUN echo export 'PATH=/opt/uClinux/bfin-elf/bin:/opt/uClinux/bfin-linux-
uclibc/bin:/opt/uClinux/bfin-uclinux/bin:$PATH' >> /home/user/.bashrc  
  
USER user  

