FROM ubuntu:xenial  
MAINTAINER "Chris Miller" <c.a.miller@wustl.edu>  
  
RUN apt-get update -y && apt-get install -y \  
build-essential \  
cmake \  
curl \  
default-jdk \  
git \  
libncurses5-dev \  
libcurl4-openssl-dev \  
libtbb2 \  
libtbb-dev \  
nodejs \  
python-dev \  
python-pip \  
tzdata \  
wget \  
zlib1g-dev \  
zip  
  
##################  
# Biscuit v0.2.2 #  
##################  
RUN cd /tmp/ && \  
wget
https://github.com/zwdzwd/biscuit/releases/download/v0.2.2.20170522/release-v0.2.2.zip
&& \  
unzip release-v0.2.2.zip && \  
cd biscuit-release && \  
make && \  
cp biscuit /usr/bin && \  
rm -rf /tmp/biscuit*  
  
##############  
#Picard 2.4.1#  
##############  
ENV picard_version 2.4.1  
# Assumes Dockerfile lives in root of the git repo. Pull source files into  
# container  
RUN apt-get update && apt-get install ant --no-install-recommends -y && \  
cd /usr/ && \  
git config --global http.sslVerify false && \  
git clone --recursive https://github.com/broadinstitute/picard.git && \  
cd /usr/picard && \  
git checkout tags/${picard_version} && \  
cd /usr/picard && \  
# Clone out htsjdk. First turn off git ssl verification  
git config --global http.sslVerify false && \  
git clone https://github.com/samtools/htsjdk.git && \  
cd htsjdk && \  
git checkout tags/${picard_version} && \  
cd .. && \  
# Build the distribution jar, clean up everything else  
ant clean all && \  
mv dist/picard.jar picard.jar && \  
mv src/scripts/picard/docker_helper.sh docker_helper.sh && \  
ant clean && \  
rm -rf htsjdk && \  
rm -rf src && \  
rm -rf lib && \  
rm build.xml  
  
  
############################  
# R, bioconductor packages #  
############################  
# partially from https://raw.githubusercontent.com/rocker-org/rocker-
versioned/master/r-ver/3.4.0/Dockerfile  
# we'll pin to v 3.4.0 for now  
  
ARG R_VERSION  
ARG BUILD_DATE  
ENV BUILD_DATE 2017-06-20  
ENV R_VERSION=${R_VERSION:-3.4.0}  
RUN apt-get update && apt-get install -y --no-install-recommends locales && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
LC_ALL=en_US.UTF-8 && \  
LANG=en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 && \  
TERM=xterm && \  
apt-get install -y --no-install-recommends \  
bash-completion \  
ca-certificates \  
file \  
fonts-texgyre \  
g++ \  
gfortran \  
gsfonts \  
libbz2-1.0 \  
libcurl3 \  
libicu55 \  
libjpeg-turbo8 \  
libopenblas-dev \  
libpangocairo-1.0-0 \  
libpcre3 \  
libpng12-0 \  
libtiff5 \  
liblzma5 \  
locales \  
zlib1g \  
libbz2-dev \  
libcairo2-dev \  
libcurl4-openssl-dev \  
libpango1.0-dev \  
libjpeg-dev \  
libicu-dev \  
libpcre3-dev \  
libpng-dev \  
libreadline-dev \  
libtiff5-dev \  
liblzma-dev \  
libx11-dev \  
libxt-dev \  
perl \  
tcl8.5-dev \  
tk8.5-dev \  
texinfo \  
texlive-extra-utils \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-latex-recommended \  
x11proto-core-dev \  
xauth \  
xfonts-base \  
xvfb \  
zlib1g-dev && \  
cd /tmp/ && \  
## Download source code  
curl -O https://cran.r-project.org/src/base/R-3/R-${R_VERSION}.tar.gz && \  
## Extract source code  
tar -xf R-${R_VERSION}.tar.gz && \  
cd R-${R_VERSION} && \  
## Set compiler flags  
R_PAPERSIZE=letter && \  
R_BATCHSAVE="--no-save --no-restore" && \  
R_BROWSER=xdg-open && \  
PAGER=/usr/bin/pager && \  
PERL=/usr/bin/perl && \  
R_UNZIPCMD=/usr/bin/unzip && \  
R_ZIPCMD=/usr/bin/zip && \  
R_PRINTCMD=/usr/bin/lpr && \  
LIBnn=lib && \  
AWK=/usr/bin/awk && \  
CFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security
-Wdate-time -D_FORTIFY_SOURCE=2 -g" && \  
CXXFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security
-Wdate-time -D_FORTIFY_SOURCE=2 -g" && \  
## Configure options  
./configure --enable-R-shlib \  
\--enable-memory-profiling \  
\--with-readline \  
\--with-blas="-lopenblas" \  
\--disable-nls \  
\--without-recommended-packages && \  
## Build and install  
make && \  
make install && \  
## Add a default CRAN mirror  
echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'),
download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site && \  
## Add a library directory (for user-installed packages)  
mkdir -p /usr/local/lib/R/site-library && \  
chown root:staff /usr/local/lib/R/site-library && \  
chmod g+wx /usr/local/lib/R/site-library && \  
## Fix library path  
echo "R_LIBS_USER='/usr/local/lib/R/site-library'" >>
/usr/local/lib/R/etc/Renviron && \  
echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-
library:/usr/local/lib/R/library:/usr/lib/R/library'}" >>
/usr/local/lib/R/etc/Renviron && \  
## install packages from date-locked MRAN snapshot of CRAN  
[ -z "$BUILD_DATE" ] && BUILD_DATE=$(TZ="America/Los_Angeles" date -I) || true
&& \  
MRAN=https://mran.microsoft.com/snapshot/${BUILD_DATE} && \  
echo MRAN=$MRAN >> /etc/environment && \  
export MRAN=$MRAN && \  
echo "options(repos = c(CRAN='$MRAN'), download.file.method = 'libcurl')" >>
/usr/local/lib/R/etc/Rprofile.site && \  
## Use littler installation scripts  
Rscript -e "install.packages(c('littler', 'docopt'), repo = '$MRAN')" && \  
ln -s /usr/local/lib/R/site-library/littler/examples/install2.r
/usr/local/bin/install2.r && \  
ln -s /usr/local/lib/R/site-library/littler/examples/installGithub.r
/usr/local/bin/installGithub.r && \  
ln -s /usr/local/lib/R/site-library/littler/bin/r /usr/local/bin/r  
## install r packages, bioconductor, etc ##  
ADD rpackages.R /tmp/  
RUN R -f /tmp/rpackages.R  
  
## Clean up  
RUN cd / && \  
rm -rf /tmp/* && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
#################  
#Sambamba v0.6.4#  
#################  
  
RUN mkdir /opt/sambamba/ \  
&& wget
https://github.com/lomereiter/sambamba/releases/download/v0.6.4/sambamba_v0.6.4_linux.tar.bz2
\  
&& tar --extract --bzip2 --directory=/opt/sambamba
\--file=sambamba_v0.6.4_linux.tar.bz2 \  
&& ln -s /opt/sambamba/sambamba_v0.6.4 /usr/bin/sambamba  
ADD sambamba_merge /usr/bin/  
RUN chmod +x /usr/bin/sambamba_merge  
  
##################  
# ucsc utilities #  
RUN mkdir -p /tmp/ucsc && \  
cd /tmp/ucsc && \  
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig &&
\  
chmod ugo+x * && \  
mv * /usr/bin/ && \  
rm -rf /tmp/ucsc  
  
###############  
#Flexbar 3.0.3#  
###############  
  
RUN mkdir -p /opt/flexbar/tmp \  
&& cd /opt/flexbar/tmp \  
&& wget https://github.com/seqan/flexbar/archive/v3.0.3.tar.gz \  
&& wget https://github.com/seqan/seqan/releases/download/seqan-v2.2.0/seqan-
library-2.2.0.tar.xz \  
&& tar xzf v3.0.3.tar.gz \  
&& tar xJf seqan-library-2.2.0.tar.xz \  
&& mv seqan-library-2.2.0/include flexbar-3.0.3 \  
&& cd flexbar-3.0.3 \  
&& cmake . \  
&& make \  
&& cp flexbar /opt/flexbar/ \  
&& cd / \  
&& rm -rf /opt/flexbar/tmp  
  
##############  
#HTSlib 1.3.2#  
##############  
ENV HTSLIB_INSTALL_DIR=/opt/htslib  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2
&& \  
tar --bzip2 -xvf htslib-1.3.2.tar.bz2 && \  
cd /tmp/htslib-1.3.2 && \  
./configure --enable-plugins --prefix=$HTSLIB_INSTALL_DIR && \  
make && \  
make install && \  
cp $HTSLIB_INSTALL_DIR/lib/libhts.so* /usr/lib/  
################  
#Samtools 1.3.1#  
################  
ENV SAMTOOLS_INSTALL_DIR=/opt/samtools  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
tar --bzip2 -xf samtools-1.3.1.tar.bz2 && \  
cd /tmp/samtools-1.3.1 && \  
./configure --with-htslib=$HTSLIB_INSTALL_DIR --prefix=$SAMTOOLS_INSTALL_DIR
&& \  
make && \  
make install && \  
cd / && \  
rm -rf /tmp/samtools-1.3.1  
#wrapper script for converting bam to cram  
ADD bam_to_cram /usr/bin/  
#wrapper script for converting vcf2bed  
ADD bsvcf2bed /usr/bin/  
  
######  
#Toil#  
######  
RUN apt-get update -y && apt-get install -y \  
nodejs \  
python-dev \  
python-pip \  
tzdata  
RUN pip install --upgrade pip \  
&& pip install toil[cwl]==3.12.0 \  
&& sed -i 's/select\\[type==X86_64 && mem/select[mem/'
/usr/local/lib/python2.7/dist-packages/toil/batchSystems/lsf.py  
######  
# Needed for MGI mounts  
######  
RUN apt-get update -y && apt-get install -y libnss-sss  
  
## clean up  
RUN apt-get clean autoclean && apt-get autoremove -y  

