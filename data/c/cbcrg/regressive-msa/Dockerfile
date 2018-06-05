FROM debian:jessie  
MAINTAINER Evan Floden <evanfloden@gmail.com>  
  
## Docker image for TCOFFEE DPA including all the requirements  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ed \  
less \  
vim-tiny \  
wget \  
git \  
python \  
build-essential \  
cmake \  
curl \  
libargtable2-0 \  
ca-certificates \  
libpng12-0 \  
python-biopython \  
python-numpy \  
ruby \  
python-setuptools \  
default-jdk \  
libpng-dev  
  
# install argtable 2  
RUN wget http://prdownloads.sourceforge.net/argtable/argtable2-13.tar.gz && \  
tar -zxf argtable2-13.tar.gz && \  
cd argtable2-13 && \  
./configure && \  
make && \  
make install && \  
rm /argtable2-13.tar.gz  
  
# install CLUSTAL OMEGA  
RUN wget http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz && \  
tar -zxf clustal-omega-1.2.4.tar.gz && \  
cd clustal-omega-1.2.4 && \  
./configure && \  
make && \  
make install && \  
rm /clustal-omega-1.2.4.tar.gz  
  
# install MAFFT  
RUN wget http://mafft.cbrc.jp/alignment/software/mafft-7.397-with-extensions-
src.tgz && \  
tar xfvz mafft-7.397-with-extensions-src.tgz && \  
cd mafft-7.397-with-extensions/core/ && \  
sed -i "s/PREFIX = \/usr\/local/PREFIX = \/mafft/g" Makefile && \  
sed -i "s/BINDIR = \$(PREFIX)\/bin/BINDIR = \/mafft\/bin/g" Makefile && \  
make clean && \  
make && \  
make install && \  
wget http://mafft.cbrc.jp/alignment/software/newick2mafft.rb && \  
chmod +x newick2mafft.rb && \  
export "PATH=$PATH:/mafft/bin" && \  
export MAFFT_BINARIES="" && \  
cp /mafft/bin/* /bin/. && \  
mv /mafft-7.397-with-extensions /mafft && \  
rm /mafft-7.397-with-extensions-src.tgz  
  
# Install PROBCONS  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
probcons  
  
# Install MSAProbs  
RUN wget
"https://downloads.sourceforge.net/project/msaprobs/MSAProbs-0.9.7.tar.gz" -O
msaprobs.tar.gz && \  
tar zxf msaprobs.tar.gz && \  
cd MSAProbs-0.9.7/MSAProbs && \  
make && \  
cp msaprobs /usr/bin && \  
rm /msaprobs.tar.gz  
  
# install UPP  
RUN git clone http://github.com/smirarab/sepp.git && \  
cd sepp && \  
mkdir -p /home/lib/python2.7/site-packages/ && \  
export PYTHONPATH=$PYTHONPATH:/home/lib/python2.7/site-packages/ && \  
python setup.py config -c && \  
echo "/home/" > /sepp/home.path && \  
sed -i "s/root/home/g" /sepp/.sepp/main.config && \  
python setup.py install --prefix=/home/ && \  
python setup.py develop && \  
mkdir /pasta-code && \  
cd /pasta-code && \  
git clone https://github.com/smirarab/pasta.git && \  
git clone https://github.com/smirarab/sate-tools-linux.git && \  
cd pasta && \  
python setup.py develop -user && \  
export PATH=$PATH:/pasta-code/pasta:/sepp && \  
cd /sepp && \  
python setup.py upp -c && \  
sed -i "s/root/home/g" /sepp/.sepp/upp.config && \  
cd /pasta-code/pasta && \  
python setup.py develop  
  
# Install MSA  
RUN wget ftp://ftp.ncbi.nih.gov/pub/msa/msa.tar.Z && \  
tar xfvz msa.tar.Z &&\  
cd msa && \  
make clean && \  
make msa && \  
rm /msa.tar.Z && \  
chmod +x /msa/msa && \  
cp /msa/msa /bin/.  
  
# Install TCOFFEE  
RUN git clone https://github.com/cbcrg/tcoffee.git tcoffee && \  
cd tcoffee && \  
git checkout 3c3d66e9797f32beaff56cf3d06522b8dd65460f && \  
cd compile && \  
make t_coffee && \  
cp t_coffee /bin/.  
  
ENV CACHE_4_TCOFFEE='${TMPDIR:-/tmp}/.tcoffee/cache'  
ENV LOCKDIR_4_TCOFFEE='${TMPDIR:-/tmp}/.tcoffee/lock'  
ENV TMP_4_TCOFFEE='${TMPDIR:-/tmp}/.tcoffee/tmp'  
  
# Test Data  
RUN mkdir /test_data && \  
cd test_data && \  
wget https://raw.githubusercontent.com/skptic/dpa-
analysis/master/tutorial/seqs/rnasemam.fa && \  
wget https://raw.githubusercontent.com/skptic/dpa-
analysis/master/tutorial/seqs/seatoxin.fa && \  
wget https://raw.githubusercontent.com/skptic/dpa-
analysis/master/tutorial/refs/rnasemam.ref && \  
wget https://raw.githubusercontent.com/skptic/dpa-
analysis/master/tutorial/refs/seatoxin.ref && \  
wget https://raw.githubusercontent.com/skptic/dpa-
analysis/master/tutorial/trees/rnasemam.dnd && \  
wget https://raw.githubusercontent.com/skptic/dpa-
analysis/master/tutorial/trees/seatoxin.dnd  

