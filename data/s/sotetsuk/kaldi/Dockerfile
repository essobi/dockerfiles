FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -y g++ zlib1g-dev make automake libtool-bin git autoconf vim
gawk bc && \  
apt-get install -y subversion libatlas3-base bzip2 wget python2.7 && \  
ln -s /usr/bin/python2.7 /usr/bin/python && \  
ln -s -f bash /bin/sh  
  
RUN git clone https://github.com/jbender/kaldi.git /kaldi --depth=1  
  
RUN cd /kaldi/tools && make  
  
RUN cd /kaldi/src && ./configure && make depend && make  
  
RUN cd /kaldi/tools && ./extras/install_irstlm.sh  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
/opt/conda/bin/conda install -y numpy && \  
rm ~/miniconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENTRYPOINT ["bin/sh"]  

