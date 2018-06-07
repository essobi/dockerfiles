FROM debian:stretch  
  
RUN apt-get update \  
&& apt-get install --assume-yes \  
texlive-full \  
biber \  
latexmk \  
make \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

