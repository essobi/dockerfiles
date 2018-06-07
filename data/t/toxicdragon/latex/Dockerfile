FROM ubuntu:artful  
  
RUN apt-get update \  
&& apt-get install --yes \--no-install-recommends \  
lmodern \  
texlive-latex-base \  
texlive-lang-german \  
texlive-lang-english \  
texlive-binaries \  
texlive-latex-extra \  
texlive-generic-extra \  
texlive-science \  
texlive-full \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-font-utils \  
texlive-xetex \  
texlive-luatex \  
latexmk \  
biber \  
python-pygments \  
gnuplot \  
make \  
inkscape\  
&& apt-get remove --yes \  
texlive-latex-base-doc \  
texlive-latex-recommended-doc \  
texlive-latex-extra-doc \  
texlive-fonts-recommended-doc \  
texlive-fonts-extra-doc \  
texlive-humanities-doc \  
texlive-latex-base-doc \  
texlive-latex-extra-doc \  
texlive-latex-recommended-doc \  
texlive-metapost-doc \  
texlive-pictures-doc \  
texlive-pstricks-doc \  
texlive-publishers-doc \  
texlive-science-doc \  
&& apt-get autoclean \  
&& apt-get --purge --yes autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

