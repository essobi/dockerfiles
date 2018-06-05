# Ubuntu base image  
FROM ubuntu:14.04  
MAINTAINER Benjamin Schubert <schubert@infomratik.uni-tuebingen.de>  
  
#installation of software  
RUN apt-get update && apt-get install -y software-properties-common \  
&& apt-get install -y python-software-properties \  
&& add-apt-repository ppa:git-core/ppa \  
&& add-apt-repository ppa:george-edison55/cmake-3.x \  
&& add-apt-repository ppa:ubuntu-toolchain-r/test \  
&& apt-get update && apt-get install -y \  
gcc-4.9 \  
g++-4.9 \  
build-essential \  
coinor-cbc \  
git \  
mercurial \  
curl \  
pkg-config \  
python \  
python-pip \  
python-dev \  
python-matplotlib \  
libmysqlclient-dev \  
libboost-dev \  
libboost-serialization-dev \  
zlib1g-dev \  
tcsh \  
gawk \  
cmake \  
r-base \  
bowtie \  
libbz2-dev \  
liblzma-dev \  
libboost-dev \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 60 --slave
/usr/bin/g++ g++ /usr/bin/g++-4.9 \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& apt-get purge  
  
  
RUN git clone https://github.com/FRED-2/ImmunoNodes.git \  
&& make -C /ImmunoNodes/src \  
&& chmod -R 777 /ImmunoNodes/  
  
#get contribs  
RUN mkdir /usr/src/LKH \  
&& mkdir /usr/src/hdf5 \  
&& curl -o /ImmunoNodes/src/data/tries/uniprot_proteome_l8.trie
"https://netcologne.dl.sourceforge.net/project/immunonode-
files/uniprot_proteome_l8.trie" \  
&& curl -o /ImmunoNodes/src/data/tries/uniprot_proteome_l9.trie
"https://netcologne.dl.sourceforge.net/project/immunonode-
files/uniprot_proteome_l9.trie" \  
&& curl -o /ImmunoNodes/src/data/tries/uniprot_proteome_l10.trie
"https://netcologne.dl.sourceforge.net/project/immunonode-
files/uniprot_proteome_l10.trie" \  
&& curl -o /ImmunoNodes/src/data/tries/uniprot_proteome_l11.trie
"https://netcologne.dl.sourceforge.net/project/immunonode-
files/uniprot_proteome_l11.trie" \  
&& curl -o /usr/local/pkg_predictors.tar.gz
"https://netcologne.dl.sourceforge.net/project/immunonode-
files/contrib/pkg_predictors.tar.gz" \  
&& curl -o /usr/src/LKH/LKH-2.0.7.tgz
"https://netcologne.dl.sourceforge.net/project/immunonode-
files/contrib/LKH-2.0.7.tgz" \  
&& curl -o /usr/src/hdf5/hdf5.tar.gz
"https://netcologne.dl.sourceforge.net/project/immunonode-
files/contrib/hdf5-1.8.18-linux-centos7-x86_64-gcc485-shared.tar.gz" \  
&& tar -xzf /usr/local/pkg_predictors.tar.gz -C /usr/local/ \  
&& tar -xzf /usr/src/LKH/LKH-2.0.7.tgz -C /usr/src/LKH/ \  
&& tar -xvf /usr/src/hdf5/hdf5.tar.gz -C /usr/src/hdf5/ \  
&& mv /usr/src/hdf5/hdf5-1.8.18-linux-centos7-x86_64-gcc485-shared/bin/*
/usr/local/bin/ \  
&& mv /usr/src/hdf5/hdf5-1.8.18-linux-centos7-x86_64-gcc485-shared/lib/*
/usr/local/lib/ \  
&& mv /usr/src/hdf5/hdf5-1.8.18-linux-centos7-x86_64-gcc485-shared/include/*
/usr/local/include/ \  
&& mv /usr/src/hdf5/hdf5-1.8.18-linux-centos7-x86_64-gcc485-shared/share/*
/usr/local/share/ \  
&& make -C /usr/src/LKH/LKH-2.0.7/ \  
&& mv /usr/src/LKH/LKH-2.0.7/LKH /usr/local/bin/ \  
&& rm -rf /usr/src/LKH/ \  
&& rm -f /usr/local/pkg_predictors.tar.gz \  
&& rm -rf /usr/src/hdf5/  
  
  
  
#HLA Typing  
#OptiType dependecies  
  
  
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH  
ENV HDF5_DIR /usr/local/  
  
RUN pip install --upgrade pip && pip install \  
setuptools==33.1.1 \  
cython \  
numpy \  
pyomo \  
pysam \  
matplotlib \  
tables \  
pandas \  
future \  
&& pip install git+https://github.com/FRED-2/Fred2@master  
  
#installing optitype form git repository (version Dec 09 2015) and wirtig
config.ini  
RUN git clone https://github.com/FRED-2/OptiType.git \  
&& sed -i -e '1i#!/usr/bin/env python\' OptiType/OptiTypePipeline.py \  
&& mv OptiType/ /usr/local/bin/ \  
&& chmod 777 /usr/local/bin/OptiType/OptiTypePipeline.py \  
&& echo "[mapping]\n\  
razers3=/usr/local/bin/razers3 \n\  
threads=1 \n\  
\n\  
[ilp]\n\  
solver=cbc \n\  
threads=1 \n\  
\n\  
[behavior]\n\  
deletebam=true \n\  
unpaired_weight=0 \n\  
use_discordant=false\n" >> /usr/local/bin/OptiType/config.ini  
  
  
#installing razers3  
RUN git clone https://github.com/seqan/seqan.git seqan-src \  
&& cd seqan-src \  
&& cmake -DCMAKE_BUILD_TYPE=Release \  
&& make razers3 \  
&& cp bin/razers3 /usr/local/bin \  
&& cd .. \  
&& rm -rf seqan-src  
  
#Seq2HLA  
RUN hg clone https://bitbucket.org/sebastian_boegel/seq2hla \  
&& sed -i -e '1i#!/usr/bin/env python\' seq2hla/seq2HLA.py \  
&& mv seq2hla/ /usr/local/bin/ \  
&& chmod 777 /usr/local/bin/seq2hla/seq2HLA.py  
  
#Fred2  
#RUN pip install --upgrade pip && pip install
git+https://github.com/FRED-2/Fred2@master  
  
  
#set envirnomental variables for prediction methods  
ENV NETCHOP /usr/local/predictors/netchop/netchop-3.1  
ENV TMPDIR /tmp  
ENV PATH
/ImmunoNodes/src/:/usr/local/bin/OptiType:/usr/local/bin/seq2hla:/usr/local/predictors/bin:$PATH  
  
  

