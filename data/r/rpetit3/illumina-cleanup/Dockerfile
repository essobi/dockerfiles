FROM rpetit3/nextconda-base  
  
MAINTAINER robbie.petit@gmail.com  
  
RUN apt-get -qq update \  
&& apt-get -qq -y --no-install-recommends install g++ gcc zlib1g-dev \  
&& conda install -y spades==3.11.1 \  
&& conda install -y bbmap==37.62 \  
&& pip install numpy \  
&& conda clean --all --yes \  
&& apt-get -qq -y autoremove \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/log/dpkg.log /tmp/* /var/tmp/*  
  
# FASTQ tools  
COPY src /tmp/src  
RUN cd /tmp/src \  
&& g++ -Wall -O3 -o /usr/local/bin/fastq-interleave fastq-interleave.cpp \  
&& g++ -Wall -O3 -o /usr/local/bin/fastq-stats fastq-stats.cpp \  
&& rm *.cpp \  
&& chmod 755 ./* \  
&& mv ./* /usr/local/bin \  
&& mkdir -p /opt/references/ /data \  
&& rm -rf /tmp/*  
  
COPY data /opt/references  
  
WORKDIR /data  
  
CMD ["illumina-cleanup.nf", "--help"]  

