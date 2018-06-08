FROM nathankw/python2:2.7.14  
LABEL maintainer "Nathaniel Watson nathankw@stanford.edu"  
#Folders /srv/src and /srv/software were created in the base image.  
#INSTALL Python package cutadapt for adapter trimming. Needed by TrimGalore.  
RUN pip install cutadapt  
  
#INSTALL Trim Galore v0.4.1.  
RUN mkdir -p /srv/software/TrimGalore && \  
cd /srv/software/TrimGalore && \  
wget
http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/trim_galore_v0.4.1.zip
&& \  
unzip trim_galore_v0.4.1.zip && \  
mv trim_galore_zip/* . && \  
rm -rf trim_galore_zip trim_galore_v0.4.1.zip  
ENV PATH=/srv/software/TrimGalore/:${PATH}  
  
#INSTALL FASTQC v0.11.5  
# trim_galore can call FASTQC if the --fastqc switch is used.  
RUN mkdir /srv/software/FASTQC && \  
cd /srv/software/FASTQC && \  
wget
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip &&
\  
unzip fastqc_v0.11.5.zip && \  
rm fastqc_v0.11.5.zip && \  
cd FastQC && \  
chmod a+x fastqc  
ENV PATH=/srv/software/FASTQC/FastQC:${PATH}  
  
WORKDIR /home  
#the default workdir is /  
#CMD ["--help"]  
#ENTRYPOINT ["trim_galore"]  

