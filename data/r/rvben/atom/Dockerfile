FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget libxss1 libasound2 libxkbfile1 gdebi && \  
wget https://atom.io/download/deb -O atom.deb && \  
gdebi --n /atom.deb && \  
rm -rf /atom.deb && \  
apt-get -y clean && \  
apt-get -y autoremove  
  
ENV WORK_DIR /home/atom/project  
RUN useradd -m atom && \  
mkdir -p $WORK_DIR  
USER atom  
CMD atom -f $WORK_DIR  

