FROM ubuntu:16.04  
MAINTAINER Fabian Wrede (forked from Vincent von Hof <vincent@vhof.de>,
Andreas Fuchs)  
  
RUN apt-get update -qyy  
RUN apt-get install -qyy texlive-full \  
texlive-latex-extra \  
python \  
python-pygments \  
biber \  
latexmk \  
make  
  
# Clean up APT when done.  
RUN apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  

