FROM ubuntu:yakkety  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
latexmk \  
lmodern \  
texlive-full \  
texlive-lang-japanese \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /app  
WORKDIR /app  
  
CMD ["latexmk"]  

