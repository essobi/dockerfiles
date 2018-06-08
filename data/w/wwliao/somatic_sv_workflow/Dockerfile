FROM biocontainers/biocontainers:latest  
  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="Somatic SV Workflow"  
LABEL software.version="0.2"  
LABEL description="Somatic SV workflow"  
LABEL website="https://github.com/ding-lab/somatic_sv_workflow"  
LABEL documentation="https://github.com/ding-
lab/somatic_sv_workflow/blob/master/README.md"  
LABEL license="https://github.com/ding-
lab/somatic_sv_workflow/blob/master/LICENSE"  
LABEL tags="Genomics"  
  
MAINTAINER Wen-Wei Liao <wen-wei.liao@wustl.edu>  
  
RUN conda install manta cyvcf2  
  
WORKDIR /home/biodocker  
  
COPY filter_vcf.py .  
COPY manta bin  
  
USER root  

