FROM nathankw/python2:2.7.14  
LABEL maintainer "Nathaniel Watson nathankw@stanford.edu"  
#Folders /srv/src and /srv/software were created in the base image.  
#INSTALL illumina_fastq git repos  
RUN cd /srv/software \  
&& git clone https://github.com/StanfordBioinformatics/illumina_fastq.git  
  
ENV PYTHONPATH=/srv/software/:${PYTHONATH}  
ENV PATH=/srv/software/illumina_fastq/scripts:${PATH}  
  
WORKDIR /home  
#the default workdir is /  
CMD ["--help"]  
ENTRYPOINT ["add_mate_reads.py"]  

