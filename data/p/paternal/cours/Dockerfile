FROM svlentink/texlive-full  
LABEL maintainer "Louis Paternault <spalax+docker@gresille.org>"  
  
# Install softwares  
ARG DEBIAN_FRONTEND=noninteractive  
RUN \  
apt-get -y update \  
&& apt-get install --yes \  
# Misc tools  
git \  
unzip \  
wget \  
strace \  
locales \  
# Python  
python3 \  
python3-pip \  
# Other tools  
graphviz \  
&& apt-get clean  
  
# Pablo  
RUN git clone https://framagit.org/lpaternault/pablo.git /usr/share/pablo  
ENV TEXINPUTS :/usr/share/pablo  
  
# Évariste  
RUN pip3 install evariste  
  
# Set locale  
RUN locale-gen fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR.UTF-8  
ENV LC_ALL fr_FR.UTF-8  
RUN dpkg-reconfigure locales  

