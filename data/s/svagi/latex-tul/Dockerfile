FROM svagi/latex  
MAINTAINER Jan Svager <jan@svager.cz>  
  
# Install additional packages specific for TUL  
RUN apt-get update \  
&& apt-get --no-install-recommends install -y \  
texlive-lang-czechslovak \  
texlive-generic-extra \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Install TUL package  
COPY ./tul-1.2 /usr/share/texmf/tex/latex/  
RUN texhash  

