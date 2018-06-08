FROM python:3.6-slim  
  
RUN apt-get update -y \  
&& apt-get install --no-install-recommends -y \  
texlive \  
texlive-latex-recommended \  
texlive-fonts-recommended \  
texlive-latex-extra \  
texlive-math-extra \  
texlive-lang-english \  
texlive-lang-german \  
texlive-science \  
latexmk  
  
RUN pip install --upgrade pip && \  
pip install -U \  
sphinx \  
sphinx_rtd_theme \  

