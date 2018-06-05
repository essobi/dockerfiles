FROM ubuntu  
RUN apt-get -y update  
RUN apt-get install -y wget gzip zip bzip2 python git  
RUN mkdir /usr/tools && cd /usr/tools  
RUN mkdir /usr/tools/bin  
#WORKDIR /usr/tools  
### install conda  
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh  
RUN echo "yes\nyes\n" > conda_inst_stdin.txt  
RUN bash Miniconda2-latest-Linux-x86_64.sh < conda_inst_stdin.txt  
RUN export PATH=/root/miniconda2/bin:$PATH  
ENV PATH /root/miniconda2/bin:$PATH  
RUN conda list  
RUN conda config --add channels r  
RUN conda config --add channels bioconda  
  
#### install bowtie  
RUN conda install -y bowtie  
  
#### get bowtie_wrapper.py  
RUN mkdir /tmp/bowtie  
WORKDIR /tmp/bowtie  
  
RUN git clone https://github.com/galaxyproject/tools-devteam bowtie_deps  
RUN cp bowtie_deps/tools/bowtie_wrappers/bowtie_wrapper.py
/usr/tools/bin/bowtie_wrapper.py  
RUN chmod a+x /usr/tools/bin/bowtie_wrapper.py  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /usr/tools/bin  
  

