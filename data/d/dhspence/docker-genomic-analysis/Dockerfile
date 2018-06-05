FROM ubuntu:xenial  
MAINTAINER David Spencer <dspencer@wustl.edu>  
  
LABEL Image for basic ad-hoc bioinformatic analyses  
  
#some basic tools  
RUN apt-get update && apt-get install -y --no-install-recommends locales && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
LC_ALL=en_US.UTF-8 && \  
LANG=en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 && \  
TERM=xterm  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
build-essential \  
bzip2 \  
curl \  
default-jdk \  
default-jre \  
emacs \  
emacs-goodies-el \  
g++ \  
git \  
less \  
libcurl4-openssl-dev \  
libpng-dev \  
libssl-dev \  
libxml2-dev \  
make \  
ncurses-dev \  
nodejs \  
pkg-config \  
python \  
rsync \  
unzip \  
wget \  
zip \  
libbz2-dev \  
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
zlib1g-dev \  
bc  
  
#  
# Some perl modules  
#  
RUN cpan install Statistics::Basic && cpan install JSON  
  
##############  
#HTSlib 1.5#  
##############  
ENV HTSLIB_INSTALL_DIR=/opt/htslib  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/htslib/releases/download/1.5/htslib-1.5.tar.bz2 &&
\  
tar --bzip2 -xvf htslib-1.5.tar.bz2 && \  
cd /tmp/htslib-1.5 && \  
./configure --enable-plugins --prefix=$HTSLIB_INSTALL_DIR && \  
make && \  
make install && \  
cp $HTSLIB_INSTALL_DIR/lib/libhts.so* /usr/lib/ && \  
ln -s $HTSLIB_INSTALL_DIR/bin/tabix /usr/bin/tabix  
  
################  
#Samtools 1.5#  
################  
ENV SAMTOOLS_INSTALL_DIR=/opt/samtools  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
&& \  
tar --bzip2 -xf samtools-1.5.tar.bz2 && \  
cd /tmp/samtools-1.5 && \  
./configure --with-htslib=$HTSLIB_INSTALL_DIR --prefix=$SAMTOOLS_INSTALL_DIR
&& \  
make && \  
make install && \  
ln -s /opt/samtools/bin/* /usr/local/bin/ && \  
cd / && \  
rm -rf /tmp/samtools-1.5  
  
################  
#bcftools 1.5#  
################  
ENV BCFTOOLS_INSTALL_DIR=/opt/bcftools  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/bcftools/releases/download/1.5/bcftools-1.5.tar.bz2
&& \  
tar --bzip2 -xf bcftools-1.5.tar.bz2 && \  
cd /tmp/bcftools-1.5 && \  
make prefix=$BCFTOOLS_INSTALL_DIR && \  
make prefix=$BCFTOOLS_INSTALL_DIR install && \  
ln -s /opt/bcftools/bin/* /usr/local/bin/ && \  
cd / && \  
rm -rf /tmp/bcftools-1.5  
  
  
##############  
#Picard 2.13.1#  
##############  
ENV picard_version 2.13.1  
  
# Assumes Dockerfile lives in root of the git repo. Pull source files into  
# container  
RUN apt-get update && apt-get install ant --no-install-recommends -y && \  
cd /usr/ && \  
git config --global http.sslVerify false && \  
git clone --recursive https://github.com/broadinstitute/picard.git && \  
cd picard && \  
./gradlew shadowJar && \  
mv build/libs/picard.jar picard.jar && \  
./gradlew clean && \  
rm -rf src && \  
rm -rf gradle && \  
rm -rf .git && \  
rm gradlew && \  
rm build.gradle && \  
cp picard.jar /usr/local/bin/ && \  
echo '#!/bin/bash'"\n"'java -Xmx16g -jar /usr/local/bin/picard.jar $@' >
/usr/local/bin/picard && \  
chmod a+x /usr/local/bin/picard  
  
##############  
## bedtools ##  
  
WORKDIR /usr/local  
RUN git clone https://github.com/arq5x/bedtools2.git && \  
cd /usr/local/bedtools2 && \  
git checkout v2.25.0 && \  
make && \  
ln -s /usr/local/bedtools2/bin/* /usr/local/bin/  
  
##############  
## vcftools ##  
ENV ZIP=vcftools-0.1.14.tar.gz  
ENV URL=https://github.com/vcftools/vcftools/releases/download/v0.1.14/  
ENV FOLDER=vcftools-0.1.14  
ENV DST=/tmp  
  
RUN wget $URL/$ZIP -O $DST/$ZIP && \  
tar xvf $DST/$ZIP -C $DST && \  
rm $DST/$ZIP && \  
cd $DST/$FOLDER && \  
./configure && \  
make && \  
make install && \  
cd / && \  
rm -rf $DST/$FOLDER  
  
  
##################  
# ucsc utilities #  
RUN mkdir -p /tmp/ucsc && \  
cd /tmp/ucsc && \  
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig
http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedToBigBed
http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bigBedToBed
http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bigWigAverageOverBed
http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bigWigToBedGraph
http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/wigToBigWig && \  
chmod ugo+x * && \  
mv * /usr/bin/  
  
############################  
# R, bioconductor packages #  
# from https://raw.githubusercontent.com/rocker-org/rocker-
versioned/master/r-ver/3.4.0/Dockerfile  
# we'll pin to 3.4.0 for now  
ARG R_VERSION  
ARG BUILD_DATE  
ENV BUILD_DATE 2017-06-20  
ENV R_VERSION=${R_VERSION:-3.4.0}  
RUN cd /tmp/ && \  
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
  
#################################  
# Python 2 and 3, plus packages  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
  
# Install conda  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
curl -s https://repo.continuum.io/miniconda/Miniconda3-4.3.21-Linux-x86_64.sh
-o miniconda.sh && \  
/bin/bash miniconda.sh -f -b -p $CONDA_DIR && \  
rm miniconda.sh && \  
$CONDA_DIR/bin/conda config --system --add channels conda-forge && \  
$CONDA_DIR/bin/conda config --system --set auto_update_conda false && \  
conda clean -tipsy  
  
# Install Python 3 packages available through pip  
RUN conda install --yes 'pip' && \  
conda clean -tipsy && \  
#dependencies sometimes get weird - installing each on it's own line seems to
help  
pip install numpy==1.13.0 && \  
pip install scipy==0.19.0 && \  
pip install cruzdb==0.5.6 && \  
pip install cython==0.25.2 && \  
pip install pyensembl==1.1.0 && \  
pip install pyfaidx==0.4.9.2 && \  
pip install pybedtools==0.7.10 && \  
pip install cyvcf2==0.7.4 && \  
pip install intervaltree_bio==1.0.1 && \  
pip install pandas==0.20.2 && \  
pip install scipy==0.19.0 && \  
pip install pysam==0.11.2.2 && \  
pip install seaborn==0.7.1 && \  
pip install scikit-learn==0.18.2  
  
# Install Python 2  
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 'pip' &&
\  
conda clean -tipsy && \  
/bin/bash -c "source activate python2 && \  
#dependencies sometimes get weird - installing each on it's own line seems to
help  
pip install numpy==1.13.0 && \  
pip install scipy==0.19.0 && \  
pip install cruzdb==0.5.6 && \  
pip install cython==0.25.2 && \  
pip install pyensembl==1.1.0 && \  
pip install pyfaidx==0.4.9.2 && \  
pip install pybedtools==0.7.10 && \  
pip install cyvcf2==0.7.4 && \  
pip install intervaltree_bio==1.0.1 && \  
pip install pandas==0.20.2 && \  
pip install scipy==0.19.0 && \  
pip install pysam==0.11.2.2 && \  
pip install seaborn==0.7.1 && \  
pip install scikit-learn==0.18.2 && \  
source deactivate"  
  
# needed for MGI data mounts  
RUN apt-get update && apt-get install -y libnss-sss && apt-get clean all  
  
#set timezone to CDT  
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime  
#LSF: Java bug that need to change the /etc/timezone.  
# The above /etc/localtime is not enough.  
RUN echo "America/Chicago" > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# some other utils  
RUN apt-get update && apt-get install -y --no-install-recommends gawk openssh-
client grep evince && apt-get clean all  
  
RUN mkdir /tmp/bin  
ENV PATH=/bin:/usr/bin:${PATH}  
  

