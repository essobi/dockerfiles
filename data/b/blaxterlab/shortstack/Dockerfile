FROM ubuntu:16.04  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y bowtie software-properties-common cpanminus  
RUN apt-add-repository ppa:j-4/vienna-rna  
RUN apt-get update  
RUN apt-get install -y bedtools vienna-rna  
RUN apt-get install -y wget bzip2  
RUN apt-get install -y build-essential  
RUN apt-get install -y libncurses5-dev  
RUN apt-get install -y zlib1g-dev  
RUN apt-get install -y libbz2-dev  
RUN apt-get install -y liblzma-dev  
  
RUN wget
https://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
&& tar xf samtools-1.5.tar.bz2 \  
&& cd samtools-1.5 && ./configure && make && make install  
RUN wget
https://github.com/samtools/htslib/releases/download/1.5/htslib-1.5.tar.bz2 &&
tar xf htslib-1.5.tar.bz2 \  
&& cd htslib-1.5 && ./configure && make && make install  
RUN wget
https://github.com/samtools/bcftools/releases/download/1.5/bcftools-1.5.tar.bz2
&& tar xf bcftools-1.5.tar.bz2 \  
&& cd bcftools-1.5 && ./configure && make && make install  
  
RUN curl
https://raw.githubusercontent.com/MikeAxtell/ShortStack/v3.8.3/ShortStack
>ShortStack  
RUN chmod a+x ShortStack  
ENV PATH /:$PATH  
CMD ShortStack  

