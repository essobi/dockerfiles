FROM python:2.7  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
make g++ gcc cmake git libx11-dev libxpm-dev libxft-dev libxext-dev python
lsb-release locales libxml2-dev python-dev libgsl0-dev ccache \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -f UTF-8 en_US.UTF-8  
  
ADD build.sh /  
ENV PATH="/usr/local/root/bin:${PATH}"  
ENV LD_LIBRARY_PATH="/usr/local/root/lib/root"  

