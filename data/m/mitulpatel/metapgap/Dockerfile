FROM ubuntu:14.04  
  
FROM bioperl/bioperl-deps  
  
#FROM r-base  
  
MAINTAINER Mitul Patel <mitul428@gmail.com>  
  
LABEL version="v1.0"  
  
RUN mkdir metaPGAP  
RUN cd metaPGAP  
RUN mkdir binaries  
  
# Update the repository sources list  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer && \  
apt-get clean  
  
# Install R  
RUN apt-get -y install r-base  
  
# Install python  
RUN apt-get install --yes \  
python3  
  
# Install BioPython  
RUN apt-get install --yes \  
python-biopython=1.63-1 \  
python-biopython-sql=1.63-1  
  
# Install pip  
RUN apt-get install --yes \  
python-pip  
  
RUN cpanm -v \  
https://github.com/bioperl/bioperl-live/archive/master.tar.gz  
  
# Install compiler and perl stuff  
RUN apt-get install --yes \  
build-essential \  
gcc-multilib \  
apt-utils \  
perl \  
expat \  
libexpat-dev  
  
# Install BioPerl dependancies, mostly from cpan  
RUN apt-get install --yes \  
libpixman-1-0 \  
libpixman-1-dev \  
graphviz \  
libxml-parser-perl \  
libsoap-lite-perl  
  
RUN cpanm Test::Most \  
Algorithm::Munkres \  
Array::Compare Clone \  
PostScript::TextBlock \  
SVG \  
SVG::Graph \  
Set::Scalar \  
Sort::Naturally \  
Graph \  
GraphViz \  
HTML::TableExtract \  
Convert::Binary::C \  
Math::Random \  
Error \  
Spreadsheet::ParseExcel \  
XML::Parser::PerlSAX \  
XML::SAX::Writer \  
XML::Twig XML::Writer  
  
  
# Install software  
RUN apt-get install -y git && \  
apt-get install -y wget && \  
apt-get install -y zip && \  
apt-get install -y gzip && \  
apt-get install -y alien  
  
# Install RaXML  
RUN cd binaries && \  
wget https://github.com/stamatak/standard-RAxML/archive/master.zip && \  
unzip master.zip && \  
rm master.zip && \  
cd standard-RAxML-master && \  
make -f Makefile.gcc && \  
rm *.o && \  
cd ../  
  
# Install get_homologues  
RUN cd binaries && \  
wget https://github.com/eead-csic-
compbio/get_homologues/releases/download/v2.0.22/get_homologues-x86_64-20161027.tgz
&& \  
tar -zxvpf get_homologues-x86_64-20161027.tgz && \  
cd ../  
  
RUN apt-get install -y inkscape  
  
#install Prokka  
RUN cd binaries && \  
wget http://www.vicbioinformatics.com/prokka-1.11.tar.gz && \  
apt-get install -y libdatetime-perl libxml-simple-perl libdigest-md5-perl && \  
tar -zxvf prokka-1.11.tar.gz && \  
sed 's/$MAXCONTIGIDLEN = 20;/$MAXCONTIGIDLEN = 50;/1' prokka-1.11/bin/prokka >
prokka-1.11/bin/prokka-new && \  
mv prokka-1.11/bin/prokka-new prokka-1.11/bin/prokka && \  
chmod 755 prokka-1.11/bin/prokka && \  
wget
ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux.tbl2asn.gz
&& \  
gunzip linux.tbl2asn.gz && \  
mv linux.tbl2asn prokka-1.11/binaries/linux/tbl2asn && \  
chmod 755 prokka-1.11/binaries/linux/tbl2asn && \  
prokka-1.11/bin/prokka --setupdb && \  
cd ../  
  
# Install MAFFT  
RUN cd binaries && \  
wget -q http://mafft.cbrc.jp/alignment/software/mafft-7.130-with-extensions-
src.tgz -O- \  
| tar xz && \  
cd mafft-7.130-with-extensions/core && \  
#sed 's/\/usr\/local/\/metaPGAP\/binaries\/mafft-7.130-with-extensions/1'
Makefile > Makefile-new && \  
#mv Makefile-new Makefile && \  
make clean && make && make install && \  
cd ../extensions && \  
make clean && make && make install && \  
cd ../../  
  
# Install Clustal Omega  
RUN cd binaries && \  
wget http://www.clustal.org/omega/clustalo-1.2.3-Ubuntu-x86_64 && \  
mv clustalo-1.2.3-Ubuntu-x86_64 clustao && \  
chmod 755 clustao && \  
cd ../  
  
# Install AMAS  
RUN cd binaries && \  
wget https://github.com/marekborowiec/AMAS/archive/master.zip && \  
unzip master.zip && \  
mv AMAS-master AMAS && \  
rm master.zip && \  
cd ../  
  
# Installing NewickTools  
RUN cd binaries && \  
#mkdir newick-utils-1.6 && \  
wget http://cegg.unige.ch/pub/newick-utils-1.6-Linux-x86_64-disabled-
extra.tar.gz && \  
tar -xzvf newick-utils-1.6-Linux-x86_64-disabled-extra.tar.gz && pwd && \  
newick-utils-1.6/configure --prefix=/binaries/newick-utils-1.6 && make && make
install && \  
cd ../  
  
# Installing metaPGAP  
RUN cd binaries && \  
wget https://github.com/mitul-patel/docker-metapgap/archive/master.zip && \  
unzip master.zip && \  
mv docker-metapgap-master docker-metaPGAP && \  
rm master.zip && \  
cd ../  
  
ENV PATH /binaries/prokka-1.11/bin:$PATH  
ENV PATH /metaPGAP/binaries/get_homologues-x86_64-20161027:$PATH  
ENV PATH /binaries/mafft-7.130-with-extensions/bin:$PATH  
ENV PATH /binaries/AMAS/amas:$PATH  
ENV PATH /binaries/standard-RAxML-master:$PATH  
ENV PATH /binaries/newick-utils-1.6/bin:$PATH  
ENV PATH /binaries/docker-metaPGAP:$PATH  
ENV PATH /usr/local/bin:$PATH  
  
RUN chmod -R 770 /metaPGAP  
  
CMD ["python", "/binaries/docker-metaPGAP/metaPGAP.py"]  
  

