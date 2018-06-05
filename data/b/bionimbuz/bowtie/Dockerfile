FROM ubuntu:trusty  
MAINTAINER Tiago Alves "tiagoalves83@gmail.com"  
ENV APP_DOWNLOAD_LINK https://sourceforge.net/projects/bowtie-
bio/files/bowtie/1.1.2/bowtie-1.1.2-linux-x86_64.zip/download  
  
RUN apt-get -y update && apt-get -y install \  
python \  
unzip \  
wget  
  
RUN wget -O bowtie.zip $APP_DOWNLOAD_LINK  
  
RUN unzip -o bowtie.zip -d /bin  
  
RUN ln -s /bin/bowtie-* /bin/bowtie-latest  
  
ENTRYPOINT ["/bin/bowtie-latest/bowtie"]  
CMD ["--help"]  

