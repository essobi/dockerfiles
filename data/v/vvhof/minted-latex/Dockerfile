FROM ubuntu:16.04  
MAINTAINER Vincent von Hof <vincent@vhof.de>, Andreas Fuchs  
  
RUN apt-get update -qyy  
RUN apt-get install -qyy texlive-full \  
texlive-latex-extra \  
python \  
python-pip \  
python-pygments  
  
# Clean up APT when done.  
RUN apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
VOLUME inputData/  
WORKDIR /inputData/  
ENTRYPOINT ["latexmk", "-shell-escape"]  

