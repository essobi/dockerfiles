FROM ubuntu  
MAINTAINER Nicolas Delhomme (nicolas.delhomme@umu.se)  
RUN groupadd -g 2000 training && useradd -m -u 2000 -g 2000 training  
RUN echo 'training:training' | chpasswd  
RUN chsh -s /bin/bash training  
RUN echo "alias ll='ls -la -G'" >> /home/training/.profile  
  
#########  
### Aptitude packages  
#########  
RUN apt-get update  
RUN apt-get install -y --fix-missing \  
build-essential wget libghc-zlib-dev libncurses-dev libpcre3-dev libxml2-dev
locales libbz2-dev liblzma-dev \  
libblas-dev gfortran git unzip ftp libzmq3-dev nano ftp fort77 libreadline-dev
libcurl4-openssl-dev default-jdk \  
libx11-dev libxt-dev x11-common libcairo2-dev libpng12-dev libreadline6-dev
libjpeg8-dev pkg-config texlive-latex-base \  
texinfo texlive-fonts-extra zip supervisor tcl-dev tk-dev && \  
mkdir build  
WORKDIR /build  
  
#########  
### Squash locale warnings  
#########  
RUN rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
#########  
### R version 3.4.3  
#########  
RUN wget http://ftp.acc.umu.se/mirror/CRAN/src/base/R-3/R-3.4.3.tar.gz && \  
tar -zxf R-3.4.3.tar.gz && cd R-3.4.3 && \  
./configure --enable-memory-profiling -enable-R-shlib --with-blas --with-
lapack --with-tcltk \  
\--with-valgrind-instrumentation=3 --with-readline --with-cairo --with-libpng
--with-jpeglib --with-x=no && \  
make && make pdf && make info && make install && make install-info && make
install-pdf  
## make && make check && make pdf && make info && make install && make
install-info && make install-pdf  
#########  
### Cleanup  
#########  
WORKDIR /  
RUN rm -rf build  
  
#########  
### supervisord  
#########  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#########  
### Volumes  
#########  
RUN mkdir /home/training/share  
VOLUME /home/training/share  
  
#########  
### CMD  
#########  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

