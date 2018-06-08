################## BASE IMAGE ######################  
FROM biocontainers/biocontainers:latest  
  
################## METADATA ######################  
  
LABEL base_image="biocontainers:latest"  
LABEL version="1.0"  
LABEL software="vt-nf"  
LABEL software.version="1.0"  
LABEL about.summary="vt normalization with nextflow"  
LABEL about.home="http://github.com/IARCbioinfo/vt-nf"  
LABEL about.documentation="http://github.com/IARCbioinfo/vt-nf"  
LABEL about.license_file="http://github.com/IARCbioinfo/vt-nf"  
LABEL about.license="GNU-3.0"  
  
################## MAINTAINER ######################  
MAINTAINER Tiffany Delhomme <delhommet@students.iarc.fr>  
  
################## INSTALLATION ######################  
  
RUN conda install vt  
RUN conda install -c bioconda tabix  

