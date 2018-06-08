FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y \  
texlive-latex-base \  
texlive-xetex \  
texlive-lang-french \  
&& rm -rf /var/lib/apt/lists/*  
  
# Ideas: latex-xcolor texlive-math-extra texlive-latex-extra  
# texlive-fonts-extra texlive-bibtex-extra fontconfig lmodern  
# fonts-font-awesome  
ENV PANDOC_VERSION "2.0.3"  
RUN apt-get update && apt-get install -y curl  
  
RUN curl
https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/pandoc-${PANDOC_VERSION}-linux.tar.gz
-sLo /pandoc-${PANDOC_VERSION}-linux.tar.gz \  
&& tar xvf pandoc-${PANDOC_VERSION}-linux.tar.gz \  
&& mv pandoc-${PANDOC_VERSION}/bin/pandoc /usr/bin/pandoc \  
&& rm -r pandoc-${PANDOC_VERSION}-linux.tar.gz pandoc-${PANDOC_VERSION}  
  
CMD ["/usr/bin/pandoc"]  

