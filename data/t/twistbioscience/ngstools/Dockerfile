FROM ubuntu:14.04  
# (from https://hub.docker.com/r/briney/abstar/~/dockerfile/)  
# Initial configuration  
RUN apt-get update --fix-missing && apt-get install -y build-essential wget \  
bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 pigz s3cmd \  
git mercurial subversion libtool automake zlib1g-dev libbz2-dev pkg-config \  
muscle mafft cd-hit unzip libfontconfig1 autoconf ncbi-blast+  
RUN ln -s /usr/bin/cdhit /usr/bin/cd-hit  
RUN mkdir /tools  
  
# Anaconda  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh
&& \  
/bin/bash /Anaconda2-4.0.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm /Anaconda2-4.0.0-Linux-x86_64.sh  
ENV PATH /opt/conda/bin:$PATH  
  
# Tini  
# What's Tini? See https://github.com/krallin/tini/  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
# PANDAseq  
RUN cd /tools && \  
git clone https://github.com/neufeld/pandaseq && \  
cd pandaseq && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
# BaseSpace Python SDK  
RUN cd /tools && \  
git clone https://github.com/basespace/basespace-python-sdk && \  
cd basespace-python-sdk/src && \  
python setup.py install  
  
# Install BaseSpaceRunDownloader  
RUN cd /tools && \  
wget
https://da1s119xsxmu0.cloudfront.net/sites/knowledgebase/API/08052014/Script/BaseSpaceRunDownloader_v2.zip
&& \  
unzip BaseSpaceRunDownloader_v2.zip && \  
rm BaseSpaceRunDownloader_v2.zip && \  
rm Run_BaseSpaceRunDownloader.bat  
  
# FASTQC  
RUN cd /tools && \  
wget
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip &&
\  
unzip fastqc_v0.11.5.zip && \  
ln -s FastQC/fastqc /usr/local/bin/fastqc  
  
# Cutadapt  
RUN pip install cutadapt  
  
# Install Spades  
RUN cd /tools && \  
wget http://cab.spbu.ru/files/release3.10.0/SPAdes-3.10.0-Linux.tar.gz && \  
tar -xzf SPAdes-3.10.0-Linux.tar.gz  
  
# Pysamstats  
# (from https://github.com/fjukstad/seq)  
RUN pip install pysam==0.8.4  
RUN pip install numpy \  
tables \  
pysamstats  
  
# SeqPrep  
RUN cd /tools && \  
wget https://github.com/jstjohn/SeqPrep/archive/master.zip && \  
unzip master.zip && \  
rm master.zip && \  
cd SeqPrep-master && \  
make && \  
cp SeqPrep /usr/local/bin/  
  
# Pear  
RUN cd /tools && \  
git clone https://github.com/xflouris/PEAR.git && \  
cd PEAR && ./autogen.sh && ./configure && make && \  
make install && \  
cd .. && rm -r PEAR  
  
# Install MultiQC  
RUN pip install multiqc  
  
# Illuminate  
RUN pip install illuminate  
# fix per: https://bitbucket.org/invitae/illuminate/issues/5/writing-to-csv  
RUN sed -i '3 a import cStringIO' /opt/conda/lib/python2.7/site-
packages/illuminate/base_parser_class.py  
  
# Install awscli  
RUN pip install awscli  
RUN mkdir /root/.aws  
  
# Install csvkit  
RUN pip install csvkit  
  
# Install parallel (and not the super old one from the ubuntu repo)  
RUN cd /tools && wget
http://ftpmirror.gnu.org/parallel/parallel-20170222.tar.bz2 && \  
tar -xvjf parallel-20170222.tar.bz2 && \  
cd parallel-20170222 && \  
./configure && make && make install && \  
cd .. && rm -rf parallel-20170222*  
  
# Install ART  
RUN cd /tools && \  
wget
https://www.niehs.nih.gov/research/resources/assets/docs/artbinmountrainier20160605linux64tgz.tgz
&& \  
tar xvzf artbinmountrainier20160605linux64tgz.tgz  
  
# Install seqtk  
RUN cd /tools && git clone https://github.com/lh3/seqtk.git && \  
cd seqtk && make && cp seqtk /usr/local/bin/  
  
# Python graphing  
RUN pip install matplotlib seaborn  
  
# Install fadapa  
RUN pip install fadapa  
  
# Install biopython  
RUN pip install biopython  
  
#  
RUN pip install python-levenshtein  
  
RUN pip install sh  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  

