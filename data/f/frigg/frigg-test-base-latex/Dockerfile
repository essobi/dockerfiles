FROM ubuntu:14.04  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get install -y texlive-full  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git unzip vim wget poppler-utils  
  
RUN wget
https://github.com/jgm/pandoc/releases/download/1.13.2/pandoc-1.13.2-1-amd64.deb  
RUN dpkg -i pandoc-1.13.2-1-amd64.deb  
  
RUN wget http://mirrors.ctan.org/support/texcount/texcount.pl -O
/usr/local/bin/texcount && chmod +x /usr/local/bin/texcount  

