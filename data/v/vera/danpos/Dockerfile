FROM ubuntu:xenial  
  
WORKDIR /root  
  
RUN apt-get update && \  
apt-get install -y \  
python-setuptools \  
r-base \  
python-pip \  
python-dev \  
bzip2 \  
python-rpy2 \  
liblzma-dev \  
wget  
  
RUN wget
https://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
&& \  
bunzip2 samtools-1.5.tar.bz2 && \  
tar -xvf samtools-1.5.tar && \  
cd samtools-1.5 && \  
./configure && \  
make && \  
make install && \  
cd /root && \  
rm -fr /root/samtools-1.5.tar samtools-1.5  
  
RUN wget http://lilab.research.bcm.edu/dldcc-
web/lilab/kaifuc/danpos/release/danpos-2.2.2.tgz && \  
tar -zxvf danpos-2.2.2.tgz && \  
chmod +x danpos-2.2.2/*.py && \  
cp danpos-2.2.2/*.py /usr/local/bin/ && \  
cd /root && \  
rm -fr danpos-2.2.2.tgz danpos-2.2.2  
  
ENTRYPOINT ["danpos.py"]  
  
CMD ["-h"]  

