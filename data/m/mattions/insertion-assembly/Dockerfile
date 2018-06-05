FROM continuumio/miniconda  
  
# Deps  
# - ps2pdf | apt-get  
# - stretcher (emboss tool set) | apt-get  
# - fastlength (exonarate utilities) | apt-get  
RUN apt-get update && apt-get install -y ghostscript \  
emboss \  
exonerate  
  
# - samtools | bioconda  
# - bedtools | bioconda  
# - blat | bioconda  
RUN conda install -y -c bioconda samtools bedtools blat numpy  
  
# - cap3 (it needs a commercial license)  
# - repeatmasker (it needs a commercial license for the repeatlibrary)  
RUN mkdir /code  
  
WORKDIR /code  
  
# - fastq_to_fasta (from
http://nebc.nerc.ac.uk/downloads/scripts/parse/fastq_to_fasta.py)  
RUN wget http://nebc.nerc.ac.uk/downloads/scripts/parse/fastq_to_fasta.py  
  
ADD . /code  
  
ENV PATH $PATH:.  

