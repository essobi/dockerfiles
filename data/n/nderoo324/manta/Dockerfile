# Base Image  
FROM biocontainers/biocontainers:latest  
  
# Metadata  
LABEL base.image="biocontainers/biocontainers:latest"  
LABEL version="1.0.3"  
LABEL software="manta"  
LABEL software.version="1.0.3"  
LABEL description="Illumina's Manta caller for SV"  
LABEL website="https://github.com/Illumina/manta"  
LABEL documentation="https://github.com/Illumina/manta"  
LABEL license="https://github.com/Illumina/manta"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Andrew Wong <nderoo.wong@gmail.com>  
  
# Change USER to root  
USER root  
  
COPY . /home/biodocker  
  
WORKDIR /home/biodocker  
  
# Install manta  
RUN wget
https://github.com/Illumina/manta/releases/download/v1.0.3/manta-1.0.3.centos5_x86_64.tar.bz2
&& \  
tar -xvjf manta-1.0.3.centos5_x86_64.tar.bz2  
  
ENTRYPOINT ["python", "run_manta.py"]  
  
CMD ["-h"]  

