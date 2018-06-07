FROM fjukstad/seqbase  
  
USER root  
WORKDIR /tools  
RUN wget
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip  
RUN unzip fastqc_v0.11.5.zip  
RUN mv FastQC fastqc  
RUN chmod +x fastqc/fastqc  
  
RUN chown -R worker:workergroup /tools  
  
# link up everything and add to path  
RUN ln -s /tools/fastqc/fastqc /usr/local/bin/fastqc  
USER worker  
  
ENTRYPOINT ["fastqc"]  

