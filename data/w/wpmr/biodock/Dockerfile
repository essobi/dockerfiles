################################################################################################  
# This is the Dockerfile for running bioinformatic analyses at the Hinton Lab
(IIB).  
################################################################################################  
FROM ubuntu:14.04  
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
make \  
nano \  
unzip \  
wget \  
\--force-yes  
  
  
################################################################################################  
# Install Java, Python (2 \+ 3) and BioPython  
################################################################################################  
RUN apt-get install -y \  
default-jre \  
python2.7 python3 python-dev python-pip python-virtualenv python-numpy python-
matplotlib \  
python-biopython=1.63-1  
  
  
################################################################################################  
# Install Cutadapt, HTSeq and PySam using pip  
################################################################################################  
RUN pip install --install-option="--prefix=/usr" cutadapt==1.10  
RUN pip install --install-option="--prefix=/usr" HTSeq==0.6.1  
RUN pip install pysam==0.9.0  
  
  
  
################################################################################################  
# Install Kallisto  
################################################################################################  
RUN git clone git://github.com/pachterlab/kallisto.git && \  
cd kallisto && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .. && \  
make && \  
make install && \  
cd / && \  
rm -rf /kallisto  
  
  
################################################################################################  
# Install Kraken (no DB included)  
################################################################################################  
RUN cd /opt && \  
git clone git://github.com/DerrickWood/kraken && \  
cd kraken && \  
./install_kraken.sh ./ && \  
ln -s /opt/kraken/krake* /usr/bin/ && \  
cd /  
  
  
################################################################################################  
# Install NGSutils  
################################################################################################  
RUN cd /opt && \  
git clone git://github.com/ngsutils/ngsutils.git && \  
cd ngsutils && \  
make && \  
ln -s /opt/ngsutils/bin/* /usr/bin/ && \  
cd /  
  
  
################################################################################################  
# Install Prodigal  
################################################################################################  
RUN cd /opt && \  
wget --no-check-certificate
https://prodigal.googlecode.com/files/Prodigal-2.60.tar.gz && \  
tar -xvf Prodigal-2.60.tar.gz && \  
cd Prodigal-2.60 && \  
make && \  
ln -s /opt/Prodigal-2.60/prodigal /usr/bin/prodigal && \  
cd / && \  
rm -rf /opt/Prodigal-2.60.tar.gz  
  
  
################################################################################################  
# Install Prokka and dependencies  
################################################################################################  
RUN cd /opt && \  
apt-get install -y libdatetime-perl libxml-simple-perl libdigest-md5-perl
bioperl && \  
git clone git://github.com/tseemann/prokka.git && \  
prokka/bin/prokka --setupdb && \  
ln -s /opt/prokka/bin/* /usr/bin/ && \  
cd /  
  
  
################################################################################################  
# Install R, Bioconductor, R packages and dependencies  
################################################################################################  
RUN apt-get install -y \  
r-base \  
libxml2-dev \  
libcurl4-openssl-dev  
RUN cd /opt && \  
RREPO='"http://cran.rstudio.com/"' && \  
printf "install.packages(\"ggplot2\",
repo=$RREPO)\ninstall.packages(\"reshape\",repo=$RREPO)\ninstall.packages(\"gplots\",repo=$RREPO)\ninstall.packages(\"optparse\",repo=$RREPO)\ninstall.packages(\"XML\",repo=$RREPO)\ninstall.packages(\"getopt\",repo=$RREPO)"
> dep.R && \  
Rscript dep.R && \  
rm dep.R && \  
R -e 'source("http://bioconductor.org/biocLite.R"); biocLite();
biocLite(c("NOISeq", "Repitools", "Rsamtools", "rtracklayer"))' && \  
cd /  
  
  
################################################################################################  
# Install Roary and dependencies  
################################################################################################  
RUN apt-get install -y \  
cpanminus=1.7001-1 \  
fasttree=2.1.7-1 \  
mafft=7.123-1 \  
mcl=1:12-135-2 \  
parallel=20130922-1 \  
prank=0.0.140110-1 && \  
cpanm -f Bio::Roary  
  
  
################################################################################################  
# Install Segemehl and dependencies  
################################################################################################  
RUN cd /opt && \  
apt-get install -y lib32ncurses5-dev && \  
wget http://www.bioinf.uni-leipzig.de/Software/segemehl/segemehl_0_2_0.tar.gz
&& \  
tar -xvf segemehl_0_2_0.tar.gz && \  
cd segemehl_0_2_0/segemehl && \  
make && \  
ln -s /opt/segemehl_0_2_0/segemehl/segemehl.x /usr/bin/ && \  
cd / &&\  
rm -rf /opt/segemehl_0_2_0.tar.gz  
  
  
################################################################################################  
# Install SMALT and dependencies  
################################################################################################  
RUN cd /opt && \  
apt-get install -y python3-pip zlib1g-dev libncurses5-dev libncursesw5-dev &&
\  
wget
http://downloads.sourceforge.net/project/mummer/mummer/3.23/MUMmer3.23.tar.gz
&& \  
tar -zxf MUMmer3.23.tar.gz && \  
cd MUMmer3.23 && \  
make && \  
mkdir bin && \  
mv annotate combineMUMs delta-filter dnadiff exact-tandems gaps m* n* p* r*
sh* ./bin && \  
ln -s /opt/MUMmer3.23/bin/* /usr/bin/ && \  
cd .. && \  
for x in `find MUMmer3.23/ -maxdepth 1 -executable -type f`; do cp -s $x . ;
done && \  
rm -rf MUMmer3.23.tar.gz && \  
wget http://downloads.sourceforge.net/project/smalt/smalt-0.7.6-bin.tar.gz &&
\  
tar -zxf smalt-0.7.6-bin.tar.gz && \  
cp smalt-0.7.6-bin/smalt_x86_64 /usr/bin/smalt && \  
rm -rf smalt-0.7.6-bin.tar.gz && \  
cd /  
  
  
################################################################################################  
# Install UCSC tools  
################################################################################################  
RUN cd /usr/bin && \  
wget --no-check-certificate
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/wigToBigWig && \  
wget --no-check-certificate
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/bigWigToBedGraph &&
\  
wget --no-check-certificate
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/bedGraphToBigWig &&
\  
chmod a+rwx wigToBigWig bigWigToBedGraph bedGraphToBigWig && \  
cd /  
  
  
################################################################################################  
# Install Velvet  
################################################################################################  
RUN cd /opt && \  
git clone git://github.com/dzerbino/velvet && \  
cd velvet && \  
make color && \  
ln -s /opt/velvet/velvet* /usr/bin/ && \  
cd /  
  
  
################################################################################################  
# Install VSearch  
################################################################################################  
RUN cd /opt && \  
git clone git://github.com/torognes/vsearch && \  
cd vsearch && \  
./autogen.sh && \  
./configure && \  
automake && \  
make && \  
make install && \  
cp ./bin/vsearch /usr/bin/ && \  
cd / && \  
rm -rf /opt/vsearch  
  
  
################################################################################################  
# Install additional software using apt-get  
################################################################################################  
RUN apt-get install -y \  
bedtools=2.17.0-1 \  
ncbi-blast+=2.2.28-2 \  
bowtie2=2.1.0-2 \  
bwa=0.7.5a-2 \  
cd-hit=4.6.1-2012-08-27-2 \  
fastqc=0.10.1+dfsg-2 \  
fastx-toolkit=0.0.14-1 \  
HMMER=3.1b1-3 \  
samtools=0.1.19-1 \  
\--force-yes  
  
  
################################################################################################  
# Clone lab gitlab project, install scripts, create bash profile and clean
cache  
################################################################################################  
RUN cd /opt && \  
git clone https://gitlab.com/will_rowe/biodock.git && \  
mkdir /opt/SCRIPT_bin && \  
find /opt/biodock/00_SCRIPTS/ -type f -name '*.py' -exec cp {}
/opt/SCRIPT_bin/ \; && \  
find /opt/biodock/00_SCRIPTS/ -type f -name '*.pl' -exec cp {}
/opt/SCRIPT_bin/ \; && \  
find /opt/biodock/00_SCRIPTS/ -type f -name '*.sh' -exec cp {}
/opt/SCRIPT_bin/ \; && \  
ln -s /opt/SCRIPT_bin/* /usr/bin/ && \  
cp /opt/biodock/bashrc ~/.bashrc && \  
rm -rf /var/lib/apt/lists/*  
  
  
################################################################################################  
# Define working directory and define default command for container launch  
################################################################################################  
RUN mkdir /SCRATCH  
WORKDIR /SCRATCH  
CMD ["bash"]  

