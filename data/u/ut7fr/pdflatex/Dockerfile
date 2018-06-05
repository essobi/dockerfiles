FROM ubuntu:trusty  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
texlive-latex-base texlive-latex-recommended texlive-fonts-recommended \  
lmodern texlive-latex-extra texlive-lang-french latex-xcolor  
  
ENTRYPOINT ["pdflatex"]  

