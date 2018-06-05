FROM ubuntu:xenial  
  
RUN apt update && apt install --yes \  
wget \  
build-essential \  
git \  
zlib1g-dev \  
python3-setuptools \  
ncbi-blast+ \  
bowtie2 \  
samtools \  
openjdk-8-jre-headless \  
python3  
  
WORKDIR /opt  
RUN wget -O spades.tar.gz \  
http://spades.bioinf.spbau.ru/release3.11.1/SPAdes-3.11.1-Linux.tar.gz && \  
tar xvzf spades.tar.gz && \  
rm spades.tar.gz  
ENV PATH=/opt/SPAdes-3.11.1-Linux/bin/:"$PATH"  
RUN apt install --yes \  
mummer \  
python-numpy \  
python-matplotlib \  
time && \  
git clone \--branch 0.5.0 https://github.com/isovic/racon.git racon && \  
cd racon && \  
make modules && \  
make tools && \  
make -j  
ENV PATH=/opt/racon/bin/:"$PATH"  
RUN mkdir pilon-1.22 && \  
cd pilon-1.22 && \  
wget
https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar
&& \  
ln -s pilon-1.22.jar pilon.jar && \  
bash -c 'echo -e "#!/bin/bash\njava -Xmx128G -jar /opt/pilon-1.22/pilon.jar
$@" > pilon' && \  
chmod +x pilon  
ENV PATH=/opt/pilon-1.22/:"$PATH"  
ENV PYTHONPATH=/opt/lib/python3.5/site-packages/  
ENV PATH=/opt/bin/:"$PATH"  
RUN git clone \--branch v0.4.4 https://github.com/rrwick/Unicycler.git
/opt/unicycler && \  
cd /opt/unicycler && \  
python3 setup.py install --prefix=/opt/  
  
VOLUME /data  
WORKDIR /data  

