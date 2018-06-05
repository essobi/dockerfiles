FROM pwlb/rna-seq-pipeline-base:v0.1.0  
COPY install /install  
RUN Rscript /install/install.R  
  
# determine the sampleid from the complete path, this extracts the  
# base file name and then takes the part of the name in front of the  
# first underscore (so /a/b/c/123_S95_L003_R1_001.fastq.gz -> 123)  
ENV FILTERSAMPLEID "awk -F \"/\" '{print \$NF}'|cut -d'_' -f1"  
ENV THREADS 1  
ENV JOBS 1  
COPY scripts /scripts  
  
ENTRYPOINT ["bash","/scripts/run-all.sh"]  
CMD [""]  

