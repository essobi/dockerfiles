FROM fpco/stack-build:lts-11.2  
  
RUN apt-get update && apt-get install -y \  
texlive-latex-recommended  
  
  
RUN stack install pandoc  
  
  
RUN apt-get install -y texlive-xetex  
RUN apt-get install -y texlive-math-extra  

