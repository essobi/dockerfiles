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
\  
mkdir -p /tools && \  
\  
cd /tools && \  
echo "build BLAT v.34" && \  
wget http://hgdownload.soe.ucsc.edu/admin/exe/userApps.v349.src.tgz && \  
tar -xzvf userApps.v349.src.tgz && \  
rm -f userApps.v349.src.tgz && \  
cd userApps && \  
make && \  
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
cd /tools && \  
echo "build libmaus-0.0.196" && \  
wget
https://github.com/gt1/libmaus/archive/0.0.196-release-20150326095654.tar.gz
&& \  
tar xzvf 0.0.196-release-20150326095654.tar.gz && \  
rm -f 0.0.196-release-20150326095654.tar.gz && \  
cd libmaus-0.0.196-release-20150326095654 && \  
autoreconf -i -f && \  
./configure && \  
make && \  
make install && \  
\  
cd /tools && \  
echo "build biobambam-0.0.191" && \  
wget -nc
https://github.com/gt1/biobambam/archive/0.0.191-release-20150401083643.tar.gz
&& \  
tar xzvf 0.0.191-release-20150401083643.tar.gz && \  
rm -f 0.0.191-release-20150401083643.tar.gz && \  
cd biobambam-0.0.191-release-20150401083643 && \  
autoreconf -i -f && \  
./configure && \  
make && \  
make install && \  
\  
cd /tools && \  
echo "build htslib-1.3" && \  
wget -nc
https://sourceforge.net/projects/samtools/files/samtools/1.3/htslib-1.3.tar.bz2
&& \  
tar xvf htslib-1.3.tar.bz2 && \  
rm -f htslib-1.3.tar.bz2 && \  
cd htslib-1.3 && \  
make && \  
make install  
  
  
# python package  
RUN pip install Cython && \  
pip install pysam && \  
pip install numpy && \  
pip install scipy && \  
pip install primer3-py && \  
pip install pyVCF && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-
Project/GenomonMutationFilter/archive/v0.2.1.zip && \  
unzip v0.2.1.zip && \  
rm -f v0.2.1.zip && \  
cd GenomonMutationFilter-0.2.1 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/EBFilter/archive/v0.2.1.zip && \  
unzip v0.2.1.zip && \  
rm -f v0.2.1.zip && \  
cd EBFilter-0.2.1 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/GenomonFisher/archive/v0.2.0.zip
&& \  
unzip v0.2.0.zip && \  
rm -f v0.2.0.zip && \  
cd GenomonFisher-0.2.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-
Project/GenomonMutationAnnotator/archive/v0.1.0.zip && \  
unzip v0.1.0.zip && \  
rm -f v0.1.0.zip && \  
cd GenomonMutationAnnotator-0.1.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/ken0-1n/mutation_util/archive/v0.5.0.zip && \  
unzip v0.5.0.zip && \  
rm -f v0.5.0.zip && \  
cd mutation_util-0.5.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/ken0-1n/GenomonHotspotCall/archive/v0.1.0.zip && \  
unzip v0.1.0.zip && \  
rm -f v0.1.0.zip && \  
cd GenomonHotspotCall-0.1.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/friend1ws/annot_utils/archive/v0.1.0.zip && \  
unzip v0.1.0.zip && \  
rm -f v0.1.0.zip && \  
cd annot_utils-0.1.0 && \  
python setup.py install && \  
cd resource && \  
bash prep_data.sh && \  
mv /tools/annot_utils-0.1.0/lib/annot_utils/data/hg19/*
/usr/local/lib/python2.7/site-packages/annot_utils/data/hg19/ && \  
mv /tools/annot_utils-0.1.0/lib/annot_utils/data/hg38/*
/usr/local/lib/python2.7/site-packages/annot_utils/data/hg38/ && \  
mv /tools/annot_utils-0.1.0/lib/annot_utils/data/mm10/*
/usr/local/lib/python2.7/site-packages/annot_utils/data/mm10/ && \  
\  
cd /tools && \  
wget -nc https://github.com/friend1ws/fusion_utils/archive/v0.2.0.zip && \  
unzip v0.2.0.zip && \  
rm -f v0.2.0.zip && \  
cd fusion_utils-0.2.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/friend1ws/chimera_utils/archive/v0.3.0.zip && \  
unzip v0.3.0.zip && \  
rm -f v0.3.0.zip && \  
cd chimera_utils-0.3.0 && \  
python setup.py install && \  
\  
echo "export LD_LIBRARY_PATH=/usr/local/lib" >> /root/.bashrc  
  
CMD ["/bin/bash"]  

