FROM ubuntu:devel  
  
MAINTAINER Jasper Behrensdorf <behrensdorf@irz.uni-hannover.de>  
  
# Install TeX Live  
RUN apt-get update -q && apt-get install -qy \  
texlive-full \  
python-pygments gnuplot \  
&& rm -rf /var/lib/apt/lists/*

