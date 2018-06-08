FROM python:2.7.14  
# debian 8.9  
  
MAINTAINER aokad <aokad@hgc.jp>  
  
RUN echo "deb http://deb.debian.org/debian stretch main" >
/etc/apt/sources.list && \  
echo "deb http://deb.debian.org/debian stretch-updates main" >>
/etc/apt/sources.list && \  
echo "deb http://security.debian.org stretch/updates main" >>
/etc/apt/sources.list && \  
apt-get -y update && \  
apt-get install -y dpkg-dev gcc g++ libc6-dev make patch tar unzip && \  
apt-get install -y zlib1g-dev g++ dh-autoreconf libncurses-dev pkg-config
libgd2-xpm-dev && \  
\  
mkdir -p /tools && \  
\  
cd /tools && \  
echo "build samtools-1.2" && \  
wget -nc
https://sourceforge.net/projects/samtools/files/samtools/1.2/samtools-1.2.tar.bz2
&& \  
tar xjvf samtools-1.2.tar.bz2 && \  
rm -f samtools-1.2.tar.bz2 && \  
cd samtools-1.2 && \  
make && \  
make install && \  
\  
cd /tools && \  
echo "build bedtools-2.24.0" && \  
wget -nc https://github.com/arq5x/bedtools2/archive/v2.24.0.tar.gz && \  
tar xzvf v2.24.0.tar.gz && \  
rm -f v2.24.0.tar.gz && \  
cd bedtools2-2.24.0 && \  
make && \  
make install && \  
\  
pip install pandas && \  
\  
mkdir -p /tools && \  
\  
cd /tools && \  
wget http://www.cpan.org/src/5.0/perl-5.14.4.tar.gz && \  
tar -xzf perl-5.14.4.tar.gz && \  
cd perl-5.14.4 && \  
./Configure -des -Dprefix=/usr/local/ -Dusethreads && \  
make && \  
make install && \  
\  
cd /tools && \  
wget -nc https://github.com/ICGC-TCGA-PanCancer/PCAP-
core/archive/v1.8.1.tar.gz && \  
tar xzvf v1.8.1.tar.gz && \  
rm v1.8.1.tar.gz && \  
cd PCAP-core-1.8.1 && \  
grep -l -r '/usr/bin/perl' * | xargs sed -i.bak -e
's;/usr/bin/perl;/usr/local/bin/perl;g' && \  
cpan -f JSON && \  
bash setup.sh /tools/ICGC && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/GenomonQC/archive/v2.0.2a.zip && \  
unzip v2.0.2a.zip && \  
rm -f v2.0.2a.zip && \  
cd GenomonQC-2.0.2a && \  
python setup.py install  
  
CMD ["/bin/bash"]  

