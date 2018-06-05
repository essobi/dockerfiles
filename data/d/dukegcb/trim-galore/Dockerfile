# trim_galore: wrapper around cutadapt and fastqc  
# https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/  
FROM dukegcb/fastqc:0.11.4  
LABEL maintainer="john.bradley@duke.edu"  
  
# install additional requirements  
RUN apt-get update && apt-get install -y \  
curl \  
unzip \  
python3-pip  
  
# Install cutadapt  
ENV CUTADAPT_VERSION 1.14  
RUN pip3 install cutadapt==${CUTADAPT_VERSION}  
  
# Install trim_galore  
ENV DEST_DIR /opt/  
ENV TRIM_GALORE_VERSION 0.4.4  
ENV TRIM_GALORE_URL
http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/  
ENV TRIM_GALORE_RELEASE trim_galore_v${TRIM_GALORE_VERSION}.zip  
  
# Make destination directory  
RUN mkdir -p $DEST_DIR  
  
WORKDIR /tmp  
  
# download and extract binaries  
# Do this in one command to avoid caching the zip file and its removal in
separate layers  
RUN curl -SLO ${TRIM_GALORE_URL}/${TRIM_GALORE_RELEASE} && unzip
${TRIM_GALORE_RELEASE} -d ${DEST_DIR} && rm ${TRIM_GALORE_RELEASE}  
  
# Link executable to /usr/local/bin  
RUN ln -s /opt/trim_galore /usr/local/bin/trim_galore  
  
CMD ["/usr/local/bin/trim_galore"]  

