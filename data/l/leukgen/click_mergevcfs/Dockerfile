# Use base image  
FROM ubuntu:14.04  
# Define directories  
ENV OUTPUT_DIR /data  
ENV WORK_DIR /code  
ENV OPT_DIR /opt  
  
# Mount the output volume as persistant  
VOLUME ${OUTPUT_DIR}  
  
# Create /ifs volume for MSK users  
VOLUME /ifs  
  
RUN \  
# Install Packages Dependencies  
apt-get update -yqq && \  
apt-get install -yqq \  
zlib1g-dev \  
liblzma-dev \  
libbz2-dev \  
libncurses5-dev \  
libcurl4-openssl-dev \  
bioperl \  
samtools \  
python-dev \  
pkg-config \  
perl \  
curl \  
git \  
locales \  
python-pip \  
wget \  
vim && \  
apt-get clean && \  
\  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.utf8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Install HTSlib  
RUN \  
cd /tmp && \  
wget
"https://github.com/samtools/htslib/releases/download/1.8/htslib-1.8.tar.bz2"
&& \  
tar -vxjf htslib-1.8.tar.bz2 && \  
cd htslib-1.8 && \  
./configure --disable-bz2 --disable-lzma && \  
make && \  
make install  
  
# Install vcftools  
RUN \  
cd /tmp && \  
wget
"https://github.com/vcftools/vcftools/releases/download/v0.1.15/vcftools-0.1.15.tar.gz"
&& \  
tar -xvzf vcftools-0.1.15.tar.gz && \  
cd vcftools-0.1.15 && \  
./configure && \  
make && \  
make install  
  
# Install cgpVcf  
RUN \  
cd /home && \  
wget "https://github.com/cancerit/cgpVcf/archive/v2.0.4.tar.gz" && \  
tar -xvzf v2.0.4.tar.gz && \  
cd cgpVcf-2.0.4 && \  
sed -i 's/make test/ /g' setup.sh && \  
./setup.sh /opt/  
  
# Update perl Build  
RUN \  
cd /home && \  
wget "http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/Module-
Build-0.4224.tar.gz" && \  
tar -xvzf Module-Build-0.4224.tar.gz && \  
cd Module-Build-0.4224 && \  
perl Build.PL && \  
./Build && \  
./Build install  
  
# Install BIO::DB:HTS-2.10  
RUN \  
cd /home && \  
wget "http://search.cpan.org/CPAN/authors/id/A/AV/AVULLO/Bio-DB-
HTS-2.10.tar.gz" && \  
tar -xvzf Bio-DB-HTS-2.10.tar.gz && \  
cd Bio-DB-HTS-2.10 && \  
perl Build.PL --htslib /tmp/htslib-1.8 && \  
./Build && \  
./Build install && \  
export PERL5LIB=$PERL5LIB:/home/Bio-DB-HTS-2.10/lib/Bio/DB/HTS/  
  
# Install cgpCaVEManPostProcessing  
RUN \  
cd /home && \  
wget
"https://github.com/cancerit/cgpCaVEManPostProcessing/archive/1.8.0.tar.gz" &&
\  
tar -xvzf 1.8.0.tar.gz && \  
cd cgpCaVEManPostProcessing-1.8.0 && \  
perl /opt/bin/cpanm -v --mirror http://cpan.metacpan.org -l /opt/
--installdeps . && \  
PERLROOT=/opt/lib/perl5 && \  
export PERL5LIB="$PERLROOT" && \  
export PATH="/opt/bin:$PATH" && \  
perl Makefile.PL INSTALL_BASE=/opt/ && \  
make && \  
make install && \  
export PERL5LIB=$PERL5LIB:/home/cgpCaVEManPostProcessing/lib  
  
# Install Tabix  
RUN \  
cd home && \  
git clone https://github.com/samtools/tabix.git && \  
cd tabix/ && \  
make && \  
cd perl && \  
perl Makefile.PL && \  
make && \  
make install && \  
export PERL5LIB=$PERL5LIB:/home/tabix/perl/  
  
# PERL5LIB  
ENV PERL5LIB /opt/lib/perl5/  
  
# PATH  
ENV PATH "$PATH:/opt/bin"  
# Environment variables needed for external installation of pysam  
ENV HTSLIB_LIBRARY_DIR /usr/local/lib  
ENV HTSLIB_INCLUDE_DIR /usr/local/include  
  
# Set LD_LIBRARY_PATH for correct location to libhts.* in singularity image  
ENV LD_LIBRARY_PATH "$LD_LIBRARY_PATH:/usr/local/lib/"  
# Install click_mergevcfs  
COPY . ${WORK_DIR}  
WORKDIR ${WORK_DIR}  
RUN \  
pip install --upgrade setuptools && \  
pip install --editable .  
  
# move libhts.* to the correct pysam directory  
RUN \  
mv /usr/local/lib/libhts.* /usr/local/lib/python2.7/dist-packages/pysam  
  
# Run command  
ENTRYPOINT ["click_mergevcfs"]  

