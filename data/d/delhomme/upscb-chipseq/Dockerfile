FROM delhomme/upscb-ngs-preprocessing  
MAINTAINER Nicolas Delhomme (nicolas.delhomme@umu.se)  
  
#########  
### Aptitude packages  
#########  
RUN apt-get update  
RUN apt install -y libncurses-dev libpcre3-dev libxml2-dev libblas-dev
gfortran git unzip libzmq3-dev \  
nano ftp fort77 libreadline-dev libcurl4-openssl-dev libx11-dev libxt-dev
x11-common \  
libcairo2-dev libpng12-dev libreadline6-dev libjpeg8-dev pkg-config texlive-
latex-base \  
texinfo texlive-fonts-extra default-jdk  
  
#########  
### Working dir  
#########  
RUN mkdir build  
WORKDIR /build  
  
#########  
### R version 3.4.3  
#########  
RUN wget http://ftp.acc.umu.se/mirror/CRAN/src/base/R-3/R-3.4.3.tar.gz && \  
tar -zxf R-3.4.3.tar.gz && cd R-3.4.3 && \  
./configure --enable-memory-profiling -enable-R-shlib --with-blas --with-
lapack \  
\--with-valgrind-instrumentation=3 \--with-readline --with-cairo --with-libpng
--with-jpeglib --with-x=no && \  
make && make pdf && make info && make install && make install-info && make
install-pdf  
## make && make check && make pdf && make info && make install && make
install-info && make install-pdf  
  
#########  
# R packages  
#########  
WORKDIR /home/training  
ADD R-package-list.txt /home/training/R-package-list.txt  
ADD R-install-packages.R /home/training/R-install-packages.R  
RUN Rscript R-install-packages.R  
  
#########  
### BWA  
#########  
RUN wget http://downloads.sourceforge.net/project/bio-bwa/bwa-0.7.17.tar.bz2
&& \  
tar -xf bwa-0.7.17.tar.bz2  
WORKDIR bwa-0.7.17  
RUN make && \  
cp bwa /usr/local/bin/  
  
#########  
### Pip installs: MACS2  
#########  
# PySam  
RUN pip install MACS2  
WORKDIR /build  
  
#########  
### USeq and Sissrs  
#########  
RUN mkdir /data && \  
wget
https://github.com/HuntsmanCancerInstitute/USeq/releases/download/USeq_9.1.3/USeq_9.1.3.zip
&& \  
unzip USeq_9.1.3.zip && mv USeq_9.1.3 /usr/share/USeq && \  
wget http://dir.nhlbi.nih.gov/papers/lmi/epigenomes/sissrs/sissrs_v1.4.tar.gz
&& \  
tar -xf sissrs_v1.4.tar.gz && \  
cp sissrs.pl /usr/local/bin  
  
#########  
### Clean up  
#########  
WORKDIR /home/training  
RUN rm -rf R-package-list.txt R-install-packages.R  
WORKDIR /  
RUN rm -rf /build  
  
#########  
### Ports and CMD  
#########  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

