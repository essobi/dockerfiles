FROM ubuntu:16.04  
LABEL author="Kersten Breuer, Zeller Team, EMBL 2017" \  
maintainer="kersten-breuer@outlook.com"  
  
# Install essential unix packages and dependencies:  
RUN apt-get update -y --fix-missing  
RUN apt-get install -y build-essential \  
python-dev \  
python-pip  
  
## Install MultiQC:  
ENV MULTIQC_VERSION 1.3  
RUN pip install multiqc==${MULTIQC_VERSION}  
  
CMD ["multiqc"]

