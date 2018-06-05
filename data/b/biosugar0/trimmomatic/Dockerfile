FROM openjdk:alpine  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: trimmomatic  
# Software Version: 0.36  
# Software Website: http://www.usadellab.org  
# Description: A flexible read trimming tool for Illumina NGS data  
##############################################################  
  
RUN wget
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
&& \  
unzip Trimmomatic-0.36.zip && \  
rm Trimmomatic-0.36.zip && \  
mv Trimmomatic-0.36 /data/  
  
WORKDIR /data/  

