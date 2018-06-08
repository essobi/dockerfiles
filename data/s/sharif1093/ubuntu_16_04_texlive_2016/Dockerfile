FROM ubuntu:xenial  
  
RUN apt-get update && \  
apt-get install -y \  
software-properties-common \  
python-software-properties \  
debconf-utils \  
apt-utils \  
ttf-ubuntu-font-family \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
  
RUN add-apt-repository -y ppa:jonathonf/texlive-2016 && \  
apt-get update && \  
apt-get install -y \  
texlive-full \  
&& rm -rf /var/lib/apt/lists/* \  
&& add-apt-repository --remove ppa:jonathonf/texlive-2016  

