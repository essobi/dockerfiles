############################################################  
# Dockerfile to build docker image: flowrbio/ultraseq  
############################################################  
# Set the base image to flowr on Ubuntu 16.04  
# Source:
https://raw.githubusercontent.com/flow-r/docker_ultraseq/ultraseq/Dockerfile  
# Image at https://hub.docker.com/r/flowrbio/ultraseq/  
  
FROM ubuntu:16.04  
## For questions, visit https:  
MAINTAINER "Samir B. Amin" <tweet:sbamin; sbamin.com/contact>  
  
LABEL version="1.0-b2" \  
mode="devp version for GLASS" \  
description="docker image to run GLASS consortium WGS SNV and SV pipeline" \  
contributor1="flowr and ultraseq variant caller pipeline by Sahil Seth, tweet:
sethsa" \  
contributor2="variant calling pipeline code by Hoon Kim, tweet: wisekh6" \  
website="http://glass-consortium.org" \  
code="http://odin.mdacc.tmc.edu/~rverhaak/resources" \  
contact="Dr. Roel GW Verhaak http://odin.mdacc.tmc.edu/~rverhaak/contact/
tweet:roelverhaak" \  
NOTICE="Third party license: Use of GATK and Mutect tools are subject to
approval by GATK team at the Broad Institute, Cambridge, MA, USA. This docker
image can not be deployed in public prior to getting appropriate licenses from
the Broad Institute to use GATK and mutect for use with GLASS consortium
related analysis pipelines."  
#### Install dependencies, build utilities ####  
RUN apt-get update && \  
apt-get install \--yes \--no-install-recommends build-essential python-
software-properties \  
python-setuptools sudo locales ca-certificates \  
software-properties-common cmake libcurl4-openssl-dev wget curl \  
gdebi tar zip unzip rsync screen nano vim dos2unix bc \  
libxml2-dev libssl-dev \  
dpkg-dev libx11-dev libxpm-dev libxft-dev libxext-dev libpng-dev libjpeg-dev
binutils \  
libncurses-dev zlib1g-dev \  
ruby libarchive-zip-perl libdbd-mysql-perl libjson-perl && \  
add-apt-repository \--yes ppa:git-core/ppa && \  
apt-get update && \  
apt-get install \--yes \--no-install-recommends git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
## overwrite /etc/profile with one having pathmunge function  
ADD ./config/profile /etc/  
## Configure default locale, Ref.: https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.utf8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8  
  
# Create non-root user, glass with passwordless sudo privileges  
# http://askubuntu.com/a/574454/52398  
RUN useradd -m -d /home/glass -s /bin/bash -c "GLASS User" -U glass && \  
usermod -a -G staff,sudo glass && \  
echo "%sudo ALL=(ALL) NOPASSWD:ALL" | (EDITOR="tee -a" visudo) && \  
id -a glass  
  
# Install miniconda2 python  
RUN mkdir -p /opt && \  
wget \--no-check-certificate
https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O
/opt/miniconda.sh && \  
bash /opt/miniconda.sh -b -p /opt/miniconda -f && \  
rm -f /opt/miniconda.sh && \  
echo 'pathmunge /opt/miniconda/bin' >> /etc/profile.d/3_ngspaths.sh  
#### Install Java JDK 7 and 8 ####  
## https://launchpad.net/~webupd8team/+archive/ubuntu/java  
  
RUN add-apt-repository \--yes ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install \--yes \--no-install-recommends oracle-java7-installer && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install \--yes \--no-install-recommends oracle-java8-installer && \  
mkdir -p /opt/java && cd /opt/java && \  
ln -s /usr/lib/jvm/java-8-oracle/jre jre8 && \  
ln -s /usr/lib/jvm/java-7-oracle/jre jre7 && \  
apt-get install \--yes \--no-install-recommends oracle-java8-set-default && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#### Set env ####  
ENV
PATH=/opt/miniconda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-8-oracle/bin:/usr/lib/jvm/java-8-oracle/db/bin:/usr/lib/jvm/java-8-oracle/jre/bin
\  
JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
J2SDKDIR=/usr/lib/jvm/java-8-oracle \  
J2REDIR=/usr/lib/jvm/java-8-oracle/jre  
## By default, updated java jdk 8 will be set at /usr/java/ and /usr/bin/java.  
## Java 1.7 is required for mutect.  
#### Install R ####  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list && \  
gpg \--keyserver keyserver.ubuntu.com \--recv-key E084DAB9 && \  
gpg -a \--export E084DAB9 | apt-key add - && \  
apt-get update && \  
apt-get install \--yes \--no-install-recommends r-base r-base-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
########## Install flowr ##########  
## Install R packages and setup flowr for user: root  
RUN mkdir -p /opt && \  
mkdir -p /scratch && \  
cd /opt && \  
mkdir -p /usr/share/doc/R-3.3.0/html && \  
Rscript -e 'install.packages(c("httr", "git2r", "stringr", "dplyr", "tidyr",
"devtools", "params", "flowr", "funr"), repos =
c(CRAN="http://cran.rstudio.com"))' && \  
Rscript -e 'devtools::install_github("glass-consortium/ultraseq", subdir =
"ultraseq", ref="master")' && \  
mkdir -p /root/bin && \  
Rscript -e 'library(flowr);setup()' && \  
rm -f /opt/Rplots.pdf && \  
/usr/local/lib/R/site-library/flowr/scripts/flowr run x=sleep_pipe
platform=local execute=TRUE && \  
rm -f /root/Rplots.pdf && \  
ln -s /usr/local/lib/R/site-library/flowr/scripts/flowr /usr/local/bin/flowr  
## setup flowr for user: glass  
USER glass  
  
RUN mkdir -p /home/glass/bin && \  
Rscript -e 'library(flowr);setup()' && \  
/usr/local/bin/flowr run x=sleep_pipe platform=local execute=TRUE && \  
rm -f /home/glass/Rplots.pdf  
####### flowr setup complete #########  
  
USER root  
#### Install samtools, bcftools, htslib ####  
RUN mkdir -p /opt/samtools && cd /opt/samtools && \  
wget \--no-check-certificate
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
tar xvjf samtools-1.3.1.tar.bz2 && \  
cd samtools-1.3.1 && make && make prefix=/opt/samtools/samtools install && \  
echo 'pathmunge /opt/samtools/samtools/bin after' >>
/etc/profile.d/3_ngspaths.sh && \  
rm -rf /opt/samtools/samtools-1.3.1 /opt/samtools/samtools-1.3.1.tar.bz2  
  
RUN cd /opt/samtools && \  
wget \--no-check-certificate
https://github.com/samtools/bcftools/releases/download/1.3.1/bcftools-1.3.1.tar.bz2
&& \  
tar xvjf bcftools-1.3.1.tar.bz2 && \  
cd bcftools-1.3.1 && make && make prefix=/opt/samtools/bcftools install && \  
echo 'pathmunge /opt/samtools/bcftools/bin after' >>
/etc/profile.d/3_ngspaths.sh && \  
rm -rf /opt/samtools/bcftools-1.3.1 /opt/samtools/bcftools-1.3.1.tar.bz2  
  
RUN cd /opt/samtools && \  
wget \--no-check-certificate
https://github.com/samtools/htslib/releases/download/1.3.1/htslib-1.3.1.tar.bz2
&& \  
tar xvjf htslib-1.3.1.tar.bz2 && \  
cd htslib-1.3.1 && make && make prefix=/opt/samtools/htslib install && \  
echo 'pathmunge /opt/samtools/htslib/bin after' >>
/etc/profile.d/3_ngspaths.sh && \  
rm -rf /opt/samtools/htslib-1.3.1 /opt/samtools/htslib-1.3.1.tar.bz2  
#### Install bwa ####  
RUN cd /opt && \  
wget \--no-check-certificate
https://github.com/lh3/bwa/releases/download/v0.7.15/bwakit-0.7.15_x64-linux.tar.bz2
-O bwakit.tar.bz2 && \  
tar xvjf bwakit.tar.bz2 && \  
mv bwa.kit bwa && \  
echo 'pathmunge /opt/bwa after' >> /etc/profile.d/3_ngspaths.sh && \  
rm -rf /opt/bwakit.tar.bz2  
#### Install bedtools ####  
RUN cd /opt && \  
wget \--no-check-certificate
https://github.com/arq5x/bedtools2/releases/download/v2.26.0/bedtools-2.26.0.tar.gz
-O /opt/bedtools.tar.gz && \  
tar xvzf bedtools.tar.gz && cd /opt/bedtools2 && \  
make && \  
echo 'pathmunge /opt/bedtools2/bin after' >> /etc/profile.d/3_ngspaths.sh && \  
rm -rf /opt/bedtools.tar.gz  
#### Install picard ####  
RUN mkdir -p /opt/picard && \  
wget \--no-check-certificate
https://github.com/broadinstitute/picard/releases/download/2.5.0/picard-
tools-2.5.0.zip -O /opt/picard2.zip && \  
unzip /opt/picard2.zip -d /opt/picard && cd /opt/picard && \  
ln -s picard-tools-2.5.0 default && \  
echo 'pathmunge /opt/picard/default after' >> /etc/profile.d/3_ngspaths.sh &&
\  
rm -rf /opt/picard2.zip  
#### rJava R package under Oracle JDK 1.8 ####  
RUN R CMD javareconf && \  
Rscript -e 'install.packages("rJava", repos =
c(CRAN="http://cran.rstudio.com"))'  
  
## Install bamtools  
## Copyright under MIT License by Derek Barnett, Erik Garrison, Gabor Marth,
Michael Stromberg  
## https://github.com/pezmaster31/bamtools/wiki/Building-and-installing  
RUN cd /opt && \  
git clone git://github.com/pezmaster31/bamtools.git && \  
cd bamtools && \  
git checkout tags/v2.4.0 -b v2.4.0 && \  
mkdir -p build && cd build && \  
cmake .. && make && cd .. && \  
echo 'pathmunge /opt/bamtools/bin after' >> /etc/profile.d/3_ngspaths.sh  
#### Add Sequenza ####  
# http://www.cbs.dtu.dk/biotools/sequenza/  
RUN Rscript -e
"source('http://bioconductor.org/biocLite.R');biocLite('copynumber',
suppressUpdates=TRUE)" && \  
Rscript -e 'install.packages("sequenza", repos =
c(CRAN="http://cran.rstudio.com"))' && \  
mkdir -p /opt/bin && \  
wget \--no-check-certificate
https://raw.githubusercontent.com/cran/sequenza/master/exec/sequenza-utils.py
-O /opt/bin/sequenza-utils.py && \  
chmod 755 /opt/bin/sequenza-utils.py && \  
echo 'pathmunge /opt/bin after' >> /etc/profile.d/3_ngspaths.sh  
#################### Add SpeedSeq ####################  
# https://github.com/hall-lab/speedseq  
#### root package ####  
# Source: https://root.cern.ch/content/release-60606  
# Install tips for Ubuntu 16.04 using gcc and g++ v4.8.5:  
# https://root.cern.ch/phpBB3/viewtopic.php?t=21601#p94328  
# http://askubuntu.com/a/26518/52398  
  
RUN apt-get update && \  
apt-get install \--yes gcc-4.8 g++-4.8 && \  
update-alternatives \--install /usr/bin/gcc gcc /usr/bin/gcc-4.8 10 && \  
update-alternatives \--install /usr/bin/gcc gcc /usr/bin/gcc-5 20 && \  
update-alternatives \--install /usr/bin/g++ g++ /usr/bin/g++-4.8 10 && \  
update-alternatives \--install /usr/bin/g++ g++ /usr/bin/g++-5 20 && \  
update-alternatives \--install /usr/bin/cc cc /usr/bin/gcc 30 && \  
update-alternatives \--set cc /usr/bin/gcc && \  
update-alternatives \--install /usr/bin/c++ c++ /usr/bin/g++ 30 && \  
update-alternatives \--set c++ /usr/bin/g++ && \  
update-alternatives \--display gcc && \  
update-alternatives \--display g++ && \  
update-alternatives \--set gcc "/usr/bin/gcc-4.8" && \  
update-alternatives \--set g++ "/usr/bin/g++-4.8" && \  
update-alternatives \--display gcc && \  
update-alternatives \--display g++  
  
##### root6 package #####  
RUN mkdir /opt/root6 && \  
cd /opt/root6 && \  
wget \--no-check-certificate
https://root.cern.ch/download/root_v6.06.06.source.tar.gz && \  
wget \--no-check-certificate
https://root.cern.ch/download/root_v6.06.06.Linux-
ubuntu14-x86_64-gcc4.8.tar.gz && \  
tar xvzf root_v6.06.06.source.tar.gz && \  
rm -f root_v6.06.06.source.tar.gz && \  
cd root-6.06.06 && \  
./configure && \  
make -j2 && \  
echo 'pathmunge /opt/root6/root-6.06.06/bin after' >>
/etc/profile.d/3_ngspaths.sh  
## update ENV  
ADD ./config/1_thisroot.sh /etc/profile.d/  
  
ENV PATH=/opt/root6/root-6.06.06/bin:$PATH \  
ROOTSYS=/opt/root6/root-6.06.06 \  
LD_LIBRARY_PATH=/opt/root6/root-6.06.06/lib"${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
\  
DYLD_LIBRARY_PATH=/opt/root6/root-6.06.06/lib"${DYLD_LIBRARY_PATH:+:$DYLD_LIBRARY_PATH}"
\  
LIBPATH=/opt/root6/root-6.06.06/lib"${LIBPATH:+:$LIBPATH}" \  
SHLIB_PATH=/opt/root6/root-6.06.06/lib"${SHLIB_PATH:+:$SHLIB_PATH}" \  
PYTHONPATH=/opt/root6/root-6.06.06/lib"${PYTHONPATH:+:$PYTHONPATH}" \  
CMAKE_PREFIX_PATH=/opt/root6/root-6.06.06"${CMAKE_PREFIX_PATH:+:$CMAKE_PREFIX_PATH}"  
##### end root6 install #####  
###### Install SpeedSeq and required utilities ######  
## conda pysam will also install samtools, bcftools and htslib  
## this will override compiled (if any) samtools, bcftools, htslib in PATH  
## Using gcc and g++ v4.8.5  
RUN conda install \--yes -c bioconda pysam=0.9.1 gawk && \  
conda install \--yes numpy scipy && \  
cd /opt && \  
git clone \--recursive https://github.com/hall-lab/speedseq && \  
cd speedseq && \  
rm -f Makefile  
  
# disable CNVnator compilation  
ADD ./config/speedseq_mkfile /opt/speedseq/Makefile  
  
RUN cd /opt/speedseq && \  
make && \  
cat install.log && \  
echo 'pathmunge /opt/speedseq/bin after' >> /etc/profile.d/3_ngspaths.sh && \  
mkdir -p /scratch/annotations/cnvnator_chroms && \  
rm -f /opt/speedseq/bin/speedseq.config  
## UPDATE speedseq config file with valid paths to required tools ##  
ADD ./config/speedseq.config /opt/speedseq/bin/  
#### Install CNVnator ####  
## Using gcc and g++ v4.8.5  
## BUG: binaries differ from one used by speedseq because of updated version  
# cnvnator and cnvnator2VCF.pl binaries are from compiled package while  
# annotate_rd.py and cnvnator_wrapper.py from cnvnator shipped with speedseq  
## CNVnator was compiled successfully but not working with SpeedSeq SV
function  
RUN mkdir /opt/cnvnator && \  
cd /opt/cnvnator && \  
wget \--no-check-certificate
https://github.com/abyzovlab/CNVnator/releases/download/v0.3.2/CNVnator_v0.3.2.zip
&& \  
unzip CNVnator_v0.3.2.zip && \  
cd CNVnator_v0.3.2 && \  
cd src/samtools && \  
make && \  
cd .. && \  
make && \  
ln -s cnvnator cnvnator-multi && \  
echo 'pathmunge /opt/cnvnator/CNVnator_v0.3.2 after' >>
/etc/profile.d/3_ngspaths.sh && \  
echo 'pathmunge /opt/cnvnator/CNVnator_v0.3.2/src after' >>
/etc/profile.d/3_ngspaths.sh  
##################### Install VEP ###########################  
## Using gcc and g++ v4.8.5  
## install perl modules ##  
# http://stackoverflow.com/a/3462743/1243763  
# https://hub.docker.com/r/heuermh/vep/~/dockerfile/  
### Install linuxbrew ###  
RUN cd /opt && \  
git clone https://github.com/Linuxbrew/brew.git /opt/linuxbrew  
## export following using ADD directive: add file containing following to
/etc/profile.d/brewconf.sh  
ADD ./config/2_brewconf.sh /etc/profile.d/  
  
ENV PATH=/opt/linuxbrew/bin:$PATH \  
MANPATH=/opt/linuxbrew/share/man"${MANPATH:+:$MANPATH}" \  
INFOPATH=/opt/linuxbrew/share/info"${INFOPATH:+:$INFOPATH}"  
  
RUN /opt/linuxbrew/bin/brew tap homebrew/science && \  
/opt/linuxbrew/bin/brew install htslib && \  
/opt/linuxbrew/bin/brew tap chapmanb/homebrew-cbl && \  
wget \--no-check-certificate -O - http://cpanmin.us | perl - \--self-upgrade
&& \  
/usr/local/bin/cpanm Archive::Extract CGI DBI Time::HiRes Archive::Tar
Archive::Zip File::Copy::Recursive  
  
RUN /opt/linuxbrew/bin/brew install vep && \  
mkdir -p /scratch/annotations/vep_cache  
## Pending: link VEP to speedsed; set cache dir, download annotations  
###################################################  
##### IMPORTANT: LICENSE RESTRICTION #####  
## Following can not be containerized as they require individual licenses. Use
volume mount during docker run.  
RUN mkdir -p /opt/gatk && \  
mkdir -p /opt/mutect && \  
mkdir -p /scratch/bundle && \  
chgrp -R glass /scratch && \  
chmod -R 775 /scratch  
# Cleanup  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# set workdir to /scratch where pipeline code will be cloned  
# This requires proper volume mount while running docker run -v flag to allow
docker container to see code directory.  
WORKDIR /scratch  
  
ENV PATH
/opt/root6/root-6.06.06/bin:/opt/miniconda/bin:/opt/linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-8-oracle/bin:/usr/lib/jvm/java-8-oracle/db/bin:/usr/lib/jvm/java-8-oracle/jre/bin:/opt/samtools/samtools/bin:/opt/samtools/bcftools/bin:/opt/samtools/htslib/bin:/opt/bwa:/opt/bedtools2/bin:/opt/picard/default:/opt/bamtools/bin:/opt/bin:/opt/speedseq/bin:/opt/cnvnator/CNVnator_v0.3.2:/opt/cnvnator/CNVnator_v0.3.2/src:/usr/local/gemini/bin  
  
ENTRYPOINT []  
CMD []  
  
## END ##  

