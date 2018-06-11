FROM continuumio/miniconda3  
MAINTAINER vsochat@stanford.edu  
  
# docker build -t vanessa/compare-containers .  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN apt-get update  
RUN apt-get -y install build-essential automake  
RUN apt-get -y install apt-utils cmake wget unzip libffi-dev libssl-dev \  
libtool autotools-dev automake autoconf git \  
libarchive-dev squashfs-tools uuid-dev \  
vim jq aria2 nginx cython  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Install singularity 2.5  
RUN git clone https://github.com/singularityware/singularity.git \  
&& cd singularity && ./autogen.sh && ./configure --prefix=/usr/local \  
&& make && make install  
  
# Install python dependencies  
RUN /opt/conda/bin/pip install --upgrade pip && \  
/opt/conda/bin/pip install spython==0.0.32 && \  
/opt/conda/bin/conda install -y pandas  
  
WORKDIR /opt  
RUN git clone -b v2.5 https://www.github.com/vsoch/singularity-python && \  
cd singularity-python && /opt/conda/bin/python setup.py install  
  
# Install container-diff and singularity container-diff  
RUN curl -LO https://storage.googleapis.com/container-diff/latest/container-
diff-linux-amd64 && \  
chmod +x container-diff-linux-amd64 && mv container-diff-linux-amd64
/usr/local/bin/container-diff && \  
curl -LO https://raw.githubusercontent.com/singularityhub/container-
diff/master/analyze-singularity.sh && \  
chmod +x analyze-singularity.sh && mv analyze-singularity.sh
/usr/local/bin/analyze-singularity.sh  
  
ADD . /code  
WORKDIR /code  
RUN mkdir -p /data  
  
# Clean up  
RUN apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/opt/conda/bin/python", "/code/compare.py"]  

