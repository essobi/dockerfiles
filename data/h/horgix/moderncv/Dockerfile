FROM horgix/latex:latest  
MAINTAINER Alexis Horgix Chotard <alexis.horgix.chotard@gmail.com>  
  
RUN apt-get install -y wget unzip  
  
RUN wget http://mirrors.ctan.org/macros/latex/contrib/moderncv.zip \  
&& unzip moderncv.zip \  
&& mv moderncv /usr/share/texlive/texmf-dist/  

