################################################################################################  
# This is the Dockerfile for the LIFE708 teaching materials  
################################################################################################  
# Base image  
FROM ubuntu:14.04  
  
# Maintainer  
MAINTAINER Will Rowe <will.rowe@liverpool.ac.uk>  
  
  
################################################################################################  
# Install core packages  
################################################################################################  
RUN apt-get update && apt-get install -y \  
curl \  
cmake \  
dh-autoreconf \  
git \  
libhdf5-serial-dev \  
zlib1g-dev \  
libncurses5-dev \  
libncursesw5-dev \  
libbz2-dev \  
liblzma-dev \  
make \  
nano \  
unzip \  
vim \  
wget \  
\--force-yes && \  
apt-get autoclean && \  
apt-get autoremove -y  
  
  
################################################################################################  
# Install Java, Python (2 \+ 3) and BioPython  
################################################################################################  
RUN apt-get install -y \  
default-jre \  
python2.7 \  
python3 \  
python-dev \  
python-pip \  
python3-pip \  
python-virtualenv \  
python-numpy \  
python-matplotlib \  
python-biopython=1.63-1  
  
  
################################################################################################  
# Install Assembly Statistics  
################################################################################################  
RUN cd /opt && \  
git clone https://github.com/sanger-pathogens/assembly-stats && \  
mkdir assembly-stats/build && \  
cd assembly-stats/build && \  
cmake .. && \  
make && \  
make install  
  
  
################################################################################################  
# Install Freebayes  
################################################################################################  
RUN cd /opt && \  
git clone --recursive git://github.com/ekg/freebayes.git && \  
cd freebayes && \  
make && \  
make install  
  
################################################################################################  
# Install NCBI-blast  
################################################################################################  
RUN cd /opt && \  
wget --no-check-certificate
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz && \  
tar -xvf ncbi-blast-2.6.0+-x64-linux.tar.gz && \  
ln -s /opt/ncbi-blast-2.6.0+/bin/* /usr/local/bin/ && \  
rm -rf ncbi-blast-2.6.0+-x64-linux.tar.gz  
  
  
################################################################################################  
# Install Prokka and dependencies  
################################################################################################  
RUN cd /opt && \  
apt-get install -y libdatetime-perl libxml-simple-perl libdigest-md5-perl
bioperl && \  
git clone git://github.com/tseemann/prokka.git && \  
prokka/bin/prokka --setupdb && \  
ln -s /opt/prokka/bin/* /usr/local/bin/ && \  
apt-get autoclean && \  
apt-get autoremove -y && \  
ln -s /usr/bin/perl /usr/local/bin/perl && \  
wget
ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux64.tbl2asn.gz
&& \  
gunzip linux64.tbl2asn.gz && \  
chmod a+rwx linux64.tbl2asn && \  
ln -s /opt/linux64.tbl2asn /usr/local/bin/tbl2asn  
  
  
################################################################################################  
# Install PAGIT (removed for variation workshop)  
################################################################################################  
#RUN cd /opt && \  
# mkdir PAGIT-install && \  
# cd PAGIT-install && \  
# wget ftp://ftp.sanger.ac.uk/pub/resources/software/pagit/PAGIT.V1.64bit.tgz
&& \  
# tar -xvf PAGIT.V1.64bit.tgz && \  
# bash ./installme.sh  
  
  
################################################################################################  
# Install Samtools, BCFtools and HTSlib (versions 1.4)  
################################################################################################  
RUN cd /opt && \  
wget --no-check-certificate
https://github.com/samtools/samtools/releases/download/1.4/samtools-1.4.tar.bz2
&& \  
wget --no-check-certificate
https://github.com/samtools/bcftools/releases/download/1.4/bcftools-1.4.tar.bz2
&& \  
tar -xvf samtools-1.4.tar.bz2 && \  
tar -xvf bcftools-1.4.tar.bz2 && \  
cd samtools-1.4 && \  
./configure && make && make install && cd htslib-1.4 && make && make install
&& \  
cd /opt/bcftools-1.4 && \  
make && make install && cd .. && \  
rm /opt/*.bz2  
  
  
################################################################################################  
# Install BWA  
################################################################################################  
RUN cd /opt && \  
git clone https://github.com/lh3/bwa.git && \  
cd bwa && make && \  
ln -s /opt/bwa/bwa /usr/local/bin/bwa  
  
  
################################################################################################  
# Install Seqtk  
################################################################################################  
RUN cd /opt && \  
git clone https://github.com/lh3/seqtk.git && \  
cd seqtk && \  
make && \  
ln -s /opt/seqtk/seqtk /usr/local/bin/seqtk  
  
  
################################################################################################  
# Install SMALT and dependencies  
################################################################################################  
RUN cd /opt && \  
wget
http://downloads.sourceforge.net/project/mummer/mummer/3.23/MUMmer3.23.tar.gz
&& \  
tar -zxf MUMmer3.23.tar.gz && \  
cd MUMmer3.23 && \  
make && \  
mkdir bin && \  
mv annotate combineMUMs delta-filter dnadiff exact-tandems gaps m* n* p* r*
sh* ./bin && \  
ln -s /opt/MUMmer3.23/bin/* /usr/local/bin/ && \  
cd .. && \  
for x in `find MUMmer3.23/ -maxdepth 1 -executable -type f`; do cp -s $x . ;
done && \  
rm -rf MUMmer3.23.tar.gz && \  
wget http://downloads.sourceforge.net/project/smalt/smalt-0.7.6-bin.tar.gz &&
\  
tar -zxf smalt-0.7.6-bin.tar.gz && \  
cp smalt-0.7.6-bin/smalt_x86_64 /usr/local/bin/smalt && \  
rm -rf smalt-0.7.6-bin.tar.gz && \  
apt-get autoclean && \  
apt-get autoremove -y  
  
  
################################################################################################  
# Install SPAdes  
################################################################################################  
RUN cd /opt && \  
wget --no-check-certificate
http://cab.spbu.ru/files/release3.9.1/SPAdes-3.9.1-Linux.tar.gz && \  
tar -xvf SPAdes-3.9.1-Linux.tar.gz && \  
ln -s /opt/SPAdes-3.9.1-Linux/bin/* /usr/local/bin/ && \  
rm -rf SPAdes-3.9.1-Linux.tar.gz  
  
  
################################################################################################  
# Install SRAtoolkit  
################################################################################################  
RUN cd /opt && \  
wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-
ubuntu64.tar.gz && \  
tar -xvf sratoolkit.current-ubuntu64.tar.gz && rm sratoolkit.current-
ubuntu64.tar.gz && \  
ln -s /opt/sratoolkit.*/bin/* /usr/local/bin/ && \  
wget http://downloads.sourceforge.net/project/abacas/abacas.1.3.1.pl && \  
awk 'BEGIN{print "#!/usr/bin/env perl"; getline} {print}' abacas.1.3.1.pl >
abacas.pl && \  
chmod 755 abacas.pl && \  
mv abacas.pl /usr/local/bin/  
  
  
################################################################################################  
# Install additional software using apt-get  
################################################################################################  
RUN apt-get install -y \  
bedtools=2.17.0-1 \  
bowtie2=2.1.0-2 \  
cd-hit=4.6.1-2012-08-27-2 \  
fastqc=0.10.1+dfsg-2 \  
fastx-toolkit=0.0.14-1 \  
HMMER=3.1b1-3 \  
velvet \  
\--force-yes && \  
apt-get autoclean && \  
apt-get autoremove -y  
  
  
################################################################################################  
# Clone the github repo, add any python/shell scripts, create bash profile,
clean cache and expose port  
################################################################################################  
RUN cd /opt && \  
git clone https://github.com/will-rowe/LIFE708.git && \  
mkdir /opt/scripts && \  
find /opt/LIFE708/scripts/ -type f -name '*.py' -exec cp {} /opt/scripts/ \;
&& \  
find /opt/LIFE708/scripts/ -type f -name '*.sh' -exec cp {} /opt/scripts/ \;
&& \  
wget
https://raw.githubusercontent.com/dzerbino/velvet/master/contrib/shuffleSequences_fasta/shuffleSequences_fasta.pl
-O /opt/scripts/shuffleSequences_fasta.pl && \  
chmod a+rwx /opt/scripts/* && \  
ln -s /opt/scripts/* /usr/local/bin/ && \  
cp /opt/LIFE708/bashrc ~/.bashrc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
#open ports private only  
EXPOSE 8080  
  
################################################################################################  
# Define working directory and define default command for container launch  
################################################################################################  
RUN mkdir /MOUNTED-VOLUME-LIFE708 && chmod a+rwx /MOUNTED-VOLUME-LIFE708  
WORKDIR /MOUNTED-VOLUME-LIFE708  
CMD ["bash"]  

