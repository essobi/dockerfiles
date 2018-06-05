FROM broadinstitute/picard  
  
ENV picard=/usr/picard/picard.jar  
  
RUN apt-get update &&\  
apt-get -y install ca-certificates &&\  
mkdir /usr/STAR/ &&\  
cd /usr/STAR &&\  
wget https://github.com/alexdobin/STAR/raw/master/bin/Linux_x86_64_static/STAR
&&\  
chmod +x STAR  
  
ENV PATH "/usr/STAR:${PATH}"  
COPY Drop-seq_tools-1.12.zip /usr/drop-seq/Drop-seq_tools-1.12.zip  
RUN apt-get update &&\  
apt-get -y install unzip &&\  
cd /usr/drop-seq &&\  
unzip Drop-seq_tools-1.12.zip &&\  
rm Drop-seq_tools-1.12.zip  
  
ENV dropseq=/usr/drop-seq/Drop-seq_tools-1.12  
  
WORKDIR /home/drop-seq  
  
ENTRYPOINT []  

