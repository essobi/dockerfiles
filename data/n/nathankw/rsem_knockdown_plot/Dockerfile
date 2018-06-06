FROM nathankw/python2:2.7.14  
MAINTAINER Nathaniel Watson <nathankw@stanford.edu>  
#Folders /srv/src and /srv/software were created in the base image.  
RUN git clone https://github.com/StanfordBioinformatics/rsem_utils.git
/srv/software/rsem_utils  
ENV PATH=/srv/software/rsem_utils:${PATH}  
WORKDIR /home  
#the default workdir is /  
LABEL version="1.0" description="Compares the RSEM expression values (TPM)
from a gene or isoform in two files (control and treatment), and extracts the
TPM value from into a text file that can be used as input for creating a
plot."  
  
CMD ["-h"]  
ENTRYPOINT ["cmp_two_rsem_results_files.py"]  

