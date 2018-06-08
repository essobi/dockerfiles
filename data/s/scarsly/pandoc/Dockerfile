FROM scarsly/terminal  
  
WORKDIR /source  
  
USER root  
  
RUN apt-get update -y  
  
RUN apt-get install -y --no-install-recommends \  
pandoc \  
texlive-latex-base \  
texlive-xetex latex-xcolor \  
texlive-math-extra \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-bibtex-extra \  
texlive-lang-french \  
fontconfig \  
lmodern  
  
USER dev  
  
ENTRYPOINT ["pandoc"]  
  
CMD ["--help"]  

