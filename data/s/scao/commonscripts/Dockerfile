FROM biocontainers/biocontainers:latest  
  
LABEL base.image="biocontainers:latest"  
LABEL description="commonly used scripts"  
LABEL tags="Genomics"  
  
MAINTAINER Song Cao <songcao@gmail.com>  
  
USER root  
  
RUN conda install git samtools  
WORKDIR /home/biodocker  
RUN git clone https://github.com/caosgc33d/commonscripts.git  

