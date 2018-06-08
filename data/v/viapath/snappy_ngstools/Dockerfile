# NGS tools (BAM and BED handling)  
FROM viapath/snappy_base:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
  
# htslib/samtools/bcftools 1.3.1  
RUN cd /tmp && \  
git clone \--recursive https://github.com/samtools/htslib.git && \  
cd htslib && git checkout 1.3.1 && \  
make && make install && \  
cd /tmp && \  
git clone \--recursive https://github.com/samtools/samtools.git && \  
cd samtools && git checkout 1.3.1 && \  
make && make install && \  
cd /tmp && \  
git clone \--recursive https://github.com/samtools/bcftools.git && \  
cd bcftools && git checkout e3ef8dabc4450cd7adbaaafb86840ebbf109ab98 && \  
make && make install && \  
cd /tmp && rm -rf /tmp/*  
  
# install python modules for samtools (pysam)  
RUN pip install pysam==0.8.3  
  
# bedtools  
RUN cd /tmp && \  
git clone https://github.com/arq5x/bedtools2.git && \  
cd bedtools2 && \  
git checkout v2.24.0 && \  
make clean && \  
make all && \  
chmod +x bin/bedtools && \  
mv bin/bedtools /usr/local/bin/ && \  
cd .. && \  
rm -rf /tmp/bedtools2  
  
# vcflib  
RUN cd /tmp && \  
git clone \--recursive https://github.com/ekg/vcflib.git && \  
cd vcflib && \  
git checkout 7f1575e24f0d603a69aa4938ae4ed07dd074e9f0 && \  
git submodule update --init --recursive && \  
make && \  
mv bin /usr/local/pipeline/vcflib && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/vcflib' /home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/vcflib && \  
chown -R snappy:snappy /usr/local/pipeline && \  
ln -s /usr/local/pipeline/vcflib/* /usr/local/bin/ && \  
rm -rvf /tmp/*  
  
# gVCFtools  
RUN cd /tmp && \  
git clone \--recursive https://github.com/sequencing/gvcftools.git && \  
cd gvcftools && \  
git checkout v0.16 && \  
make && \  
mv bin /usr/local/pipeline/gvcftools && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/gvcftools' /home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/gvcftools && \  
chown -R snappy:snappy /usr/local/pipeline && \  
ln -s /usr/local/pipeline/gvcftools/* /usr/local/bin/ && \  
rm -rvf /tmp/*  
  
# VT  
RUN cd tmp && \  
git clone \--recursive https://github.com/atks/vt.git && \  
cd vt && \  
git checkout 0.57 && \  
git submodule update --recursive && \  
make && \  
mkdir -p /usr/local/pipeline/vt && \  
cp vt /usr/local/pipeline/vt/ && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/vt' /home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/vt && \  
chown -R snappy:snappy /usr/local/pipeline && \  
ln -s /usr/local/pipeline/vt/vt /usr/local/bin/ && \  
rm -rvf /tmp/*  
  
# sambamba (for future use)  
RUN cd /tmp && \  
wget
https://github.com/lomereiter/sambamba/releases/download/v0.5.8/sambamba_v0.5.8_linux.tar.bz2
&& \  
tar -xjvf sambamba_v0.5.8_linux.tar.bz2 && \  
mv sambamba_v0.5.8 /usr/local/bin/sambamba && \  
chmod +rwx /usr/local/bin/sambamba && \  
rm -rf /tmp/sambamba_v0.5.8_linux.tar.bz2  
  
## VCFtools  
RUN cd /usr/local/pipeline && \  
git clone https://github.com/vcftools/vcftools.git && \  
cd vcftools && \  
git checkout v0.1.13 && \  
make && \  
make install && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/vcftools/bin' /home/snappy/.bashrc &&
\  
rm -rf .git Makefile cpp examples  
  
## Heng Li's alphanumeric (yet unstable)  
RUN cd /usr/local/pipeline && \  
git clone https://github.com/lh3/foreign.git && \  
cd foreign/sort && \  
make && \  
cp sort /usr/local/bin/ansort  
  
## pyHGVS 0.9.4 (from viapath source)  
RUN cd /tmp && \  
git clone https://github.com/viapath/hgvs.git && \  
cd hgvs && git checkout aebe5bd9683f4b5937fd653ce4b13fcd4f3ebb10 && \  
python setup.py install && \  
rm -rf /tmp/*  
  
ENV PERL5LIB /usr/local/pipeline/vcftools/perl  
  
CMD ["/bin/bash"]  

