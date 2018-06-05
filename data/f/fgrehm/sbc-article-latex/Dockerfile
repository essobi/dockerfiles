FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
texlive \  
texlive-latex-extra \  
texlive-lang-portuguese \  
texlive-math-extra \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
ADD ./package /usr/share/texmf/  
RUN texhash  

