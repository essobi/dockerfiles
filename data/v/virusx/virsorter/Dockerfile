FROM ubuntu:16.04  
ENV VIRSORTER_VERSION=1bc4cc2e4  
RUN apt-get update && \  
apt-get install -y hmmer mcl muscle ncbi-blast+ wget git perl cpanminus build-
essential libdb-dev && \  
wget "http://metagene.nig.ac.jp/metagene/mga_x86_64.tar.gz" -qO- | tar xz -C
/tmp/ && \  
mv /tmp/mga_linux_ia64 /usr/local/bin/ && \  
cpanm --force Capture::Tiny && \  
cpanm --force BioPerl && \  
cpanm File::Which && \  
git clone https://github.com/simroux/VirSorter /tmp/virsorter && \  
cd /tmp/virsorter && \  
git checkout ${VIRSORTER_VERSION} && \  
cd && \  
cp /tmp/virsorter/wrapper_phage_contigs_sorter_iPlant.pl /usr/local/bin/ && \  
cp -r /tmp/virsorter/Scripts/ /usr/local/bin/Scripts/ && \  
apt-get purge -y build-essential git wget cpanminus && \  
apt-get autoremove -y --purge && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

