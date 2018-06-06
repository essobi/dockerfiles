FROM ummidock/ubuntu_base:latest  
  
WORKDIR /NGStools/  
  
RUN apt-get update  
  
# -- General Dependencies ---  
RUN apt-get install -y git wget make gcc libxml2-dev libxslt1-dev zlib1g-dev
g++ build-essential libncurses5-dev libncursesw5-dev  
RUN apt-get install -y python-dev python-pip  
RUN apt-get install -y lbzip2 unzip  
  
# -- PneumoCaT Dependencies ---  
#Bowtie2  
RUN wget https://downloads.sourceforge.net/project/bowtie-
bio/bowtie2/2.2.9/bowtie2-2.2.9-linux-x86_64.zip && unzip
bowtie2-2.2.9-linux-x86_64.zip && rm bowtie2-2.2.9-linux-x86_64.zip  
ENV PATH="/NGStools/bowtie2-2.2.9:${PATH}"  
#Samtools  
RUN wget
https://downloads.sourceforge.net/project/samtools/samtools/0.1.19/samtools-0.1.19.tar.bz2
&& tar -xf samtools-0.1.19.tar.bz2 && rm samtools-0.1.19.tar.bz2  
WORKDIR samtools-0.1.19  
RUN make  
ENV PATH="/NGStools/samtools-0.1.19:${PATH}"  
WORKDIR /NGStools/  
  
#Python dependencies  
RUN pip2 install PyYaml numpy lxml pysam biopython  
  
# -- PneumoCaT ---  
RUN git clone https://github.com/phe-bioinformatics/PneumoCaT.git  
ENV PATH="/NGStools/PneumoCaT:${PATH}"  
#CMD PneumoCaT.py --help

