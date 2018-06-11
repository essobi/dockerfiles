FROM java:openjdk-8-jre-alpine  
ENV FASTQ_VERSION=0.11.7 PATH="/FastQC/:${PATH}"  
RUN apk add \--no-cache wget perl fontconfig ttf-dejavu && \  
wget
"https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${FASTQ_VERSION}.zip"
-O fastqc.zip && \  
unzip fastqc.zip && \  
chmod +x /FastQC/fastqc && \  
rm fastqc.zip  

