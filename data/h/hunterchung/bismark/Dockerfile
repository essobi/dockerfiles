FROM hunterchung/bowtie2  
MAINTAINER Hunter Chung <hchung@zymoresearch.com>  
  
# RUN apt-get update && \  
# apt-get install -y \  
# samtools &&\  
# rm -rf /var/lib/apt/lists/* && \  
# apt-get clean autoclean && \  
# apt-get autoremove -y  
RUN curl -L
"http://www.bioinformatics.bbsrc.ac.uk/projects/bismark/bismark_v0.14.5.tar.gz"
> /bismark_v0.14.5.tar.gz &&\  
tar zxvf /bismark_v0.14.5.tar.gz -C / &&\  
rm /bismark_v0.14.5.tar.gz  
  
ENV PATH=${PATH}:/bismark_v0.14.5 \  
TERM=xterm  
WORKDIR /mnt  

