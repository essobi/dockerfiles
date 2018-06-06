FROM ubuntu:xenial  
  
LABEL maintainer="foersterfrank@gmx.de"  
  
RUN apt update && apt install --yes --no-install-recommends \  
liblog-log4perl-perl \  
libmoose-perl \  
libfile-which-perl \  
libipc-run-perl \  
libterm-progressbar-perl \  
libgraph-perl \  
bowtie2 \  
ncbi-blast\+ \  
samtools \  
bedtools \  
r-base \  
ghostscript \  
jellyfish \  
wget \  
build-essential \  
git \  
zlib1g-dev \  
python3-setuptools \  
openjdk-8-jre-headless \  
libncurses5-dev \  
libbz2-dev \  
liblzma-dev \  
python3 && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
RUN wget -O spades.tar.gz \  
http://spades.bioinf.spbau.ru/release3.11.1/SPAdes-3.11.1-Linux.tar.gz && \  
tar xvzf spades.tar.gz && \  
rm spades.tar.gz  
ENV PATH=/opt/SPAdes-3.11.1-Linux/bin/:"$PATH"  
  
RUN wget
https://github.com/samtools/samtools/releases/download/1.4.1/samtools-1.4.1.tar.bz2
&& \  
tar xjf samtools-1.4.1.tar.bz2 && \  
cd samtools-1.4.1 && \  
./configure && \  
make && \  
make check && \  
make install && \  
cd .. && \  
rm -rf samtools-1.4.1 samtools-1.4.1.tar.bz2  
  
RUN apt update && apt install --yes --no-install-recommends \  
mummer \  
python-numpy \  
python-matplotlib \  
time && \  
git clone --branch 0.5.0 https://github.com/isovic/racon.git racon && \  
cd racon && \  
make modules && \  
make tools && \  
make && \  
find -type d -name ".git" | xargs rm -rf && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH=/opt/racon/bin/:"$PATH"  
  
RUN mkdir pilon-1.22 && \  
cd pilon-1.22 && \  
wget
https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar
&& \  
ln -s pilon-1.22.jar pilon.jar && \  
bash -c 'echo -e "#!/bin/bash\njava -Xmx2G -jar /opt/pilon-1.22/pilon.jar $@"
> pilon' && \  
chmod +x pilon  
ENV PATH=/opt/pilon-1.22/:"$PATH"  
  
ENV PYTHONPATH=/opt/lib/python3.5/site-packages/  
ENV PATH=/opt/bin/:"$PATH"  
RUN git clone --branch v0.4.4 https://github.com/rrwick/Unicycler.git
/opt/unicycler && \  
cd /opt/unicycler && \  
rm -rf .git && \  
sed -i 's/str(min(8, multiprocessing.cpu_count/str(min(1,
multiprocessing.cpu_count/' setup.py && \  
python3 setup.py install --prefix=/opt/  
  
RUN apt update && apt install --yes --no-install-recommends git && rm -rf
/var/lib/apt/lists/*  
RUN git clone --recursive \  
\--branch v1.0.3 \  
https://github.com/chloroExtractorTeam/chloroExtractor.git \  
/opt/chloroExtractor/ && \  
find /opt/chloroExtractor -type d -name ".git" | xargs rm -rf  
ENV PATH "/opt/chloroExtractor/bin/:$PATH"  
  
VOLUME /data  
  
WORKDIR /data  
  
ENTRYPOINT ["/opt/chloroExtractor/bin/ptx"]  
  
CMD ["--help"]  

