FROM flowcraft/bowtie2_samtools:1.0.0-1  
WORKDIR /index_hg19  
  
RUN wget ftp://ftp.ccb.jhu.edu/pub/data/bowtie2_indexes/hg19.1.zip  
RUN wget ftp://ftp.ccb.jhu.edu/pub/data/bowtie2_indexes/hg19.2.zip  
RUN wget ftp://ftp.ccb.jhu.edu/pub/data/bowtie2_indexes/hg19.3.zip  
  
RUN unzip hg19.1.zip  
RUN unzip hg19.2.zip  
RUN unzip hg19.3.zip  
  
RUN rm hg19.1.zip hg19.2.zip hg19.3.zip  
  
ENV PATH="/index_hg19:$PATH"  
WORKDIR /NGStools/renamePE_samtools  
  
RUN wget
https://raw.githubusercontent.com/miguelpmachado/pythonScripts/master/renamePE_samtoolsFASTQ.py  
RUN chmod +x renamePE_samtoolsFASTQ.py  
  
ENV PATH="NGStools/renamePE_samtools:$PATH"

