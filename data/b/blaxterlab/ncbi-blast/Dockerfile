FROM debian:jessie  
LABEL maintainer "sujaikumar@gmail.com"  
  
RUN apt-get update && apt-get install -y \  
parallel \  
wget  
  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz && \  
tar xzf ncbi-blast-2.6.0+-x64-linux.tar.gz  
  
ENV PATH=".:/ncbi-blast-2.6.0+/bin:${PATH}"  
RUN mkdir /query && mkdir /db && mkdir /out  
  
RUN adduser --disabled-password --gecos '' dockeruser  
  
RUN chown -R dockeruser /out  
  
COPY blast.pl /  
  
RUN chmod a+x blast.pl  
  
RUN parallel ln -s blast.pl {} ::: blastn blastp blastx deltablast psiblast
rpsblast rpstblastn tblastn tblastx  
  
USER dockeruser  

